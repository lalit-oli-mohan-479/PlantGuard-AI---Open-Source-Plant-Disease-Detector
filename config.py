"""
PlantGuard AI Configuration
Defines application constants, model metadata, class definitions, and file limits.
"""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
UPLOADS_DIR = DATA_DIR / "uploads"
MODELS_DIR = BASE_DIR / "models"
DB_PATH = DATA_DIR / "journal.db"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# App Metadata
APP_TITLE = "PlantGuard AI"
APP_SUBTITLE = "Open-Source Plant Disease Detector"
APP_TAGLINE = "Healthy Plants Start with Smart Care."
APP_VERSION = "1.0.0"

# Open-Source Model Configuration
# Model: linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification
# Architecture: MobileNetV2 (google/mobilenet_v2_1.0_224)
# Dataset: PlantVillage / New Plant Diseases Dataset (38 classes, 87K images)
# License: Open Source (Model: Apache-2.0 / Dataset: CC-BY-SA)
# Parameter count: ~3.5M parameters (~9MB weights file)
DEFAULT_MODEL_ID = "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"
FALLBACK_LOCAL_MODEL_DIR = MODELS_DIR / "mobilenet_v2_plant_disease"

# Image Upload Constraints
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE_MB = 15
MAX_IMAGE_DIMENSION = 4096
MIN_IMAGE_DIMENSION = 32

# Confidence Thresholds
CONFIDENCE_HIGH_THRESHOLD = 0.85
CONFIDENCE_MEDIUM_THRESHOLD = 0.60

# Supported Crops (derived from the 38 classes)
SUPPORTED_CROPS = [
    "Apple",
    "Blueberry",
    "Cherry",
    "Corn (Maize)",
    "Grape",
    "Orange",
    "Peach",
    "Bell Pepper",
    "Potato",
    "Raspberry",
    "Soybean",
    "Squash",
    "Strawberry",
    "Tomato",
]

# The 38 canonical classes mapped from PlantVillage dataset
PLANT_DISEASE_CLASSES = [
    "Apple Scab",
    "Apple with Black Rot",
    "Cedar Apple Rust",
    "Healthy Apple",
    "Healthy Blueberry Plant",
    "Cherry with Powdery Mildew",
    "Healthy Cherry Plant",
    "Corn (Maize) with Cercospora and Gray Leaf Spot",
    "Corn (Maize) with Common Rust",
    "Corn (Maize) with Northern Leaf Blight",
    "Healthy Corn (Maize) Plant",
    "Grape with Black Rot",
    "Grape with Esca (Black Measles)",
    "Grape with Isariopsis Leaf Spot",
    "Healthy Grape Plant",
    "Orange with Citrus Greening",
    "Peach with Bacterial Spot",
    "Healthy Peach Plant",
    "Bell Pepper with Bacterial Spot",
    "Healthy Bell Pepper Plant",
    "Potato with Early Blight",
    "Potato with Late Blight",
    "Healthy Potato Plant",
    "Healthy Raspberry Plant",
    "Healthy Soybean Plant",
    "Squash with Powdery Mildew",
    "Strawberry with Leaf Scorch",
    "Healthy Strawberry Plant",
    "Tomato with Bacterial Spot",
    "Tomato with Early Blight",
    "Tomato with Late Blight",
    "Tomato with Leaf Mold",
    "Tomato with Septoria Leaf Spot",
    "Tomato with Spider Mites or Two-spotted Spider Mite",
    "Tomato with Target Spot",
    "Tomato Yellow Leaf Curl Virus",
    "Tomato Mosaic Virus",
    "Healthy Tomato Plant",
]
