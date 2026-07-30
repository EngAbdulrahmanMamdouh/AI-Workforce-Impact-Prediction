import streamlit as st


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)


# =========================
# Title
# =========================

st.title("ℹ️ About The Project")


# =========================
# Project Description
# =========================

st.subheader("🤖 AI Workforce Impact Prediction System")


st.write("""
This project is an Artificial Intelligence based system that predicts
the impact of AI adoption on employee career status.

The system analyzes employee and job-related features to classify
the expected future career outcome.
""")


# =========================
# Project Goal
# =========================

st.subheader("🎯 Project Goal")


st.write("""
The main goal is to build a Machine Learning solution that helps
understand how Artificial Intelligence can affect workforce careers
and identify possible outcomes such as employment stability,
reskilling needs, career transition, or unemployment risk.
""")


# =========================
# Dataset Information
# =========================

st.subheader("📊 Dataset Information")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Dataset Size",
        "99,042 Employees"
    )


with col2:
    st.metric(
        "Features",
        "73 Features"
    )


with col3:
    st.metric(
        "Classes",
        "4 Categories"
    )


# =========================
# Machine Learning
# =========================

st.subheader("🧠 Machine Learning Approach")


st.markdown("""
The project follows these steps:

1. Data Collection
2. Data Understanding
3. Exploratory Data Analysis (EDA)
4. Data Cleaning
5. Feature Encoding
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Deployment using Streamlit
""")


# =========================
# Technologies
# =========================

st.subheader("🛠️ Technologies Used")


st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost
- Streamlit
- Joblib
""")


# =========================
# Model Information
# =========================

st.subheader("🏆 Model Information")


st.write("""
The final deployed model is **Logistic Regression**.

The model receives employee information as input and predicts one
of four career outcomes:

- Employed
- Reskilled
- Career Change
- Unemployed
""")


# =========================
# Footer
# =========================

st.divider()

st.caption(
    "AI Workforce Impact Prediction & Career Analytics System"
)