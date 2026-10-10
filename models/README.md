# PlantGuard AI — Local Model Information

## Model Details
- **Model Identifier:** `linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification`
- **Base Architecture:** Google MobileNetV2 (`google/mobilenet_v2_1.0_224`)
- **Weights Format:** PyTorch (`pytorch_model.bin`) / SafeTensors compatible
- **Weights Size:** ~8.9 MB
- **Dataset:** New Plant Diseases Dataset / PlantVillage (54,306+ leaf images across 38 classes)
- **Validation Accuracy:** 95.41%

## License Information
- **Model Weights License:** Open Source (Apache 2.0 / Permissive)
- **Dataset License:** Creative Commons CC-BY-SA 4.0 (Mohanty et al., Penn State & EPFL)
- **Application Code License:** MIT License

## Offline Use & First Run
When you run PlantGuard AI for the first time, Hugging Face Hub automatically caches the 8.9 MB weights into your user cache directory:
- Windows: `C:\Users\<username>\.cache\huggingface\hub\`
- Linux/macOS: `~/.cache/huggingface/hub/`

Once downloaded, the model can run **completely offline without any internet connection or third-party API key**.
To explicitly run offline, you can export the environment variable:
```bash
# Windows PowerShell
$env:HF_HUB_OFFLINE = "1"

# Linux / macOS
export HF_HUB_OFFLINE=1
```
