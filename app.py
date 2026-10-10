"""
PlantGuard AI - Open-Source Plant Disease Detector & Care Companion
Built for Hacktoberfest Open-Source AI Challenge Week 1: 'Touch Grass'
"""

import os
from pathlib import Path
from typing import Tuple, List, Dict, Any, Optional
import gradio as gr
from PIL import Image

from config import (
    APP_TITLE,
    APP_SUBTITLE,
    APP_TAGLINE,
    APP_VERSION,
    SUPPORTED_CROPS,
    PLANT_DISEASE_CLASSES,
)
from src.classifier import PlantClassifier
from src.image_utils import (
    validate_and_load_image,
    save_image_locally,
    ImageValidationError,
)
from src import journal
from src.recommendations import get_recommendation

# Initialize local classifier singleton
classifier = PlantClassifier()

# Custom CSS for rich gardening aesthetics
CUSTOM_CSS = """
/* PlantGuard AI Custom Styling */
:root {
    --primary-green: #2d6a4f;
    --dark-green: #1b4332;
    --light-green: #52b788;
    --pale-green: #d8f3dc;
    --mint-bg: #f8faf8;
    --card-bg: #ffffff;
    --text-dark: #1b262c;
    --accent-gold: #d4a373;
}

body, .gradio-container {
    background-color: var(--mint-bg) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}

.hero-banner {
    background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 100%);
    color: white !important;
    padding: 2.2rem 2.5rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px -5px rgba(27, 67, 50, 0.25);
}

.hero-title {
    font-size: 2.3rem;
    font-weight: 800;
    margin: 0;
    color: #ffffff !important;
    letter-spacing: -0.5px;
}

.hero-tagline {
    font-size: 1.15rem;
    color: #b7e4c7 !important;
    margin-top: 0.4rem;
    margin-bottom: 0.8rem;
    font-weight: 500;
}

.hero-desc {
    color: #e8f5e9 !important;
    max-width: 720px;
    font-size: 0.95rem;
    line-height: 1.5;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.2rem;
    margin: 1.5rem 0;
}

.feature-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.4rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(45, 106, 79, 0.08);
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 0.6rem;
}

.feature-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--dark-green);
    margin-bottom: 0.4rem;
}

.feature-text {
    font-size: 0.88rem;
    color: #4a5568;
    line-height: 1.45;
}

.prediction-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.4rem;
    border: 1px solid #b7e4c7;
    box-shadow: 0 4px 15px rgba(45, 106, 79, 0.05);
}

.confidence-badge {
    display: inline-block;
    padding: 0.35rem 0.8rem;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
}

.badge-high {
    background: #d8f3dc;
    color: #1b4332;
    border: 1px solid #74c69d;
}

.badge-moderate {
    background: #fefae0;
    color: #b07d1a;
    border: 1px solid #e9d8a6;
}

.badge-low {
    background: #ffe5d9;
    color: #9d0208;
    border: 1px solid #f4a261;
}

.warning-box {
    background: #fff3cd;
    border-left: 5px solid #ffc107;
    color: #856404;
    padding: 0.9rem 1.2rem;
    border-radius: 8px;
    margin: 0.8rem 0;
    font-size: 0.9rem;
}

.touch-grass-card {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border: 2px solid #81c784;
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.disclaimer-box {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-size: 0.82rem;
    color: #64748b;
    margin-top: 1rem;
}
"""


def analyze_plant_image(
    image_input, plant_name_input: str, user_notes_input: str
) -> Tuple[str, str, str, str, str, str, str]:
    """
    Handles image analysis workflow:
    1. Validation & local saving
    2. Model inference via MobileNetV2
    3. Output formatting and care guidance
    """
    if image_input is None:
        return (
            "<div class='warning-box'>⚠️ <b>No image uploaded.</b> Please select or upload a leaf photo to analyze.</div>",
            "",
            "",
            "",
            "",
            "",
            "None",
        )

    try:
        # Validate image
        validated_img, original_path = validate_and_load_image(image_input)

        # Run local classifier inference
        prediction_result = classifier.predict(validated_img)

        # Save local copy for journal tracking
        saved_local_path = save_image_locally(validated_img, prefix="leaf_scan")

        top = prediction_result["top_prediction"]
        label = top["label"]
        confidence = top["confidence"]
        percentage = top["percentage"]
        conf_level = top["confidence_level"]
        crop = top["crop"]
        category = top["category"]
        rec = prediction_result["recommendation"]

        # 1. Main Diagnosis Header HTML
        badge_class = (
            "badge-high"
            if conf_level == "High Confidence"
            else "badge-moderate" if conf_level == "Moderate Confidence" else "badge-low"
        )
        status_emoji = "🌿" if "Healthy" in label else "🔍"

        diagnosis_html = f"""
        <div class="prediction-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <h2 style="margin:0; color:#1b4332; font-size:1.6rem;">{status_emoji} {label}</h2>
                <span class="confidence-badge {badge_class}">{conf_level}</span>
            </div>
            <div style="margin-top:0.8rem; display:flex; gap:1.5rem; flex-wrap:wrap; font-size:0.95rem;">
                <div><b>Target Crop:</b> {crop}</div>
                <div><b>Condition Type:</b> {category}</div>
                <div><b>Model Statistical Confidence:</b> <span style="font-weight:700; color:#2d6a4f;">{percentage}</span></div>
                <div><b>Inference Latency:</b> {prediction_result['inference_time_ms']} ms (Local CPU)</div>
            </div>
        </div>
        """

        # 2. Confidence Warning (if applicable)
        warning_html = ""
        if prediction_result["confidence_warning"]:
            warning_html = f"""
            <div class="warning-box">
                ⚠️ <b>Confidence Advisory:</b> {prediction_result['confidence_warning']}
            </div>
            """

        # 3. Alternative Predictions Markdown
        alt_md = "### 📊 Top Alternative Model Predictions\n\n"
        alt_md += "| Rank | Predicted Condition | Statistical Confidence |\n"
        alt_md += "| :--- | :--- | :--- |\n"
        for i, alt in enumerate(prediction_result["all_top_k"], start=1):
            marker = "👈 *(Selected)*" if i == 1 else ""
            alt_md += f"| #{i} | **{alt['label']}** | `{alt['percentage']}` {marker} |\n"

        # 4. Plant Care Recommendations Markdown
        care_md = f"### 🩺 Plant Care & Guidance for: *{label}*\n\n"
        care_md += f"**Observed Symptoms Profile:**\n{rec['symptoms']}\n\n"

        care_md += "**Immediate Practical Actions:**\n"
        for action in rec["immediate_actions"]:
            care_md += f"- 🪴 {action}\n"

        care_md += "\n**Preventative & Cultural Care:**\n"
        for prev in rec["preventative_care"]:
            care_md += f"- 💧 {prev}\n"

        care_md += (
            "\n> 💡 **Gardener's Rule:** General cultural advice is distinct from model output. "
            "Never apply aggressive synthetic chemicals without corroborating symptoms with local agricultural experts."
        )

        # 5. Touch Grass Checklist Markdown
        touch_grass_md = f"### 🌱 Touch Grass Outdoor Action Checklist\n\n"
        touch_grass_md += (
            "*Step outside into the sunlight and inspect your living plant in person!*\n\n"
        )
        for task in rec["outdoor_tasks"]:
            touch_grass_md += f"- [ ] **Outdoor Task:** {task}\n"
        touch_grass_md += "- [ ] **Soil Check:** Insert finger 2 inches into soil to verify moisture level.\n"
        touch_grass_md += "- [ ] **Follow-Up:** Schedule a calendar check 48-72 hours from now to note changes.\n"

        # 6. Auto-log entry to journal
        effective_plant_name = plant_name_input.strip() or crop
        entry_id = journal.add_journal_entry(
            predicted_class=label,
            confidence=confidence,
            plant_name=effective_plant_name,
            image_path=str(saved_local_path),
            notes=user_notes_input.strip(),
            status="Pending Outdoor Check",
        )

        log_status_msg = f"✅ Saved to local journal as Entry #{entry_id} (Plant: '{effective_plant_name}')"

        return (
            diagnosis_html,
            warning_html,
            alt_md,
            care_md,
            touch_grass_md,
            log_status_msg,
            str(entry_id),
        )

    except ImageValidationError as e:
        error_html = f"<div class='warning-box'>⚠️ <b>Image Validation Error:</b> {str(e)}</div>"
        return error_html, "", "", "", "", "Analysis halted due to invalid input.", "None"
    except Exception as e:
        error_html = f"<div class='warning-box'>❌ <b>Unexpected Inference Error:</b> {str(e)}</div>"
        return error_html, "", "", "", "", "Inference failed.", "None"


def mark_outdoor_inspection_done(entry_id_str: str) -> str:
    """Updates journal entry with outdoor inspection completion."""
    if not entry_id_str or entry_id_str == "None":
        return "⚠️ No active plant analysis selected. Please analyze a plant first!"

    try:
        eid = int(entry_id_str)
        success = journal.update_journal_entry_status(
            entry_id=eid,
            new_status="Grass Touched: Inspected Outdoors",
            notes_append="[Outdoor Inspection Completed]: Plant checked in real garden setting.",
        )
        if success:
            return "🎉 Grass Touched! Your outdoor inspection has been recorded in your local journal."
        return "Could not find journal entry to update."
    except Exception as e:
        return f"Error updating status: {str(e)}"


def load_journal_table() -> List[List[Any]]:
    """Fetches formatted records from SQLite journal."""
    entries = journal.get_all_journal_entries()
    rows = []
    for e in entries:
        rows.append(
            [
                e["id"],
                e["timestamp"],
                e["plant_name"] or "Unnamed",
                e["predicted_class"],
                f"{e['confidence'] * 100:.1f}%",
                e["status"],
                e["notes"] or "",
            ]
        )
    return rows


def delete_selected_journal_entry(entry_id_input: str) -> Tuple[str, List[List[Any]]]:
    """Deletes record by ID and refreshes view."""
    if not entry_id_input or not entry_id_input.strip().isdigit():
        return "⚠️ Please enter a valid numerical Entry ID to delete.", load_journal_table()

    eid = int(entry_id_input.strip())
    success = journal.delete_journal_entry(eid)
    if success:
        return f"🗑️ Entry #{eid} deleted successfully.", load_journal_table()
    return f"Entry #{eid} was not found.", load_journal_table()


# Build Gradio Interface
def create_app() -> gr.Blocks:
    # Ensure database is ready
    journal.init_db()

    with gr.Blocks(
        title=f"{APP_TITLE} — {APP_SUBTITLE}",
    ) as demo:

        # Header Hero Banner
        with gr.Row():
            gr.HTML(
                f"""
                <div class="hero-banner">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-size:2.8rem;">🌿</span>
                        <div>
                            <h1 class="hero-title">{APP_TITLE}</h1>
                            <div class="hero-tagline">{APP_TAGLINE}</div>
                        </div>
                    </div>
                    <div class="hero-desc">
                        An open-source, 100% locally runnable plant disease screening tool built for the 
                        <b>Hacktoberfest Open-Source AI Challenge Week 1: “Touch Grass”</b>. 
                        Screen leaf symptoms, receive transparent organic care steps, and get out into your real garden!
                    </div>
                </div>
                """
            )

        # Tab Navigation
        with gr.Tabs() as tabs:

            # ================= TAB 1: HOME =================
            with gr.Tab("🏡 Home & Overview", id="tab_home"):
                gr.HTML(
                    """
                    <div class="feature-grid">
                        <div class="feature-card">
                            <div class="feature-icon">🔬</div>
                            <div class="feature-title">Open-Source AI Vision</div>
                            <div class="feature-text">
                                Powered by a lightweight MobileNetV2 architecture trained on the open PlantVillage dataset.
                                Covers 38 classes across 14 crops with 95.4% benchmark accuracy.
                            </div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">🛡️</div>
                            <div class="feature-title">100% Local & Private</div>
                            <div class="feature-text">
                                Inference runs strictly on your machine's CPU/GPU. No images are sent to any cloud server or proprietary API.
                                Zero telemetry, zero cost.
                            </div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">🩺</div>
                            <div class="feature-title">Practical Care Steps</div>
                            <div class="feature-text">
                                Transparent gardening guidance mapped to disease symptoms. Emphasizes organic, cultural, and preventive care
                                while warning against premature chemical use.
                            </div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">🌱</div>
                            <div class="feature-title">Touch Grass Mode</div>
                            <div class="feature-text">
                                Built for the challenge theme! Prompts you with an actionable outdoor checklist to inspect your living plants,
                                feel the soil, and enjoy nature.
                            </div>
                        </div>
                    </div>
                    """
                )

                with gr.Row():
                    with gr.Column(scale=2):
                        gr.Markdown(
                            """
                            ### 📸 How to Take a Good Leaf Photo
                            1. **Natural, Indirect Light:** Photograph outdoors or near a bright window without harsh flash glare.
                            2. **Single Leaf in Focus:** Keep one representative leaf centered and flat in the frame.
                            3. **Plain Background:** Place a neutral card, paper, or hand behind the leaf if the garden backdrop is cluttered.
                            4. **Both Sides Matter:** Check the underside for fungal mold, rust pustules, or mite webbing.
                            """
                        )
                    with gr.Column(scale=1):
                        gr.Markdown(
                            f"""
                            ### 🌾 Supported Crops ({len(SUPPORTED_CROPS)})
                            - **Fruits:** Apple, Cherry, Grape, Orange, Peach, Strawberry, Raspberry, Blueberry
                            - **Vegetables:** Bell Pepper, Potato, Tomato, Squash
                            - **Field Crops:** Corn (Maize), Soybean
                            """
                        )

            # ================= TAB 2: ANALYZE PLANT =================
            with gr.Tab("🔬 Analyze Plant", id="tab_analyze"):
                current_entry_id = gr.State(value="None")

                with gr.Row():
                    # Left column: Input controls
                    with gr.Column(scale=1):
                        gr.Markdown("### 1. Upload Leaf Photo")
                        image_input = gr.Image(
                            type="pil",
                            label="Leaf Photo (JPG, JPEG, PNG)",
                            sources=["upload", "clipboard"],
                        )

                        with gr.Row():
                            plant_name_input = gr.Textbox(
                                label="Plant / Crop Name (Optional)",
                                placeholder="e.g., Heirloom Tomato, Honeycrisp Apple",
                            )
                        user_notes_input = gr.Textbox(
                            label="Your Notes / Observations",
                            placeholder="e.g., Yellowing started near the base; rainy weather for 3 days.",
                            lines=2,
                        )

                        with gr.Row():
                            analyze_btn = gr.Button(
                                "🔬 Analyze Plant", variant="primary", scale=2
                            )
                            clear_btn = gr.Button("🔄 Clear", variant="secondary", scale=1)

                        # Sample quick-test images
                        gr.Markdown("#### 🧪 Or Try Sample Leaves:")
                        sample_paths = [
                            ["samples/tomato_healthy.jpg", "Healthy Tomato", "Test healthy leaf baseline"],
                            ["samples/tomato_early_blight.jpg", "Tomato Early Blight", "Fungal target spot test"],
                            ["samples/apple_scab.jpg", "Apple Scab", "Fungal apple scab test"],
                        ]
                        gr.Examples(
                            examples=sample_paths,
                            inputs=[image_input, plant_name_input, user_notes_input],
                            label="Click a sample to load into analyzer",
                        )

                    # Right column: Output controls
                    with gr.Column(scale=1):
                        gr.Markdown("### 2. Diagnosis & Statistical Analysis")
                        diagnosis_output = gr.HTML(
                            label="Diagnosis",
                            value="<div style='color:#666; padding:1.5rem; background:#fff; border-radius:12px; border:1px dashed #ccc; text-align:center;'>Upload an image and click <b>Analyze Plant</b> to view results.</div>",
                        )
                        warning_output = gr.HTML()
                        alt_predictions_output = gr.Markdown()

                gr.Markdown("---")

                # Care Recommendations & Touch Grass Checklist
                with gr.Row():
                    with gr.Column(scale=1):
                        care_output = gr.Markdown("### 🩺 Care Recommendations\n*Recommendations will appear here after analysis.*")
                    with gr.Column(scale=1):
                        touch_grass_output = gr.Markdown("### 🌱 Touch Grass Outdoor Action Checklist\n*Outdoor tasks will appear here after analysis.*")
                        with gr.Row():
                            touch_grass_btn = gr.Button(
                                "🌿 Mark Outdoor Inspection Complete",
                                variant="primary",
                            )
                        touch_grass_status = gr.Markdown()

                # Disclaimer
                gr.HTML(
                    """
                    <div class="disclaimer-box">
                        <b>⚠️ Responsible AI & Gardening Disclaimer:</b> 
                        PlantGuard AI uses computer vision pattern screening. It is not an agricultural laboratory diagnosis. 
                        Nutrient imbalances, root rot, sunburn, and pesticide phytotoxicity can produce symptoms mimicking biological pathogens. 
                        Always verify findings physically and consult your local university extension office before undertaking drastic interventions.
                    </div>
                    """
                )

                # Wiring analysis actions
                analyze_btn.click(
                    fn=analyze_plant_image,
                    inputs=[image_input, plant_name_input, user_notes_input],
                    outputs=[
                        diagnosis_output,
                        warning_output,
                        alt_predictions_output,
                        care_output,
                        touch_grass_output,
                        touch_grass_status,
                        current_entry_id,
                    ],
                )

                touch_grass_btn.click(
                    fn=mark_outdoor_inspection_done,
                    inputs=[current_entry_id],
                    outputs=[touch_grass_status],
                )

                clear_btn.click(
                    fn=lambda: (
                        None,
                        "",
                        "",
                        "<div style='color:#666; padding:1.5rem; background:#fff; border-radius:12px; border:1px dashed #ccc; text-align:center;'>Upload an image and click <b>Analyze Plant</b> to view results.</div>",
                        "",
                        "",
                        "### 🩺 Care Recommendations\n*Recommendations will appear here after analysis.*",
                        "### 🌱 Touch Grass Outdoor Action Checklist\n*Outdoor tasks will appear here after analysis.*",
                        "",
                        "None",
                    ),
                    inputs=[],
                    outputs=[
                        image_input,
                        plant_name_input,
                        user_notes_input,
                        diagnosis_output,
                        warning_output,
                        alt_predictions_output,
                        care_output,
                        touch_grass_output,
                        touch_grass_status,
                        current_entry_id,
                    ],
                )

            # ================= TAB 3: TOUCH GRASS MODE =================
            with gr.Tab("🌱 Touch Grass Mode", id="tab_touch_grass"):
                gr.HTML(
                    """
                    <div class="touch-grass-card">
                        <div style="font-size:2rem; margin-bottom:0.4rem;">🌻 Touch Grass: Connect with Living Nature</div>
                        <p style="font-size:1.05rem; color:#1b4332; margin:0; line-height:1.5;">
                            Technology should enhance our connection to the physical world, not trap us in screens.
                            The <b>Touch Grass</b> philosophy reminds us that real plant health begins in the soil, the sun, and our tactile attention.
                        </p>
                    </div>
                    """
                )

                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown(
                            """
                            ### 👣 Outdoor Gardening Routine
                            1. **Step away from the monitor:** Put your phone or laptop down and take a deep breath outside.
                            2. **Touch the foliage:** Feel the thickness and texture of leaves. Are they crisp, leathery, or limp?
                            3. **The 2-Inch Soil Finger Test:**
                               - Push your index finger two inches into the potting soil or garden bed.
                               - If dry and warm: the plant needs deep watering.
                               - If cool and spongy: moisture is optimal.
                               - If muddy and saturated: hold off watering to avoid root rot.
                            4. **Observe the Ecosystem:**
                               - Look for beneficial insects (ladybugs, bees, lacewings).
                               - Check if neighboring companion plants are thriving.
                            """
                        )
                    with gr.Column(scale=1):
                        gr.Markdown(
                            """
                            ### 📋 Quick Outdoor Inspection Log
                            Take a moment to record your outdoor inspection notes directly into your local database:
                            """
                        )
                        outdoor_crop_input = gr.Textbox(
                            label="Plant Inspected", placeholder="e.g., Garden Tomato"
                        )
                        outdoor_note_input = gr.Textbox(
                            label="Physical Garden Observations",
                            placeholder="e.g., Soil was dry; watered roots. Found ladybug on upper branch.",
                            lines=3,
                        )
                        log_outdoor_btn = gr.Button("🌿 Log Outdoor Session", variant="primary")
                        outdoor_status_msg = gr.Markdown()

                        def quick_outdoor_log(plant: str, note: str) -> str:
                            if not plant.strip():
                                return "⚠️ Please specify a plant name."
                            eid = journal.add_journal_entry(
                                predicted_class="Manual Outdoor Garden Inspection",
                                confidence=1.0,
                                plant_name=plant.strip(),
                                notes=note.strip(),
                                status="Grass Touched: Manual Check Done",
                            )
                            return f"🎉 Outdoor session saved to Journal as Entry #{eid}! Great job tending to your living garden."

                        log_outdoor_btn.click(
                            fn=quick_outdoor_log,
                            inputs=[outdoor_crop_input, outdoor_note_input],
                            outputs=[outdoor_status_msg],
                        )

            # ================= TAB 4: PLANT JOURNAL =================
            with gr.Tab("📖 Plant Care Journal", id="tab_journal"):
                gr.Markdown(
                    """
                    ### 📓 Local Plant Health History
                    All inspection records, confidence scores, and notes are saved strictly in your local SQLite database (`data/journal.db`).
                    No personal photos or data ever leave your machine.
                    """
                )

                with gr.Row():
                    refresh_journal_btn = gr.Button("🔄 Refresh Journal Records", variant="secondary")

                journal_dataframe = gr.Dataframe(
                    headers=["ID", "Timestamp", "Plant Name", "Condition", "Confidence", "Status", "Notes"],
                    datatype=["number", "str", "str", "str", "str", "str", "str"],
                    value=load_journal_table,
                    interactive=False,
                    label="Local Health Records",
                )

                with gr.Row():
                    with gr.Column(scale=1):
                        delete_id_input = gr.Textbox(
                            label="Entry ID to Delete", placeholder="e.g. 1"
                        )
                        delete_btn = gr.Button("🗑️ Delete Selected Entry", variant="stop")
                        delete_status = gr.Markdown()

                delete_btn.click(
                    fn=delete_selected_journal_entry,
                    inputs=[delete_id_input],
                    outputs=[delete_status, journal_dataframe],
                )

                refresh_journal_btn.click(
                    fn=load_journal_table,
                    inputs=[],
                    outputs=[journal_dataframe],
                )

            # ================= TAB 5: OPEN-SOURCE AI & MODEL CARD =================
            with gr.Tab("ℹ️ Open-Source AI & Model Card", id="tab_model"):
                info = classifier.get_model_info()
                gr.Markdown(
                    f"""
                    ## 🔬 Open-Source Model Card & Specifications

                    ### 1. Model Architecture & Origin
                    - **Model ID:** `{info['model_id']}`
                    - **Base Architecture:** `{info['architecture']}`
                    - **Weights Size:** `{info['weights_size']}` (Ultra-compact, low RAM overhead)
                    - **Hardware Requirements:** CPU-friendly, requires < 250MB RAM for inference
                    - **Training Dataset:** `{info['dataset']}` (54,000+ benchmarked leaf images)
                    - **Benchmark Validation Accuracy:** `95.41%`

                    ---

                    ### 2. Licensing & Open Governance
                    - **Model Weights License:** `{info['model_license']}` (Open Source, permissive use)
                    - **Dataset License:** `{info['dataset_license']}` (Open Access with attribution)
                    - **Project Application License:** `MIT License`
                    
                    > **Why Open Innovation Matters:**
                    > Many commercial plant apps require paid subscriptions ($30-$60/yr) and upload every garden photo 
                    > to remote corporate cloud servers. PlantGuard AI demonstrates that open-weights AI can run 
                    > **100% locally, free of charge, with complete personal privacy**, empowering gardeners and researchers everywhere.

                    ---

                    ### 3. Supported Classes ({info['classes_count']} Categories)
                    """
                )

                with gr.Row():
                    with gr.Column():
                        gr.Markdown("#### 🍎 Fruit & Orchard Classes\n" + "\n".join([f"- {c}" for c in PLANT_DISEASE_CLASSES if any(fruit in c for fruit in ['Apple', 'Cherry', 'Grape', 'Orange', 'Peach', 'Strawberry', 'Raspberry', 'Blueberry'])]))
                    with gr.Column():
                        gr.Markdown("#### 🍅 Vegetable & Field Classes\n" + "\n".join([f"- {c}" for c in PLANT_DISEASE_CLASSES if any(veg in c for veg in ['Tomato', 'Potato', 'Pepper', 'Corn', 'Soybean', 'Squash'])]))

                gr.Markdown(
                    """
                    ---
                    ### 4. Known Model Limitations
                    - **Species Boundary:** The model is trained on 14 specific crop types. Non-crop indoor house plants (like Monstera or Pothos) will be mapped to the closest visual pattern, which triggers the **Low Confidence Warning**.
                    - **Environmental Confounders:** Extreme heat stress, nutrient burns, or severe drought can visually mimic fungal or bacterial blights.
                    - **Lighting Sensitivity:** Direct sunlight glare or blurry images lower statistical confidence.
                    """
                )

    return demo


if __name__ == "__main__":
    demo = create_app()
    soft_theme = gr.themes.Soft(
        primary_hue=gr.themes.colors.emerald,
        secondary_hue=gr.themes.colors.green,
        neutral_hue=gr.themes.colors.slate,
    )
    # Launch on localhost
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        theme=soft_theme,
        css=CUSTOM_CSS,
        share=False,
    )
