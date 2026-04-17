import pickle
import streamlit as st
import numpy as np
model=pickle.load(open("fraud_model.pkl","rb"))
st.title("Credit Card Fraud Detection")
st.write("Enter Transaction Details")
time=st.number_input("Transaction Time",min_value=0.0)
amount=st.number_input("Transaction amount",min_value=0.0)
if st.button("Predict"):
  input_data=[time,amount]+[0]*28
  input_data=np.array(input_data).reshape(1,-1)
  prediction=model.predict(input_data)
  if prediction[0]==1:
    st.error("Fraudulent Transaction") 
  else:
    st.success("Non-Fraudulent Transaction")