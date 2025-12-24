import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_model.pkl")

st.title("Salary Prediction App")
age=st.number_input("Age",18.0,100.0,18.0)
years = st.number_input("Years of Experience", 0.0, 40.0, 1.0)
gender = st.selectbox("Gender", ["Male", "Female"])
edu = st.selectbox("Education Level", ["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
job = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Manager", "Analyst"])

input_df = pd.DataFrame([{
    "Age": age,
    "Years of Experience": years,
    "Gender": gender,
    "Education Level": edu,
    "Job Title": job
}])

if st.button("Predict Salary"):
    pred = model.predict(input_df)[0]
    st.success(f"Estimated Salary: ₹{pred:,.2f}")
