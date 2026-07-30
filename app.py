import streamlit as st


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="AI Workforce Impact Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# Home Page
# =========================

st.title("🤖 AI Workforce Impact Prediction & Career Analytics System")


st.markdown("""
## Welcome 👋

This application uses **Machine Learning** to predict the impact of 
Artificial Intelligence adoption on employee career status.

The system analyzes employee and job-related features to classify the expected career outcome.
""")


# =========================
# Project Objective
# =========================

st.subheader("🎯 Project Objective")


st.write("""
The main objective of this project is to build an intelligent prediction system
that estimates how AI adoption may affect employees' future career status.

The model predicts four possible outcomes:
""")


# =========================
# Prediction Classes
# =========================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.info("""
    ### 👨‍💼 Employed

    Employee is expected to remain employed after AI adoption.
    """)


with col2:
    st.success("""
    ### 📚 Reskilled

    Employee may require or complete new skills training.
    """)


with col3:
    st.warning("""
    ### 🔄 Career Change

    Employee may transition to another career path.
    """)


with col4:
    st.error("""
    ### ⚠️ Unemployed

    Employee may face employment risk.
    """)



# =========================
# Project Information
# =========================

st.subheader("📊 Project Information")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Dataset Size",
        "99,042 Records"
    )


with col2:
    st.metric(
        "Prediction Classes",
        "4 Classes"
    )


with col3:
    st.metric(
        "Best Model",
        "Logistic Regression"
    )



# =========================
# Machine Learning Pipeline
# =========================

st.subheader("⚙️ Machine Learning Pipeline")


st.markdown("""
The system follows a complete Machine Learning workflow:

1. 📥 Data Collection  
2. 🔍 Exploratory Data Analysis (EDA)  
3. 🧹 Data Cleaning & Preprocessing  
4. 🔠 Feature Encoding  
5. ⚖️ Feature Scaling  
6. 🤖 Model Training & Evaluation  
7. 💾 Model Saving  
8. 🌐 Deployment using Streamlit


The deployed application allows users to enter employee information
and receive an AI-based career impact prediction.
""")


# =========================
# Navigation
# =========================

st.subheader("📌 Available Pages")


st.markdown("""
Use the sidebar to navigate through:

- 🤖 **Prediction**  
  Predict employee career status after AI adoption.

- 📊 **Dashboard**  
  Explore dataset insights and visual analytics.

- ℹ️ **About**  
  Learn more about the project and technology stack.
""")


# =========================
# Footer
# =========================

st.divider()

st.caption(
    "AI Workforce Impact Prediction System | Machine Learning Deployment Project"
)