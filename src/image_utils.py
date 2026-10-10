"""
PlantGuard AI - Image Processing & Validation Utilities
Handles safe image reading, format validation, size checks, and local storage.
"""

import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Tuple, Union, Optional
from PIL import Image, UnidentifiedImageError

from config import (
    ALLOWED_EXTENSIONS,
    MAX_FILE_SIZE_MB,
    MAX_IMAGE_DIMENSION,
    MIN_IMAGE_DIMENSION,
    UPLOADS_DIR,
)


class ImageValidationError(ValueError):
    """Raised when an uploaded image fails validation."""
    pass


def validate_and_load_image(
    image_input: Union[str, Path, Image.Image]
) -> Tuple[Image.Image, Optional[Path]]:
    """
    Validates and loads an image from a file path or PIL Image instance.

    Args:
        image_input: Path to image file or existing PIL Image.

    Returns:
        Tuple of (PIL.Image in RGB mode, optional Path to original file).

    Raises:
        ImageValidationError: If format, size, or dimensions are invalid.
    """
    if image_input is None:
        raise ImageValidationError("No image provided. Please upload a leaf photo.")

    file_path: Optional[Path] = None

    if isinstance(image_input, (str, Path)):
        file_path = Path(image_input)
        if not file_path.exists():
            raise ImageValidationError(f"File not found: {file_path}")

        # Check file extension
        ext = file_path.suffix.lower()
        if ext not in ALLOWED_EXTENSIONS:
            allowed_str = ", ".join(sorted(ALLOWED_EXTENSIONS))
            raise ImageValidationError(
                f"Unsupported file format '{ext}'. Allowed formats: {allowed_str}"
            )

        # Check file size
        file_size_mb = file_path.stat().st_size / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            raise ImageValidationError(
                f"Image size ({file_size_mb:.1f} MB) exceeds maximum allowed limit ({MAX_FILE_SIZE_MB} MB)."
            )

        try:
            with Image.open(file_path) as img:
                # Fully load pixels and copy into memory so file handle can close cleanly
                img.load()
                image = img.convert("RGB").copy()
        except (UnidentifiedImageError, OSError) as e:
            raise ImageValidationError(f"Invalid or corrupted image file: {str(e)}")

    elif isinstance(image_input, Image.Image):
        image = image_input
    else:
        raise ImageValidationError(f"Unsupported image input type: {type(image_input)}")

    # Check dimensions
    width, height = image.size
    if width < MIN_IMAGE_DIMENSION or height < MIN_IMAGE_DIMENSION:
        raise ImageValidationError(
            f"Image dimensions ({width}x{height}) are too small. "
            f"Minimum size is {MIN_IMAGE_DIMENSION}x{MIN_IMAGE_DIMENSION} pixels for reliable leaf inspection."
        )

    # Convert to RGB mode (handles PNG alpha, CMYK, Palette modes)
    if image.mode != "RGB":
        image = image.convert("RGB")

    return image, file_path


def save_image_locally(image: Image.Image, prefix: str = "leaf") -> Path:
    """
    Saves an image into the local data/uploads directory with a timestamped UUID filename.
    Guarantees privacy by keeping user images strictly local.
    """
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = uuid.uuid4().hex[:8]
    filename = f"{prefix}_{timestamp}_{unique_id}.jpg"
    dest_path = UPLOADS_DIR / filename

    # Save as high-quality JPEG
    image.save(dest_path, format="JPEG", quality=92)
    return dest_path


def prepare_image_for_display(image: Image.Image, max_size: int = 800) -> Image.Image:
    """Creates a resized copy suitable for web UI preview while maintaining aspect ratio."""
    img_copy = image.copy()
    img_copy.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    return img_copy
