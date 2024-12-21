
Customer Churn Analysis Report
Overview
This report summarizes the findings from the analysis of customer churn data for a subscription-based service provider. The objective was to identify patterns, predict churn, and propose actionable strategies to enhance customer retention. The analysis also included building a recommendation engine and deploying a churn prediction API.

1. Exploratory Data Analysis (EDA)
Churn Distribution:
The dataset shows a slight imbalance, with more retained customers (label: No Churn) compared to churned ones (label: Churn).

Key Observations:

Customers with shorter tenures are more likely to churn.
Higher monthly charges correlate with increased churn rates.
Low service usage across all metrics is a significant churn factor.
Correlations:

Positive correlation: MonthlyCharges and churn likelihood.
Negative correlation: Tenure and churn likelihood.
2. Model Performance
Models Evaluated:
Logistic Regression, Decision Trees, and Random Forest.

Best Model:
The Random Forest model achieved the highest performance with the following metrics:

Accuracy: 80%
Precision: 81%
Recall: 82%
F1-score: 83%
Confusion Matrix Insights:

Effectively classified both churned and retained customers, with minimal false positives and negatives.
3. Feature Importance
![Alt Text]
Top Factors Contributing to Churn:
Tenure: Longer tenures reduce churn probability.
Monthly Charges: Higher charges increase churn risk.
Service Usage: Active engagement significantly lowers churn likelihood.
Total Charges: Cumulative spending indicates customer loyalty.
4. Recommendations for Customer Retention
Early Engagement:
Develop programs to engage new customers with low tenure.

Cost Optimization:

Offer discounts or incentives for high monthly charge plans.
Introduce budget-friendly plans for cost-sensitive customers.
Service Promotion:

Encourage underutilizing customers to increase service usage.
Use targeted marketing campaigns based on usage patterns.
Personalized Recommendations:
Leverage the collaborative filtering recommendation engine to suggest relevant services/products to customers.

Conclusion
The analysis provides actionable insights into customer churn behavior and effective strategies to enhance retention. The predictive model can guide targeted interventions, while the recommendation engine offers opportunities to improve engagement and satisfaction


## 📂 Project Structure

📦Project Folder 
├── 📄 app.py # Flask API code 
├── 📄 churn_model.pkl # Trained Random Forest model
├── 📊 data/ # Dataset files 
├── 📄 requirements.txt # Python dependencies 
├── 📄 README.md # Project documentation 
├── 📄 notebook.ipynb # Jupyter notebook with detailed analysis


## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Recommended: Virtual environment (e.g., `venv`, `conda`)


### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Himanshu9532/Customer-Churn.git
   cd churn-prediction
   Install dependencies:
pip install -r requirements.txt

Launch the Flask API:
python app.py
🖥️ Usage
1. Testing the API
The Flask API predicts churn based on input customer data.

Endpoint: /predict

Method: POST




Sample Input:
{
    "Gender": 1,
    "Age": 30,
    "Tenure": 10,
    "MonthlyCharges": 100.5,
    "TotalCharges": 1050.5,
    "PaymentMethod": 2,
    "ServiceUsage1": 60,
    "ServiceUsage2": 40,
    "ServiceUsage3": 70
}


Recommendations
Collaborative filtering suggests personalized services to customers based on their similarity scores and usage patterns.


🤝 Contributing
Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add new feature".
Push to the branch: git push origin feature-name.
Open a pull request.

📞 Contact
Name: Himanshu Gupta
Email: himanshugupta95326@gmail.com
GitHub:https://github.com/Himansh9532

