# app.py
import streamlit as st
import pandas as pd
from PIL import Image
from backend import get_file_hash, generate_schedule
from backend import medicine_pool
import os

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Streamlit config
st.set_page_config(page_title="AI Prescription Scanner", layout="wide")
st.markdown("<h1 style='text-align: center; color:#0072ff;'>🌈 Prescription Scanner & Medicine Schedule</h1>", unsafe_allow_html=True)

# Initialize session state
if "schedules" not in st.session_state:
    st.session_state.schedules = {}

# Upload file
upload = st.file_uploader("📤 Upload Prescription (Image Only)", type=["png", "jpg", "jpeg"])

if upload:
    file_hash = get_file_hash(upload)
    upload.seek(0)  # Reset file pointer for image reading

    if file_hash not in st.session_state.schedules:
        st.session_state.schedules[file_hash] = generate_schedule()

    # Layout
    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            img = Image.open(upload)
            st.image(img, caption=f"🖼 Uploaded: {upload.name}", use_container_width=True)
        except Exception as e:
            st.error(f"❌ Could not open the image. Error: {str(e)}")

    with col2:
        st.success("✅ Prescription uploaded successfully.")
        st.markdown("### 💊 Medicine Schedule")
        df = st.session_state.schedules[file_hash]
        st.dataframe(df, use_container_width=True)

        # Download option
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Schedule", csv, file_name="medicine_schedule.csv", mime="text/csv")

# Reset button
st.markdown("<br>", unsafe_allow_html=True)
col_reset = st.columns([3, 1, 3])
with col_reset[1]:
    if st.button("🔄 Reset All"):
        st.session_state.schedules = {}
        st.warning("All uploaded schedules cleared!")
