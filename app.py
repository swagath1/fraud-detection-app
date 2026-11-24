
import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open("fraud_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Credit Card Fraud Detection")
st.write("Enter Transaction Details")

time = st.number_input("Transaction Time", min_value=0.0)
amount = st.number_input("Transaction Amount", min_value=0.0)

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[time] + [0.0]*28 + [amount]],
        columns=["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
    )

    input_data[["Time", "Amount"]] = scaler.transform(
        input_data[["Time", "Amount"]]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraudulent Transaction")
    else:
        st.success("Non-Fraudulent Transaction")
