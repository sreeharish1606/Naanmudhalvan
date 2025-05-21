import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

st.title("Damaged Car Image Preprocessing App")

uploaded_file = st.file_uploader("Choose a damaged car image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    st.image(img, caption="Original Image", channels="BGR")

    st.subheader("Preprocessing Options")
    resized_img = cv2.resize(img, (256, 256))
    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    ret, binary_thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    adaptive_thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    st.image(resized_img, caption="Resized Image", channels="BGR")
    st.image(hsv_img, caption="HSV Image", channels="HSV")
    st.image(binary_thresh, caption="Binary Threshold", channels="GRAY")
    st.image(adaptive_thresh, caption="Adaptive Threshold", channels="GRAY")
