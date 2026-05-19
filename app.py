import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# --- 1. Dashboard Settings ---
st.set_page_config(page_title="HealthSync Dashboard", layout="wide")
st.title("🫀 HealthSync: Lifestyle & Heart Health")
st.markdown("Predictive Analysis of Lifestyle Habits on Cardiovascular Health.")

# --- 2. Load and Prep Data (Cached for speed) ---
@st.cache_data
def load_data():
    df = pd.read_csv('heart_attack_prediction_dataset.csv')
    cols_to_drop = ['Patient ID', 'Country', 'Continent', 'Hemisphere']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    if 'Blood Pressure' in df.columns:
        df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(float)
        df = df.drop(columns=['Blood Pressure'])
    categorical_cols = df.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df, df_encoded

df_raw, df_encoded = load_data()

# --- 3. Train the AI Model (LIFESTYLE FEATURES ONLY) ---
@st.cache_resource
def train_model(data):
    # We ONLY train on the exact columns the user will interact with
    features_to_use = ['Age', 'Sleep Hours Per Day', 'Exercise Hours Per Week', 
                       'Stress Level', 'Cholesterol', 'Smoking', 'Diet_Healthy', 'Diet_Unhealthy']
    
    # Ensure the 'Smoking' column exists (handling original dataset naming)
    if 'Smoking_Yes' in data.columns:
        data = data.rename(columns={'Smoking_Yes': 'Smoking'})
        
    X = data[features_to_use]
    y = data['Heart Attack Risk']
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X, y)
    return model, features_to_use

rf_model, feature_cols = train_model(df_encoded)

# --- 4. Dashboard Layout: Sidebar for User Inputs ---
st.sidebar.header("Patient Lifestyle Inputs")
age = st.sidebar.slider("Age", 18, 90, 45)
sleep = st.sidebar.slider("Sleep Hours Per Day", 2, 12, 7)
exercise = st.sidebar.slider("Exercise Hours Per Week", 0.0, 20.0, 3.0)
stress = st.sidebar.slider("Stress Level (1-10)", 1, 10, 5)
cholesterol = st.sidebar.slider("Cholesterol", 120, 400, 200)

diet = st.sidebar.selectbox("Diet", ["Healthy", "Average", "Unhealthy"])
smoking = st.sidebar.radio("Smoker?", ["Yes", "No"])

# --- 5. Data Visualization (EDA) Section ---
st.subheader("📊 Dataset Insights: Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
corr_matrix = df_encoded.corr()
# Show only top 10 correlations to keep dashboard clean
sns.heatmap(corr_matrix.loc[['Heart Attack Risk'], :].drop(columns=['Heart Attack Risk']), 
            cmap='coolwarm', annot=False, ax=ax)
st.pyplot(fig)
st.caption("Notice how single lifestyle factors have low direct correlation. Heart health requires looking at the combined picture!")

# --- 6. Prediction Section ---
st.subheader("🤖 AI Risk Prediction")
if st.button("Calculate My Risk"):
    # Create a patient profile with ONLY the lifestyle features
    patient_data = pd.DataFrame(columns=feature_cols)
    patient_data.loc[0] = 0 # Initialize a single row
    
    # Fill in the exact user inputs
    patient_data['Age'] = age
    patient_data['Sleep Hours Per Day'] = sleep
    patient_data['Exercise Hours Per Week'] = exercise
    patient_data['Stress Level'] = stress
    patient_data['Cholesterol'] = cholesterol
    patient_data['Smoking'] = 1 if smoking == "Yes" else 0
    
    if diet == "Healthy": patient_data['Diet_Healthy'] = 1
    elif diet == "Unhealthy": patient_data['Diet_Unhealthy'] = 1
    
    # MEDICAL AI TRICK: Use predict_proba instead of predict
    # This gets the exact percentage of risk (class 1)
    risk_probability = rf_model.predict_proba(patient_data)[0][1]
    
    # If the AI thinks there is even a 40% chance of a heart attack, trigger the warning
    if risk_probability >= 0.40:
        st.error(f"⚠️ **High Risk Detected!** (Calculated Risk: {risk_probability*100:.1f}%) Based on your specific lifestyle combinations, our AI flags you for elevated cardiovascular risk.")
    else:
        st.success(f"✅ **Low Risk.** (Calculated Risk: {risk_probability*100:.1f}%) Your lifestyle combinations currently align with low cardiovascular risk.")