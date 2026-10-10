# 🌿 PlantGuard AI — Open-Source Plant Disease Detector

> **“Healthy Plants Start with Smart Care.”**  
> *Built for the Hacktoberfest Open-Source AI Challenge Week 1: “Touch Grass”.*

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-2d6a4f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework: Gradio](https://img.shields.io/badge/UI-Gradio%206-orange.svg)](https://gradio.app/)
[![Model: MobileNetV2](https://img.shields.io/badge/Model-MobileNetV2%20(Open%20Weights)-green.svg)](https://huggingface.co/linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification)
[![Privacy: 100% Local](https://img.shields.io/badge/Privacy-100%25%20Local%20Inference-brightgreen.svg)](#privacy--offline-operation)
[![Live Demo](https://img.shields.io/badge/Live%20Website-GitHub%20Pages-2ec4b6.svg)](https://lalit-oli-mohan-479.github.io/PlantGuard-AI---Open-Source-Plant-Disease-Detector/)

---

## 🌐 Live Website (GitHub Pages)

Experience the live interactive web demo, Touch Grass checklist, and documentation online:  
👉 **[https://lalit-oli-mohan-479.github.io/PlantGuard-AI---Open-Source-Plant-Disease-Detector/](https://lalit-oli-mohan-479.github.io/PlantGuard-AI---Open-Source-Plant-Disease-Detector/)**

---

## 🌻 Overview

**PlantGuard AI** is an open-source, beginner-friendly web application designed to help gardeners, urban growers, and plant lovers diagnose crop diseases from leaf photographs, receive practical organic care suggestions, and reconnect with their living garden.

Unlike commercial plant apps that charge subscriptions ($30–$60/year) and upload personal photos to proprietary corporate clouds, PlantGuard AI runs **100% locally on your own machine** using genuine open-weight computer vision.

---

## 🌾 Why This Project Fits the "Touch Grass" Challenge

In an era of endless screen time, AI is often used to keep people glued to monitors. **PlantGuard AI flips that script**:
- **Screens as a stepping stone, not a destination:** The AI does not just give a label—it gives a concrete outdoor checklist.
- **Dedicated "Touch Grass Mode":** Encourages gardeners to step outside into natural daylight, perform physical finger tests for soil moisture, inspect leaf undersides for beneficial insects, and observe real plants.
- **Physical Inspection Logger:** Users log in-person observations into their local journal, earning celebration milestones for spending time outdoors with nature.

---

## 📸 Screenshots & Walkthrough

*(Replace these image paths with your captured screenshots upon running the application)*

| 🏠 Home & Overview | 🔬 AI Analysis & Diagnosis |
| :---: | :---: |
| `![PlantGuard AI Home](docs/screenshots/home.png)` | `![PlantGuard AI Analysis](docs/screenshots/analysis.png)` |

| 🌱 Touch Grass Outdoor Mode | 📖 Local Plant Care Journal |
| :---: | :---: |
| `![Touch Grass Mode](docs/screenshots/touch_grass.png)` | `![Plant Care Journal](docs/screenshots/journal.png)` |

---

## ✨ Core Features

1. **🔬 Real Open-Weight AI Disease Detection:**
   - Powered by a fine-tuned MobileNetV2 architecture (`linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification`).
   - Analyzes leaves across **38 classes** (14 distinct crops) with **95.41% validation accuracy**.
   - Displays clear **Model Statistical Confidence** (not diagnostic certainty).
   - Generates top alternative predictions and flags low-confidence images (< 60%).

2. **🩺 Transparent, Practical Plant Care:**
   - Comprehensive care mapping for every supported class.
   - Distinct separation between model output and general cultural advice (soil drainage, canopy airflow, sanitized pruning).
   - Cautious approach: strictly avoids prescribing hazardous synthetic chemicals without laboratory confirmation.

3. **🌱 Touch Grass Mode:**
   - Outdoor action checklist: foliage texture, 2-inch soil moisture finger test, surrounding plant inspection, and 48-hour follow-up scheduling.
   - Interactive milestone button to record completed garden visits.

4. **📖 100% Local SQLite Plant Journal:**
   - Persists plant scan history, timestamps, user notes, and inspection statuses locally in `data/journal.db`.
   - View, search, and delete records anytime.

5. **🛡️ Complete Privacy & Offline Capability:**
   - No external APIs, no analytics, no third-party telemetry.
   - After the initial ~8.9 MB model weight download, works completely without internet access.

---

## 🏛️ Architecture & Project Structure

```
PlantGuard AI — Open-Source Plant Disease Detector/
├── app.py                     # Gradio web interface and UI handlers
├── config.py                  # Global settings, paths, thresholds & class lists
├── requirements.txt           # Python package dependencies
├── pytest.ini                 # Pytest test discovery configuration
├── LICENSE                    # MIT open-source license
├── README.md                  # Comprehensive documentation
├── .gitignore                 # Git ignore rules for caches, db, and weights
├── models/
│   └── README.md              # Model specifications and offline guide
├── src/
│   ├── __init__.py            # Package initializer
│   ├── classifier.py          # MobileNetV2 inference engine & confidence logic
│   ├── image_utils.py         # Image validation, security checks & local storage
│   ├── recommendations.py     # 38-class gardening knowledge base & fallbacks
│   └── journal.py             # SQLite journal database operations
├── data/
│   ├── .gitkeep
│   ├── journal.db             # Local SQLite database (created on first run)
│   └── uploads/               # Local user scans (kept private)
├── samples/                   # Sample leaf photos for testing
│   ├── tomato_healthy.jpg
│   ├── tomato_early_blight.jpg
│   └── apple_scab.jpg
└── tests/
    ├── test_classifier.py      # Classifier inference tests
    ├── test_image_utils.py     # Validation, security & format tests
    ├── test_journal.py         # SQLite CRUD tests
    └── test_recommendations.py # Knowledge base & fallback tests
```

---

## 🔬 Open-Source Model & Licensing Details

| Component | Identifier / Source | License |
| :--- | :--- | :--- |
| **Model Weights** | `linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification` | Apache 2.0 (Open Weights) |
| **Dataset** | PlantVillage / New Plant Diseases Dataset (Mohanty et al.) | CC-BY-SA 4.0 |
| **Application Code** | PlantGuard AI | MIT License |

### Supported Crops (14 species, 38 classes):
- **Fruit & Orchard:** Apple (Scab, Black Rot, Cedar Rust, Healthy), Blueberry (Healthy), Cherry (Powdery Mildew, Healthy), Grape (Black Rot, Esca, Leaf Spot, Healthy), Orange (Citrus Greening), Peach (Bacterial Spot, Healthy), Raspberry (Healthy), Strawberry (Leaf Scorch, Healthy)
- **Vegetable & Field:** Bell Pepper (Bacterial Spot, Healthy), Potato (Early Blight, Late Blight, Healthy), Tomato (Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria, Spider Mites, Target Spot, Mosaic Virus, Yellow Leaf Curl, Healthy), Corn/Maize (Cercospora, Common Rust, Northern Blight, Healthy), Soybean (Healthy), Squash (Powdery Mildew)

---

## 🚀 Quickstart & Installation

### 1. Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13
- Git

### 2. Clone Repository & Setup
```bash
git clone https://github.com/your-username/plantguard-ai.git
cd plantguard-ai
```

*(Optional but recommended) Create and activate a virtual environment:*
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open your browser to: **`http://127.0.0.1:7860`**

---

## 🧪 Running Automated Tests

Run the full automated test suite (22 unit tests):
```bash
pytest -v
```

All tests run locally using clean isolated fixtures and test doubles.

---

## 🔒 Privacy & Offline Operation

- **Zero Cloud API Keys Required:** No OpenAI, Anthropic, or Hugging Face token is needed to run inference.
- **Completely Offline:** Once the ~8.9 MB model weights are cached on first run, you can disconnect your computer from the internet entirely:
  ```bash
  # Windows PowerShell
  $env:HF_HUB_OFFLINE = "1"
  python app.py
  ```
- **Local Storage:** Uploaded photos are stored strictly in `data/uploads/` on your hard drive and are ignored by `.gitignore`.

---

## ⚠️ Known Limitations & Responsible AI Disclosure

1. **Statistical Screening vs. Lab Diagnosis:** Visual symptoms of fungal and bacterial infections can resemble physiological stresses (sun scorch, overwatering, root rot, salt accumulation). Always verify in person.
2. **Species Boundary:** The classifier is trained specifically on the 14 agricultural crops listed above. House plants (e.g. Monstera, Ficus) will map to the closest visual pattern, which triggers the application's built-in **Low Confidence Advisory**.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request.
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push to branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
