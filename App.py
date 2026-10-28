import streamlit as st
import pickle
import numpy as np
import os

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="AI Hiring Predictor", layout="centered")

st.title("💼 Smart AI Hiring System")
st.write("Machine Learning Based Interview Selection Predictor")

# ==========================s
# LOAD MODEL
# ==========================
BASE_DIR = os.path.dirname(__file__)
model = pickle.load(open(os.path.join(BASE_DIR, "model_rf.pkl"), "rb"))

# ==========================
# INPUT SECTION
# ==========================
st.subheader("👤 Candidate Details")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", 21, 60, 25)
    Gender = st.selectbox("Gender", ["Female", "Male"])
    EducationLevel = st.selectbox("Education", ["UG", "Graduate", "Masters", "PhD"])
    ExperienceYears = st.number_input("Experience Years", 0, 30, 2)

with col2:
    PreviousCompanies = st.number_input("Previous Companies", 0, 10, 1)
    SkillScore = st.slider("Skill Score", 0, 100, 50)
    InterviewScore = st.slider("Interview Score", 0, 100, 50)
    PersonalityScore = st.slider("Personality Score", 0, 100, 50)

# ==========================
# ENCODING
# ==========================
Gender = 1 if Gender == "Male" else 0
EducationLevel = {"UG": 1, "Graduate": 2, "Masters": 3, "PhD": 4}[EducationLevel]

# ==========================
# PREDICTION
# ==========================
st.write("---")

if st.button("🚀 Predict Hiring Decision"):

    input_data = np.array([[
        Age,
        Gender,
        EducationLevel,
        ExperienceYears,
        PreviousCompanies,
        SkillScore,
        InterviewScore,
        PersonalityScore
    ]])

    result = model.predict(input_data)[0]

    st.subheader("📊 Result")

    if result == 1:
        st.success("🎉 SELECTED FOR HIRING")
        st.balloons()
    else:
        st.error("❌ NOT SELECTED")

