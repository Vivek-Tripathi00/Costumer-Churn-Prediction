from flask import Flask, request, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('improved_churn_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    probability = None
    error = None

    if request.method == 'POST':
        try:
            # Get form data
            tenure = float(request.form['tenure'])
            monthly_charges = float(request.form['monthly_charges'])
            contract = request.form['contract']
            internet_service = request.form['internet_service']
            payment_method = request.form['payment_method']
            senior_citizen = int(request.form['senior_citizen'])
            partner = request.form['partner']
            dependents = request.form['dependents']
            phone_service = request.form['phone_service']
            multiple_lines = request.form['multiple_lines']
            online_security = request.form['online_security']
            online_backup = request.form['online_backup']
            device_protection = request.form['device_protection']
            tech_support = request.form['tech_support']
            streaming_tv = request.form['streaming_tv']
            streaming_movies = request.form['streaming_movies']
            paperless_billing = request.form['paperless_billing']
            gender = request.form['gender']  # Added gender

            # Calculate derived features
            total_charges = monthly_charges * tenure
            avg_monthly_spend = total_charges / (tenure + 1e-6)  # Avoid division by zero
            tenure_group = pd.cut([tenure], bins=[0, 12, 24, 36, 48, 60, 72], 
                                 labels=['0-1yr', '1-2yr', '2-3yr', '3-4yr', '4-5yr', '5+yr'])[0]

            # Create input DataFrame matching training features
            input_data = pd.DataFrame({
                'tenure': [tenure],
                'MonthlyCharges': [monthly_charges],
                'TotalCharges': [total_charges],
                'AvgMonthlySpend': [avg_monthly_spend],
                'Contract': [contract],
                'InternetService': [internet_service],
                'PaymentMethod': [payment_method],
                'SeniorCitizen': [senior_citizen],
                'Partner': [partner],
                'Dependents': [dependents],
                'PhoneService': [phone_service],
                'MultipleLines': [multiple_lines],
                'OnlineSecurity': [online_security],
                'OnlineBackup': [online_backup],
                'DeviceProtection': [device_protection],
                'TechSupport': [tech_support],
                'StreamingTV': [streaming_tv],
                'StreamingMovies': [streaming_movies],
                'PaperlessBilling': [paperless_billing],
                'tenure_group': [tenure_group],
                'gender': [gender]  # Added gender
            })

            # Predict
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1] * 100  # Probability of churn (%)
            prediction = 'Yes' if prediction == 1 else 'No'

        except Exception as e:
            error = str(e)

    return render_template('index.html', prediction=prediction, probability=probability, error=error)

if __name__ == '__main__':
    app.run(debug=True)
