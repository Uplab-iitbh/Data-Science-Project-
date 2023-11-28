from pyexpat import features
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import pickle

# Function to load the model
@st.cache
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


# Load the pre-trained model
model_path = 'model_sarimax_fit1.pkl' #Give the path of the pickle file
model = load_model(model_path)

# web app
st.title("Credit Card Fraud Detection Model")
input_file=st.file_uploader("Upload the transaction details:",type='csv')
submit = st.button("Submit")

if submit:
    
    if input_file is not None:
        df=pd.read_csv(input_file)       
        prediction = model.predict(df)
  
        for i in range(0,len(df)):
            if prediction[i] == 0:
                st.write(f"{i+1}.This is a Legitimate Transaction !!!")
            else:
                st.write(f"{i+1}.Caution!!! This is a Fradulant Transaction.")