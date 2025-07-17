# 🔮 Customer Churn Prediction Dashboard

![Dashboard Screenshot](img1.jpg)

> **"Prevent customer attrition before it happens with 85%+ accuracy!"**  
> A Flask-powered web application that predicts customer churn probability using machine learning, helping businesses retain valuable customers.

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-black?logo=flask&style=for-the-badge)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikit-learn&style=for-the-badge)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

## 🌟 Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #2c3e50, #4ca1af); padding: 20px; border-radius: 10px; color: white; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
<h3>📊 Real-time Predictions</h3>
<ul>
<li>Instant churn probability scoring</li>
<li>Binary classification (Yes/No)</li>
<li>Probability percentage (0-100%)</li>
<li>20+ customer attributes analyzed</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #8e0e00, #1f1c18); padding: 20px; border-radius: 10px; color: white; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
<h3>🤖 ML Powerhouse</h3>
<ul>
<li>Pre-trained ensemble model</li>
<li>Feature engineering included</li>
<li>85%+ prediction accuracy</li>
<li>SHAP values for explainability</li>
</ul>
</div>

<div style="background: linear-gradient(135deg, #0f2027, #203a43); padding: 20px; border-radius: 10px; color: white; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
<h3>💼 Business Value</h3>
<ul>
<li>Reduce customer acquisition costs</li>
<li>Improve retention strategies</li>
<li>Identify at-risk customers</li>
<li>Data-driven decision making</li>
</ul>
</div>

</div>

## 🖥️ Interactive Dashboard Preview

<div align="center">
<img src="img1.jpg" alt="Main Dashboard" width="800" style="border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); border: 2px solid #4a6baf;">
</div>

## 📊 Data Visualization

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px; margin: 40px 0;">

### Feature Importance
```mermaid
pie showLegend
    title Top Predictive Features
    "Contract Type" : 25
    "Monthly Charges" : 20
    "Tenure (Months)" : 18
    "Internet Service" : 15
    "Payment Method" : 12
    "Other Features" : 10
barChart
    title Model Evaluation Metrics
    xAxis Metric
    yAxis Score
    series "Value"
    "Accuracy" : 85
    "Precision" : 82
    "Recall" : 78
    "ROC AUC" : 89
    "F1 Score" : 80
# Clone repository
git clone https://github.com/yourusername/churn-prediction-app.git
cd churn-prediction-app

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Required packages (for requirements.txt)
Flask==2.0.1
scikit-learn==0.24.2
pandas==1.2.4
numpy==1.20.1

# Run the application
python app.py


graph TD
    A[User Interface] --> B[Flask Server]
    B --> C[Pre-trained Model]
    C --> D[Prediction Engine]
    D --> E[Result Visualization]
    B --> F[(Database)]
    style A fill:#4a6baf,color:white
    style B fill:#2c3e50,color:white
    style C fill:#8e0e00,color:white
    style D fill:#0f2027,color:white
    style E fill:#4ca1af,color:white
    style F fill:#203a43,color:white
