import streamlit as st
import pandas as pd
import numpy as np
import joblib


# =========================
# Load Files
# =========================

@st.cache_resource
def load_files():

    model = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    feature_columns = joblib.load("feature_columns.pkl")

    return model, scaler, label_encoder, feature_columns


model, scaler, label_encoder, feature_columns = load_files()


# =========================
# Page Title
# =========================

st.title("🤖 AI Impact Career Prediction")

st.write(
    "Enter employee information to predict the expected career status after AI adoption."
)


# =========================
# User Inputs
# =========================

st.subheader("👤 Personal Information")


age = st.number_input(
    "Age",
    min_value=18,
    max_value=70,
    value=30
)


years_experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=5
)


salary_usd = st.number_input(
    "Salary (USD)",
    min_value=1000,
    max_value=200000,
    value=50000
)



st.subheader("🤖 AI Skills")


ai_literacy_score = st.slider(
    "AI Literacy Score",
    0.0,
    100.0,
    50.0
)


digital_skill_score = st.slider(
    "Digital Skill Score",
    0.0,
    100.0,
    50.0
)


automation_probability = st.slider(
    "Automation Probability",
    0.0,
    1.0,
    0.5
)



mental_stress_score = st.slider(
    "Mental Stress Score",
    0.0,
    100.0,
    50.0
)



st.subheader("🏢 Work Information")


country = st.selectbox(
    "Country",
    [
        "Egypt",
        "USA",
        "UK",
        "India",
        "China",
        "Germany",
        "Canada",
        "Australia",
        "Brazil"
    ]
)



industry = st.selectbox(
    "Industry",
    [
        "IT",
        "Education",
        "Healthcare",
        "Government",
        "Finance",
        "Manufacturing",
        "Retail",
        "Energy",
        "Transportation"
    ]
)



reskilling_completed = st.selectbox(
    "Reskilling Completed",
    [
        "Yes",
        "No"
    ]
)



# =========================
# Prediction
# =========================

if st.button("🔮 Predict"):


    input_data = pd.DataFrame(
        {
            "age": [age],
            "years_experience": [years_experience],
            "salary_usd": [salary_usd],
            "ai_literacy_score": [ai_literacy_score],
            "digital_skill_score": [digital_skill_score],
            "automation_probability": [automation_probability],
            "mental_stress_score": [mental_stress_score],
            "country": [country],
            "industry": [industry],
            "reskilling_completed": [reskilling_completed]
        }
    )


    # One Hot Encoding
    input_encoded = pd.get_dummies(input_data)



    # Add missing columns
    for col in feature_columns:

        if col not in input_encoded.columns:
            input_encoded[col] = 0



    # Remove extra columns
    input_encoded = input_encoded[feature_columns]



    # Show encoded data
    st.subheader("Encoded Input")

    st.dataframe(input_encoded)



    # Scaling
    input_scaled = scaler.transform(input_encoded)



    # Probabilities
    probability = model.predict_proba(input_scaled)


    prob_df = pd.DataFrame(
        probability,
        columns=label_encoder.classes_
    )


    st.subheader("Prediction Probabilities")

    st.dataframe(prob_df)



    # Prediction
    prediction = model.predict(input_scaled)



    result = label_encoder.inverse_transform(prediction)[0]


    confidence = np.max(probability) * 100



    st.success(
        f"### Prediction: {result}"
    )


    st.info(
        f"Confidence Score: {confidence:.2f}%"
    )



    if result == "Employed":

        st.write(
            "✅ The model predicts that the employee is likely to remain employed after AI adoption."
        )


    elif result == "Reskilled":

        st.write(
            "📚 The model predicts that the employee may need or complete reskilling."
        )


    elif result == "Career Change":

        st.write(
            "🔄 The model predicts a possible career transition due to AI impact."
        )


    else:

        st.write(
            "⚠️ The model predicts a higher risk of unemployment."
        )