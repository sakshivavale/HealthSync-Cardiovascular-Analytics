# 🩺 HealthSync – Cardiovascular Risk Analytics Dashboard

> Predictive Analysis of Lifestyle Habits on Cardiovascular Health using Data Analytics, Machine Learning, and Interactive Visualization.

---

## 📌 Project Overview

HealthSync is a Data Analytics and Machine Learning project developed to analyze how lifestyle habits impact cardiovascular health. The project focuses on identifying hidden relationships between behavioral factors such as sleep, exercise, stress, smoking, and diet with heart attack risk.

The system uses Exploratory Data Analysis (EDA), Statistical Analysis, SMOTE-based data balancing, and Random Forest Classification to provide real-time cardiovascular risk assessment through an interactive Streamlit dashboard.

Unlike traditional hospital-based prediction systems, HealthSync emphasizes accessible lifestyle-based analytics rather than relying heavily on clinical test reports.

---

## 🎯 Problem Statement

Cardiovascular diseases (CVDs) are among the leading causes of death globally. Although health tracking devices generate large amounts of daily lifestyle data, users often fail to understand how these habits contribute to long-term heart health risks.

HealthSync bridges this gap by converting raw lifestyle data into meaningful predictive insights using Data Analytics and Machine Learning techniques.

---

## 🚀 Key Features

- 📊 Exploratory Data Analysis (EDA)
- ❤️ Lifestyle-based cardiovascular risk prediction
- 🤖 Random Forest Classification model
- ⚖️ SMOTE for imbalanced dataset handling
- 📈 Interactive Streamlit dashboard
- 🔍 Real-time prediction system
- 📉 Correlation Heatmap Visualization
- 🧠 Feature Isolation methodology
- 📋 Statistical hypothesis testing

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn

### Concepts Used
- Data Analytics
- Machine Learning
- Data Visualization
- Statistical Analysis
- Feature Engineering
- SMOTE Oversampling

---

## 📂 Dataset Information

- Dataset Size: **8,763 Patient Records**
- Total Features: **26 Attributes**

### Important Features Used
- Age
- Cholesterol
- Sleep Hours
- Exercise Hours
- Stress Level
- Smoking Habits
- Diet Type
- Blood Pressure
- Diabetes

---

## ⚙️ Project Workflow

```text
Data Collection
       ↓
Data Cleaning & Preprocessing
       ↓
Exploratory Data Analysis (EDA)
       ↓
Feature Engineering
       ↓
SMOTE Data Balancing
       ↓
Random Forest Model Training
       ↓
Model Evaluation
       ↓
Streamlit Dashboard Deployment
```

---

## 📊 Exploratory Data Analysis (EDA)

The project includes extensive visual and statistical analysis to understand relationships between lifestyle habits and cardiovascular risk.

### EDA Techniques Used
- Correlation Heatmaps
- Histograms
- Boxplots
- Distribution Analysis
- Statistical Hypothesis Testing

### Major Findings
- Individual habits showed very weak linear correlation with heart attack risk.
- Combined lifestyle patterns revealed stronger non-linear relationships.
- Cholesterol, Age, and Exercise Hours were major predictive indicators.

---

## 🤖 Machine Learning Model

### Model Used
- Random Forest Classifier

### Why Random Forest?
- Handles non-linear relationships effectively
- Reduces overfitting
- Performs well on complex healthcare datasets
- Works efficiently with mixed behavioral data

### Special Optimization
The project implements a **Feature Isolation** approach where the model is trained only on user-interactive lifestyle inputs to avoid clinical imputation bias.

---

## ⚖️ Handling Imbalanced Data

Medical datasets often contain fewer high-risk patient records compared to healthy records.

To solve this:
- **SMOTE (Synthetic Minority Over-sampling Technique)** was used
- Generated synthetic balanced data samples
- Improved model learning and prediction reliability

---

## 📈 Dashboard Features

The project is deployed using **Streamlit** and provides:

- Interactive sliders and dropdowns
- Real-time prediction generation
- Correlation heatmap visualization
- Risk percentage calculation
- High-risk alert system
- User-friendly healthcare dashboard

---

## 🧠 Prediction Logic

The model predicts cardiovascular risk based on:
- Sleep duration
- Exercise hours
- Stress levels
- Smoking habits
- Cholesterol
- Diet patterns
- Age

If the predicted risk exceeds **40%**, the system triggers a high-risk alert.

---

## 📷 Dashboard Preview

_Add your dashboard screenshots here_

```bash
/assets/dashboard.png
```

---

## 📁 Project Structure

```bash
HealthSync-Cardiovascular-Analytics/
│
├── app.py
├── Untitled0.ipynb
├── heart_attack_prediction_dataset.csv
├── requirements.txt
├── README.md
└── assets/
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/HealthSync-Cardiovascular-Analytics.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd HealthSync-Cardiovascular-Analytics
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📌 Results

- Improved detection of high-risk cardiovascular patients
- Better recall performance for healthcare analytics
- Successful deployment of real-time prediction dashboard
- Demonstrated importance of combined lifestyle behavior analysis

---

## 🔮 Future Scope

- ⌚ Smartwatch & wearable integration
- 📱 Mobile application development
- 🧠 Explainable AI (SHAP)
- 🤖 Deep Learning models
- 🌐 Real-time IoT health monitoring

---

## 👨‍💻 Team Members

| Name | Role |
|------|------|
| Sujal Salunke | Project Manager |
| Sakshi Vavale | Data Engineer |
| Hrishikesh Mhetre | Data Analyst |
| Gurpreet Singh | Visualization Lead |

---

## 🎓 Institution

Department of Computer Science (AIML)  
G.H. Raisoni International Skill Tech University  
Pune, Maharashtra, India

---

## 📚 References

- Random Forest – Breiman (2001)
- SMOTE Technique – Chawla et al.
- Streamlit Documentation
- Scikit-learn Documentation
- WHO Cardiovascular Reports
- Kaggle Heart Attack Dataset

---

## 📌 GitHub Topics

```txt
data-analytics
machine-learning
healthcare-analytics
streamlit
python
random-forest
eda
smote
heart-disease-prediction
predictive-analysis
data-visualization
```

---

## 📄 License

This project is developed for academic and educational purposes only.

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub.
