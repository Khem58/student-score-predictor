
import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("📊 Student Exam Score Predictor")

study = st.slider("Study Hours", 1, 10)
sleep = st.slider("Sleep Hours", 4, 10)
attendance = st.slider("Attendance (%)", 50, 100)

if st.button("Predict Score"):
    pred = model.predict([[study, sleep, attendance]])
    st.success(f"Predicted Score: {pred[0]:.2f}")
