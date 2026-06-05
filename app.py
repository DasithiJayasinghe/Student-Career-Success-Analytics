import streamlit as st
import pickle

# Load model
with open('models/salary_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('models/model_features.pkl', 'rb') as file:
    features = pickle.load(file)

st.title("Student Salary Prediction System")

st.success("Model Loaded Successfully")

st.write(
"Predict expected salary package based on student profile."
)

cgpa = st.slider("CGPA", 0.0, 10.0, 7.5)

internships = st.number_input(
"Internships Completed",
min_value=0,
max_value=10,
value=1
)

github_repos = st.number_input(
"GitHub Repositories",
min_value=0,
max_value=100,
value=5
)

st.button("Predict Salary")
