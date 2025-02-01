import tensorflow as tf
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np

@st.cache_resource  # Caching the model load to avoid reloading every time
def load_model():
    return tf.keras.models.load_model("traffic_sign_classifier.h5")

# Load the model
loaded_model = load_model()

st.header("Traffic Sign Detection")
st.text('Make sure you have a clear image with all parts clearly visible')

# Upload an image
img_file_buffer = st.file_uploader("Upload an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

# Preprocessing
def preprocess_image(img_file, target_size=(64, 64)):
    img = Image.open(img_file).convert("RGB")  
    img = img.resize(target_size)  
    img_array = np.array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    st.subheader('Original Image')
    st.image(img_array[0], caption="Original Image",  use_container_width=True)  # Display the image 
    return img_array

# Prediction function
def prediction(img_file):
    input_image = preprocess_image(img_file)

    # Prediction
    prediction = loaded_model.predict(input_image)

    predicted_class = tf.argmax(prediction, axis=-1).numpy()[0]

    # Getting Class Name using predicted_class
    sign = pd.read_csv("traffic_sign.csv")
    sign_labels = list(sign['ClassId'].values)
    sign_names = list(sign['Name'].values)
    
    sign_predicted = None
    for i, label in enumerate(sign_labels):
        if label == predicted_class:
            sign_predicted = sign_names[i]
            break

    return sign_predicted

if st.button("Predict"):
    if img_file_buffer is not None:
        sign_prediction = prediction(img_file_buffer)  
        st.subheader(f"Predicted Traffic Sign: {sign_prediction}")  
    else:
        st.error("Please upload an image")