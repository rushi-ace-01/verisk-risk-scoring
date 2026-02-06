import streamlit as st
import requests

st.title("Explainable Underwriting Risk Scoring")

st.write("Enter policy details to assess underwriting risk.")

policy = {
    "Exposure": st.number_input("Exposure", 0.0, 1.0, 1.0),
    "VehAge": st.number_input("Vehicle Age", 0, 30, 5),
    "DrivAge": st.number_input("Driver Age", 18, 90, 40),
    "BonusMalus": st.number_input("Bonus-Malus", 50, 150, 100),
    "Density": st.number_input("Population Density", 0.0, 50000.0, 1000.0),
    "Area": st.selectbox("Area", ["A", "B", "C", "D", "E", "F"]),
    "VehBrand": st.selectbox("Vehicle Brand", ["B1", "B2", "B3", "B4"]),
    "VehGas": st.selectbox("Fuel Type", ["Regular", "Diesel"]),
    "Region": st.selectbox("Region", ["R1", "R2", "R3", "R4"])
}

if st.button("Score Policy"):
    response = requests.post("http://127.0.0.1:8000/score", json=policy)

    if response.status_code == 200:
        result = response.json()
        st.metric("Risk Score", result["risk_score"])
        st.metric("Claim Probability", result["claim_probability"])
        st.success(f"Decision: {result['decision']}")
    else:
        st.error("API error")

