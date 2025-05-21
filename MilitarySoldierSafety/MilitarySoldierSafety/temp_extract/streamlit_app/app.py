import streamlit as st
import cv2
import torch
from PIL import Image
import numpy as np

st.title("Soldier Safety & Weapon Detection")

uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])

model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/best.pt')  # Replace with actual model

if uploaded_file is not None:
    if uploaded_file.name.endswith(('jpg', 'jpeg', 'png')):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        results = model(np.array(image))
        results.render()
        st.image(results.ims[0])
    elif uploaded_file.name.endswith("mp4"):
        st.video(uploaded_file)
        st.warning("Video detection is not implemented in this demo.")
