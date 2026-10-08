# 💼 Job Recommendation System

## 📌 Project Overview

The Job Recommendation System is a Machine Learning based application that recommends suitable job roles based on the skills provided by a user.

The system analyzes the user's skills and predicts suitable job roles using a trained Random Forest classification model.

It also provides a skill gap analysis that shows which skills the user should learn for the recommended roles.

---

## 🎯 Objectives

- Recommend suitable job roles based on user skills.
- Compare multiple Machine Learning classification algorithms.
- Select the best-performing model.
- Calculate skill-match percentages.
- Identify missing skills for recommended roles.
- Provide an interactive web interface.

---

## 🧠 Machine Learning Approach

This project treats job recommendation as a multi-class classification problem.

### Input

The model uses 78 skill features such as:

- Python
- Java
- SQL
- Excel
- Power BI
- Machine Learning
- Deep Learning
- AWS
- Docker
- Kubernetes
- React
- Git
- and many more.

### Output

The model predicts one of 35 job roles.

---

## 🤖 Models Compared

The following classification algorithms were evaluated:

1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)
4. Support Vector Machine (SVM)
5. Gradient Boosting

### Model Performance

| Model | Accuracy |
|---|---:|
| Decision Tree | 67.42% |
| KNN | 92.16% |
| SVM | 93.40% |
| Gradient Boosting | 94.63% |
| Random Forest | **96.01%** |

Random Forest was selected as the final model.

---

## 📊 Dataset

The project uses a generated job-profile dataset containing:

- 7,000 initial candidate profiles
- 6,888 profiles after duplicate removal
- 78 skill features
- 35 job roles

The dataset was cleaned before model training.

---

## 💡 Main Features

### 1. Job Recommendation

Users select their existing skills and receive the top recommended job roles.

### 2. Model Confidence

The Random Forest model provides a confidence score for each predicted role.

### 3. Skill Match

The application calculates how closely the user's skills match the skills associated with each role.

### 4. Skill Gap Analysis

The system identifies important skills that the user is missing for the top recommended role.

---

## 🛠️ Technology Stack

### Programming Language

Python

### Machine Learning

- Scikit-learn
- Random Forest
- Decision Tree
- KNN
- SVM
- Gradient Boosting

### Data Processing

- Pandas
- NumPy

### Web Application

Streamlit

### Development Environment

Visual Studio Code

---

## 📁 Project Structure

```text
Job_Recommendation_System/
│
├── dataset/
│   ├── job_profiles.csv
│   └── job_profiles_cleaned.csv
│
├── app.py
├── create_dataset.py
├── explore_dataset.py
├── clean_dataset.py
├── prepare_data.py
├── train_model.py
├── evaluate_model.py
├── model_comparison.py
├── save_model.py
│
├── random_forest_model.pkl
├── skill_columns.pkl
├── requirements.txt
└── README.md