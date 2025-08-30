# ---------------- Imports ----------------
import streamlit as st
import pandas as pd
from PIL import Image
import random

# ---------------- Medicine Pool ----------------
medicine_pool = [
    {"Medicine": "Paracetamol", "Dosage": "500mg", "Timing": "Morning & Night"},
    {"Medicine": "Amoxicillin", "Dosage": "250mg", "Timing": "After Food (Twice Daily)"},
    {"Medicine": "Vitamin D3", "Dosage": "1000 IU", "Timing": "Morning"},
    {"Medicine": "Cetirizine", "Dosage": "10mg", "Timing": "Night"},
    {"Medicine": "Metformin", "Dosage": "500mg", "Timing": "Morning & Evening"},
    {"Medicine": "Ibuprofen", "Dosage": "400mg", "Timing": "After Food (Thrice Daily)"},
    {"Medicine": "Azithromycin", "Dosage": "500mg", "Timing": "Morning (Before Food)"},
    {"Medicine": "Calcium", "Dosage": "600mg", "Timing": "Night"},
    {"Medicine": "Pantoprazole", "Dosage": "40mg", "Timing": "Morning (Empty Stomach)"},
    {"Medicine": "Levocetirizine", "Dosage": "5mg", "Timing": "Evening"}
]

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}
.main {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
}
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    width: 100%;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}
.dataframe {
    background: #fafafa;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="AI Prescription Scanner", layout="wide")
st.markdown("<h1 style='text-align: center; color:#0072ff;'>🌈 Prescription Scanner & Medicine Schedule</h1>", unsafe_allow_html=True)

# Initialize session state
if "schedules" not in st.session_state:
    st.session_state.schedules = {}

# File uploader
upload = st.file_uploader("📤 Upload Prescription (Image Only)", type=["png", "jpg", "jpeg"])

if upload:
    img_name = upload.name

    # Generate schedule if new file
    if img_name not in st.session_state.schedules:
        selected_data = random.sample(medicine_pool, 5)
        st.session_state.schedules[img_name] = pd.DataFrame(selected_data)

    # Layout in two columns
    col1, col2 = st.columns([1, 2])

    with col1:
        img = Image.open(upload)
        st.image(img, caption=f"🖼 Uploaded: {img_name}", use_container_width=True)

    with col2:
        st.success("✅ Prescription uploaded successfully.")
        st.markdown("### 💊 Medicine Schedule")
        st.table(st.session_state.schedules[img_name])

# Reset button (center aligned)
st.markdown("<br>", unsafe_allow_html=True)
col_reset = st.columns([3, 1, 3])
with col_reset[1]:
    if st.button("🔄 Reset All"):
        st.session_state.schedules = {}
        st.warning("All uploaded schedules cleared!")
