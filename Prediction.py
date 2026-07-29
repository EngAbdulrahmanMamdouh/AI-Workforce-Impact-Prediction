import streamlit as st
import joblib

st.set_page_config(page_title="Prediction", page_icon="🤖")

st.title("🤖 AI Workforce Impact Prediction")

try:
    model = joblib.load("models/best_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    st.success("✅ All model files loaded successfully!")

except Exception as e:
    st.error(f"Error loading files: {e}")
