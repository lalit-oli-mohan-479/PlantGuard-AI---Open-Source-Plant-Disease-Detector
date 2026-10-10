"""
Unit tests for PlantGuard AI Disease Recommendations and Knowledge Base.
"""

from config import PLANT_DISEASE_CLASSES, SUPPORTED_CROPS
from src.recommendations import (
    DISEASE_KNOWLEDGE_BASE,
    get_recommendation,
    get_all_supported_crops,
    get_all_classes,
)


def test_all_classes_mapped():
    """Verify that every supported model class has an entry in DISEASE_KNOWLEDGE_BASE."""
    for class_name in PLANT_DISEASE_CLASSES:
        assert class_name in DISEASE_KNOWLEDGE_BASE, f"Missing knowledge base entry for {class_name}"


def test_recommendation_structure():
    """Verify that recommendations contain all required keys and valid data."""
    sample_classes = ["Apple Scab", "Healthy Tomato Plant", "Potato with Late Blight"]
    required_keys = {
        "crop",
        "category",
        "symptoms",
        "immediate_actions",
        "preventative_care",
        "outdoor_tasks",
    }

    for cls in sample_classes:
        rec = get_recommendation(cls)
        assert required_keys.issubset(rec.keys())
        assert len(rec["immediate_actions"]) > 0
        assert len(rec["preventative_care"]) > 0
        assert len(rec["outdoor_tasks"]) > 0
        assert isinstance(rec["symptoms"], str) and len(rec["symptoms"]) > 10


def test_fallback_recommendation():
    """Verify unknown or unlisted classes trigger the cautious generic fallback."""
    rec = get_recommendation("Completely Unknown Alien Disease")
    assert rec["category"] == "Uncertain Prediction"
    assert "outdoor_tasks" in rec
    assert len(rec["outdoor_tasks"]) > 0
    assert "visual" in rec["immediate_actions"][0].lower() or "photo" in rec["immediate_actions"][0].lower()


def test_supported_crops_coverage():
    """Verify supported crops match expected PlantVillage crop types."""
    crops = get_all_supported_crops()
    for expected_crop in SUPPORTED_CROPS:
        assert expected_crop in crops


def test_get_all_classes():
    """Verify count matches 38 canonical classes."""
    classes = get_all_classes()
    assert len(classes) == 38
