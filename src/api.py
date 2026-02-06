from fastapi import FastAPI
import joblib
import pandas as pd
import shap
import numpy as np

app = FastAPI(title="Underwriting Risk Scoring API")

# Load model
model = joblib.load("models/gb_model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score")
def score_policy(policy: dict):
    df = pd.DataFrame([policy])

    prob = model.predict_proba(df)[0, 1]
    risk_score = round(prob * 100)

    if risk_score < 35:
        decision = "Accept"
    elif risk_score < 70:
        decision = "Review"
    else:
        decision = "Decline"

    return {
        "claim_probability": round(prob, 4),
        "risk_score": risk_score,
        "decision": decision
    }
