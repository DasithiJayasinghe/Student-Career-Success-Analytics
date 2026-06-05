import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and features
with open('models/salary_prediction_model .pkl', 'rb') as file:
    model = pickle.load(file)

with open('models/Salary_prediction_model_features.pkl', 'rb') as file:
    features = pickle.load(file)

st.title("🎓 Student Salary Prediction System")
st.success("Model Loaded Successfully")
st.write("Predict expected salary package based on your student profile.")

# Create form
with st.form("salary_prediction_form"):
    st.subheader("📋 Student Profile Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        cgpa = st.slider("CGPA", 0.0, 10.0, 7.5, step=0.1, 
            help="Cumulative Grade Point Average - Your overall academic performance (0-10 scale)")
        college_tier = st.selectbox("College Tier", [1, 2, 3], index=0,
            help="College ranking category - 1: Top tier, 2: Mid tier, 3: Other tier")
        branch = st.selectbox("Branch", 
            ["Computer Science", "Information Technology", "Electronics", 
             "Mechanical", "Civil"], index=0,
            help="Your engineering branch/specialization")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0,
            help="Your gender identity")
    
    with col2:
        internships = st.number_input("Internships Completed", min_value=0, max_value=10, value=1,
            help="Total number of internships you have completed during your college years")
        github_repos = st.number_input("GitHub Repositories", min_value=0, max_value=100, value=5,
            help="Number of projects/repositories on your GitHub profile")
        ai_ml_projects = st.number_input("AI/ML Projects", min_value=0, max_value=50, value=2,
            help="Number of Artificial Intelligence and Machine Learning projects you have worked on")
    
    submit_button = st.form_submit_button("🚀 Predict Salary")

if submit_button:
    # Create input array with all features
    input_data = np.zeros(len(features))
    
    # Map input values to features
    feature_dict = {
        'cgpa': cgpa,
        'college_tier': college_tier,
        'GitHub_repos': github_repos,
        'AI_ML_projects': ai_ml_projects,
        'internships_completed': internships,
    }
    
    # Add branch features (one-hot encoded)
    for feat in features:
        if feat.startswith('branch_'):
            branch_name = feat.replace('branch_', '')
            if branch == branch_name:
                feature_dict[feat] = 1
    
    # Add gender features (one-hot encoded)
    for feat in features:
        if feat.startswith('gender_'):
            gender_name = feat.replace('gender_', '')
            if gender == gender_name:
                feature_dict[feat] = 1
    
    # Fill input array with feature values
    for i, feat in enumerate(features):
        if feat in feature_dict:
            input_data[i] = feature_dict[feat]
    
    # Make prediction
    prediction = model.predict([input_data])[0]
    
    st.success(f"💰 **Predicted Salary Package: ₹{prediction:.2f} LPA**")
    
    # Display input summary
    with st.expander("📊 Your Input Summary"):
        summary_data = {
            'CGPA': cgpa,
            'College Tier': college_tier,
            'Branch': branch,
            'Gender': gender,
            'Internships': internships,
            'GitHub Repos': github_repos,
            'AI/ML Projects': ai_ml_projects,
        }
        st.json(summary_data)
