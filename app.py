import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# SETTINGS — update with your correct values
MODEL_PATH = 'rop_densenet_model.keras'  # or .h5 if you saved in HDF5 format
IMG_SIZE = 224  # Must match your training

# Load model once (cache if rerunning to speed up)
@st.cache_resource  # use st.cache_resource for Streamlit 1.x and later
def load_rop_model():
    return load_model(MODEL_PATH)

model = load_rop_model()

# Prediction function
def predict_rop_stage(model, img):
    img = img.convert('RGB').resize((IMG_SIZE, IMG_SIZE))
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    y_pred = model.predict(arr)
    classes = ["No ROP", "Mild ROP", "Severe ROP"]
    pred_label = np.argmax(y_pred[0])
    probs = np.round(y_pred[0], 3)
    return classes[pred_label], probs

# UI
st.title('ROP Stage Classification (DenseNet)')
st.write('Upload a widefield retinal fundus image to predict the ROP stage.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Fundus Image', use_column_width=True)

    with st.spinner('Analyzing...'):
        stage, probs = predict_rop_stage(model, img)

    st.markdown("### Predicted Stage: **{}**".format(stage))
    st.write("Probabilities: No ROP: {:.2f}, Mild ROP: {:.2f}, Severe ROP: {:.2f}".format(*probs))

    # Tailored clinical messages
    if stage == "No ROP":
        st.success("There is **no Retinopathy of Prematurity (ROP)** present in the eye. There is **no need for treatment**.")
    elif stage == "Mild ROP":
        st.info(
            "Babies in these stages usually get better **without treatment** and go on to have healthy vision. "
            "Doctors will watch babies carefully to see if their ROP gets worse. Some babies who are in this group get better with no treatment, "
            "but others need treatment to stop abnormal blood vessels from damaging the retina and causing retinal detachment (which can cause vision loss).")
    else:
        st.warning(
            "**Severe ROP detected. This stage requires medical attention.** Please consult a retinal specialist promptly for potential treatment to prevent vision loss.")

    st.write("---")

# Footer
st.caption("Clinical AI Demo – DenseNet model for ROP multi-class severity. Not for diagnostic use.")
