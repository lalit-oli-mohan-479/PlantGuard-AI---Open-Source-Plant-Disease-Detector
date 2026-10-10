"""
PlantGuard AI - Open-Source Plant Disease Classifier
Wraps Hugging Face Transformers MobileNetV2 architecture for local inference.
Completely open-weight, locally runnable, and private.
"""

import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from PIL import Image

import torch
import torch.nn.functional as F
from transformers import AutoImageProcessor, AutoModelForImageClassification

from config import (
    DEFAULT_MODEL_ID,
    CONFIDENCE_MEDIUM_THRESHOLD,
    CONFIDENCE_HIGH_THRESHOLD,
    SUPPORTED_CROPS,
    PLANT_DISEASE_CLASSES,
)
from src.image_utils import validate_and_load_image
from src.recommendations import get_recommendation


class PlantClassifier:
    """
    Local plant disease classifier using open-weights MobileNetV2 fine-tuned on PlantVillage.
    Executes inference strictly on local hardware (CPU/GPU) without external API dependencies.
    """

    def __init__(
        self,
        model_name_or_path: str = DEFAULT_MODEL_ID,
        device: Optional[str] = None,
    ):
        self.model_name_or_path = model_name_or_path
        if device is None:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = torch.device(device)

        self.processor: Optional[AutoImageProcessor] = None
        self.model: Optional[AutoModelForImageClassification] = None
        self._is_loaded = False

    def load_model(self) -> None:
        """
        Loads the preprocessor and model weights from local cache or Hugging Face.
        """
        if self._is_loaded:
            return

        try:
            try:
                from transformers import MobileNetV2ImageProcessor
                self.processor = MobileNetV2ImageProcessor.from_pretrained(
                    self.model_name_or_path
                )
            except Exception:
                self.processor = AutoImageProcessor.from_pretrained(
                    self.model_name_or_path
                )

            self.model = AutoModelForImageClassification.from_pretrained(
                self.model_name_or_path
            )
            self.model.to(self.device)
            self.model.eval()
            self._is_loaded = True
        except Exception as e:
            raise RuntimeError(
                f"Failed to load plant disease classifier model '{self.model_name_or_path}': {str(e)}"
            )

    @property
    def is_loaded(self) -> bool:
        return self._is_loaded

    def predict(
        self,
        image_input: Union[str, Path, Image.Image],
        top_k: int = 5,
    ) -> Dict[str, Any]:
        """
        Runs local inference on a leaf image.

        Args:
            image_input: File path or PIL Image.
            top_k: Number of highest ranking predictions to return.

        Returns:
            Structured prediction dictionary containing top prediction,
            alternative predictions, confidence analysis, and care suggestions.
        """
        if not self._is_loaded:
            self.load_model()

        # Validate and prepare image
        image, _ = validate_and_load_image(image_input)

        start_time = time.perf_counter()

        # Preprocess image into PyTorch tensor
        inputs = self.processor(images=image, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # Run model inference under no_grad
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = F.softmax(logits, dim=-1)[0]

        inference_time_ms = (time.perf_counter() - start_time) * 1000

        # Retrieve top-k classes
        k = min(top_k, probabilities.shape[0])
        top_probs, top_indices = torch.topk(probabilities, k=k)

        top_predictions: List[Dict[str, Any]] = []
        for prob, idx in zip(top_probs, top_indices):
            idx_int = int(idx.item())
            prob_float = float(prob.item())
            label = self.model.config.id2label.get(idx_int, f"Class {idx_int}")
            top_predictions.append(
                {
                    "class_index": idx_int,
                    "label": label,
                    "confidence": prob_float,
                    "percentage": f"{prob_float * 100:.1f}%",
                }
            )

        primary = top_predictions[0]
        top_confidence = primary["confidence"]
        top_label = primary["label"]

        # Confidence categorization
        is_low_confidence = top_confidence < CONFIDENCE_MEDIUM_THRESHOLD
        if is_low_confidence:
            confidence_level = "Low Confidence"
            confidence_warning = (
                f"Model confidence is low ({primary['percentage']}). "
                "The image may be blurry, poorly lit, contain multiple leaves, "
                "or show a plant species not present in the 14 supported crops. "
                "Please cross-verify visually."
            )
        elif top_confidence < CONFIDENCE_HIGH_THRESHOLD:
            confidence_level = "Moderate Confidence"
            confidence_warning = (
                f"Model confidence is moderate ({primary['percentage']}). "
                "Inspect the plant carefully outdoors to corroborate symptoms."
            )
        else:
            confidence_level = "High Confidence"
            confidence_warning = None

        # Care recommendations lookup
        rec_data = get_recommendation(top_label)

        return {
            "top_prediction": {
                "label": top_label,
                "confidence": top_confidence,
                "percentage": primary["percentage"],
                "confidence_level": confidence_level,
                "crop": rec_data.get("crop", "Unknown"),
                "category": rec_data.get("category", "General"),
            },
            "alternative_predictions": top_predictions[1:],
            "all_top_k": top_predictions,
            "is_low_confidence": is_low_confidence,
            "confidence_warning": confidence_warning,
            "recommendation": rec_data,
            "inference_time_ms": round(inference_time_ms, 2),
            "device": str(self.device),
            "disclaimer": (
                "Notice: This prediction is generated by a computer vision model trained on leaf patterns. "
                "It is a helpful gardening screening tool, NOT a certified laboratory diagnosis. "
                "Environmental stressors (watering, sunburn, nutrient burns) can cause similar visual symptoms. "
                "Always verify in person and consult local agricultural extension experts before applying treatments."
            ),
        }

    def get_model_info(self) -> Dict[str, Any]:
        """Returns metadata about the active model and license."""
        return {
            "model_id": self.model_name_or_path,
            "architecture": "MobileNetV2 (google/mobilenet_v2_1.0_224)",
            "dataset": "PlantVillage / New Plant Diseases Dataset (87,000 leaf images)",
            "classes_count": len(PLANT_DISEASE_CLASSES),
            "supported_crops": SUPPORTED_CROPS,
            "model_license": "Apache 2.0 (Open Weights)",
            "dataset_license": "CC-BY-SA 4.0",
            "weights_size": "~8.9 MB",
            "hardware_requirements": "Lightweight, runs on standard CPU with ~200MB RAM",
            "is_loaded": self._is_loaded,
        }
