import pandas as pd
import pickle

# 1. Load the saved model
with open('improved_churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Prepare new data (with ALL features used in training)
new_data = pd.DataFrame({
    'customerID': ['9999-TEST'],
    'gender': ['Male'],
    'SeniorCitizen': [0],
    'Partner': ['Yes'],
    'Dependents': ['No'],
    'tenure': [24],
    'PhoneService': ['Yes'],
    'MultipleLines': ['No'],
    'InternetService': ['DSL'],
    'OnlineSecurity': ['No'],
    'OnlineBackup': ['Yes'],
    'DeviceProtection': ['No'],
    'TechSupport': ['Yes'],
    'StreamingTV': ['Yes'],
    'StreamingMovies': ['No'],
    'Contract': ['Month-to-month'],
    'PaperlessBilling': ['No'],
    'PaymentMethod': ['Electronic check'],
    'MonthlyCharges': [75.5],
    'TotalCharges': [1820.0]
})

# 3. REPLICATE ALL FEATURE ENGINEERING FROM TRAINING
# a) Fix TotalCharges (as done in training)
new_data['TotalCharges'] = pd.to_numeric(new_data['TotalCharges'], errors='coerce').fillna(0)

# b) Add tenure_group (critical missing feature!)
new_data['tenure_group'] = pd.cut(new_data['tenure'], 
                                 bins=[0, 12, 24, 36, 48, 60, 72],
                                 labels=['0-1yr', '1-2yr', '2-3yr', '3-4yr', '4-5yr', '5+yr'])

# c) Add other engineered features
new_data['AvgMonthlySpend'] = new_data['TotalCharges'] / (new_data['tenure'] + 1e-6)
new_data['HighMonthlySpend'] = (new_data['MonthlyCharges'] > 64.76).astype(int)  # Median from training

# 4. Drop columns not used by model
X_new = new_data.drop(['customerID'], axis=1)

# 5. Predict
try:
    churn_prob = model.predict_proba(X_new)[:, 1][0]  # Get first prediction
    print(f"\nPredicted Churn Probability: {churn_prob:.1%}")
    print(f"Verification: All features present? {set(X_new.columns) == set(model.feature_names_in_)}")
except Exception as e:
    print(f"Error: {str(e)}")
    print("Missing features:", set(model.feature_names_in_) - set(X_new.columns))