import streamlit as st
import cv2
from ultralytics import YOLO

# ============================================
# PAGE SETTINGS
# ============================================
st.set_page_config(
    page_title="Fruit Freshness Detection",
    layout="wide"
)

st.title("🍎 Fruit Freshness Detection")

st.write("Live Detection Using YOLOv8")

# ============================================
# LOAD MODEL
# ============================================
model = YOLO("runs/detect/train/weights/best.pt")

# ============================================
# SIDEBAR
# ============================================
st.sidebar.title("Settings")

confidence = st.sidebar.slider(
    "Confidence",
    0.1,
    1.0,
    0.40
)

# ============================================
# CAMERA START
# ============================================
run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

# ============================================
# LIVE DETECTION
# ============================================
while run:

    success, frame = camera.read()

    if not success:
        st.error("Camera Not Working")
        break

    # ============================================
    # DETECTION
    # ============================================
    results = model.predict(
        frame,
        conf=confidence
    )

    annotated_frame = results[0].plot()

    # ============================================
    # RGB
    # ============================================
    annotated_frame = cv2.cvtColor(
        annotated_frame,
        cv2.COLOR_BGR2RGB
    )

    FRAME_WINDOW.image(
        annotated_frame,
        channels="RGB"
    )

camera.release()