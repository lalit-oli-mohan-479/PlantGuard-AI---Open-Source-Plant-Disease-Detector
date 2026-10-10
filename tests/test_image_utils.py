"""
Unit tests for PlantGuard AI Image Utilities.
"""

import tempfile
from pathlib import Path
import pytest
from PIL import Image

from src.image_utils import (
    validate_and_load_image,
    save_image_locally,
    prepare_image_for_display,
    ImageValidationError,
)


def test_valid_image_loading():
    """Test loading and validating a standard valid RGB image."""
    img = Image.new("RGB", (256, 256), color=(34, 139, 34))
    validated_img, file_path = validate_and_load_image(img)
    assert validated_img is not None
    assert validated_img.mode == "RGB"
    assert validated_img.size == (256, 256)
    assert file_path is None


def test_rgba_converted_to_rgb():
    """Test that PNG with alpha channel (RGBA) is safely converted to RGB."""
    img = Image.new("RGBA", (128, 128), color=(34, 139, 34, 255))
    validated_img, _ = validate_and_load_image(img)
    assert validated_img.mode == "RGB"


def test_file_path_validation():
    """Test loading valid image from file path."""
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        img = Image.new("RGB", (100, 100), color="green")
        img.save(tmp_path, format="JPEG")

        validated_img, loaded_path = validate_and_load_image(tmp_path)
        assert validated_img is not None
        assert loaded_path == tmp_path
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass


def test_invalid_extension_rejected():
    """Test that unsupported file extensions are rejected."""
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        tmp.write(b"not an image")
        tmp_path = Path(tmp.name)

    try:
        with pytest.raises(ImageValidationError, match="Unsupported file format"):
            validate_and_load_image(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def test_corrupted_image_rejected():
    """Test that corrupted images are detected and rejected."""
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(b"corrupted data that is not a jpeg")
        tmp_path = Path(tmp.name)

    try:
        with pytest.raises(ImageValidationError, match="Invalid or corrupted"):
            validate_and_load_image(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def test_too_small_dimensions_rejected():
    """Test that images smaller than MIN_IMAGE_DIMENSION are rejected."""
    tiny_img = Image.new("RGB", (16, 16), color="green")
    with pytest.raises(ImageValidationError, match="too small"):
        validate_and_load_image(tiny_img)


def test_none_input_rejected():
    """Test that None image input raises ImageValidationError."""
    with pytest.raises(ImageValidationError, match="No image provided"):
        validate_and_load_image(None)


def test_local_saving():
    """Test saving image locally generates an existing file in data/uploads."""
    img = Image.new("RGB", (100, 100), color="darkgreen")
    saved_path = save_image_locally(img, prefix="test")
    assert saved_path.exists()
    assert saved_path.is_file()
    assert "uploads" in str(saved_path)
    # Cleanup
    saved_path.unlink(missing_ok=True)


def test_prepare_image_for_display():
    """Test thumbnail resize keeps max dimensions within bounds."""
    img = Image.new("RGB", (1600, 1200), color="forestgreen")
    preview = prepare_image_for_display(img, max_size=400)
    assert max(preview.size) <= 400
