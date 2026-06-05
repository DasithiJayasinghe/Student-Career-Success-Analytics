# Student Career Success Analytics and Salary Prediction

## Overview
This project predicts salary packages (LPA) of engineering graduates using academic performance, technical skills, internship experience, project work, and career development indicator.

## Dataset
- 25,000+ student records
- Engineering students from Tier 1, Tier 2, and Tier 3 colleges
- Features include:
       - CGPA
       - Internships
       - GitHub activity
       - DSA problem-solving
       - AI/ML projects
       - Resume score
       - Communication skills
       - Self-learning habits

## Project Workflow
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Deployment Preparation

## Models Evaluated
                          
- Linear Regression	           
R² Score - 0.673	
RMSE - 2.020

- Gradient Boosting          	
R² Score - 0.663	
RMSE - 2.047

- XGBoost	                     
R² Score - 0.659	
RMSE - 2.060

- Extra Trees	
R² Score - 0.644
RMSE - 2.104

- Random Forest	
R² Score - 0.640	
RMSE - 2.116

## Key Findings
- CGPA was the strongest predictor of salary.
- Internship experience significantly influenced salary outcomes.
- AI/ML project experience positively impacted salary predictions.
- Students from higher-tier colleges tended to receive higher salary packages.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost
- Google Colab


## Results
Best model: Random Forest Regressor
Academic performance (CGPA), college tier, internship experience, and AI/ML project exposure were identified as the strongest predictors of salary packages among placed engineering students.
Evaluation Metrics:
- R² Score
- MAE
- RMSE

## Deployment Notes
This project has deployed using streamlit 
- https://student-career-success-analytics-mkkrbbpgxhyd9kbz4nzknn.streamlit.app/
  
## Future Improvements
- Hyperparameter tuning
- Streamlit deployment
- Feature selection optimization
