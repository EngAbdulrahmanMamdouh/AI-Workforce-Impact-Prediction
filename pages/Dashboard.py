import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="AI Workforce Dashboard",
    page_icon="📊",
    layout="wide"
)


# =========================
# Load Dataset
# =========================

@st.cache_data
def load_data():
    df = pd.read_csv("ai_job_impact_dataset.csv")
    return df


df = load_data()


# =========================
# Title
# =========================

st.title("📊 AI Workforce Impact Dashboard")


st.write("""
This dashboard analyzes employee characteristics and the possible impact
of Artificial Intelligence on workforce career status.
""")


# =========================
# Dataset Overview
# =========================

st.subheader("📌 Dataset Overview")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Employees",
        f"{df.shape[0]:,}"
    )


with col2:
    st.metric(
        "Features",
        df.shape[1]
    )


with col3:
    st.metric(
        "Target Classes",
        df["employment_status_after_ai"].nunique()
    )


# =========================
# 1- Target Distribution
# =========================

st.subheader("🎯 Employment Status Distribution")


fig, ax = plt.subplots(figsize=(8,5))


sns.countplot(
    data=df,
    x="employment_status_after_ai",
    order=df["employment_status_after_ai"].value_counts().index,
    ax=ax
)


ax.set_xlabel("Employment Status")
ax.set_ylabel("Number of Employees")

plt.xticks(rotation=20)

st.pyplot(fig)



# =========================
# 2- Industry Distribution
# =========================

st.subheader("🏢 Top Industries Distribution")


industry_count = (
    df["industry"]
    .value_counts()
    .head(10)
)


fig, ax = plt.subplots(figsize=(10,5))


sns.barplot(
    x=industry_count.values,
    y=industry_count.index,
    ax=ax
)


ax.set_xlabel("Number of Employees")
ax.set_ylabel("Industry")


st.pyplot(fig)



# =========================
# 3- AI Literacy Score Analysis
# =========================

st.subheader("🤖 AI Literacy Score vs Employment Status")


fig, ax = plt.subplots(figsize=(10,5))


sns.boxplot(
    data=df,
    x="employment_status_after_ai",
    y="ai_literacy_score",
    ax=ax
)


ax.set_xlabel("Employment Status")
ax.set_ylabel("AI Literacy Score")


plt.xticks(rotation=20)

st.pyplot(fig)



# =========================
# 4- Digital Skill Analysis
# =========================

st.subheader("💻 Digital Skill Score vs Employment Status")


fig, ax = plt.subplots(figsize=(10,5))


sns.boxplot(
    data=df,
    x="employment_status_after_ai",
    y="digital_skill_score",
    ax=ax
)


ax.set_xlabel("Employment Status")
ax.set_ylabel("Digital Skill Score")


plt.xticks(rotation=20)

st.pyplot(fig)



# =========================
# 5- Automation Probability
# =========================

st.subheader("⚙️ Automation Probability vs Employment Status")


fig, ax = plt.subplots(figsize=(10,5))


sns.boxplot(
    data=df,
    x="employment_status_after_ai",
    y="automation_probability",
    ax=ax
)


ax.set_xlabel("Employment Status")
ax.set_ylabel("Automation Probability")


plt.xticks(rotation=20)

st.pyplot(fig)



# =========================
# Footer
# =========================

st.success(
    "Dashboard successfully loaded ✅"
)