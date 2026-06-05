import streamlit as st

st.title("Student Salary Prediction System")

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
