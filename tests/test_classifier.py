"""
Unit tests for PlantGuard AI Classifier and Inference Engine.
"""

from pathlib import Path
import pytest
from PIL import Image

from src.classifier import PlantClassifier
from src.image_utils import ImageValidationError


@pytest.fixture(scope="module")
def loaded_classifier():
    """Initializes and loads the model once for the module tests."""
    clf = PlantClassifier()
    clf.load_model()
    return clf


def test_classifier_initialization():
    """Test default initialization values."""
    clf = PlantClassifier()
    assert clf.is_loaded is False
    info = clf.get_model_info()
    assert info["architecture"].startswith("MobileNetV2")
    assert info["classes_count"] == 38
    assert len(info["supported_crops"]) == 14


def test_classifier_inference_sample(loaded_classifier):
    """Test inference on a real synthetic image."""
    img = Image.new("RGB", (224, 224), color=(40, 150, 40))
    result = loaded_classifier.predict(img)

    assert "top_prediction" in result
    assert "alternative_predictions" in result
    assert "inference_time_ms" in result
    assert "disclaimer" in result
    assert "recommendation" in result

    top = result["top_prediction"]
    assert "label" in top
    assert "confidence" in top
    assert 0.0 <= top["confidence"] <= 1.0
    assert len(result["alternative_predictions"]) == 4  # top_k=5 minus the top 1


def test_classifier_invalid_image_fails(loaded_classifier):
    """Test classifier raises ImageValidationError when bad input is passed."""
    with pytest.raises(ImageValidationError):
        loaded_classifier.predict(None)
