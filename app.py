import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Initialize the prediction pipeline
predict_pipeline = PredictPipeline()

# Streamlit app UI
st.title("Sales Prediction App")

# Collect user input using Streamlit widgets
min_age = st.number_input("Minimum Age", min_value=0, max_value=100, value=25)
max_age = st.number_input("Maximum Age", min_value=0, max_value=100, value=35)
gender = st.selectbox("Gender", ["Male", "Female"])
interest = st.slider("Interest Level", min_value=0, max_value=150, value=5)
Impressions = st.number_input("Impressions", min_value=0, value=1000)
Clicks = st.number_input("Clicks", min_value=0, value=50)
Spent = st.number_input("Amount Spent", min_value=0.0, value=20.0)

# Predict button
if st.button("Predict"):
    user_data = CustomData(
        min_age=int(min_age),
        max_age=int(max_age),
        gender=gender,
        interest=int(interest),
        Impressions=int(Impressions),
        Clicks=int(Clicks),
        Spent=float(Spent),
    )
    
    input_df = user_data.get_data_as_data_frame()
    prediction = predict_pipeline.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")