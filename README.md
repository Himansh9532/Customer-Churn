# 🌀 Customer Churn Prediction & Recommendation System

This project analyzes customer churn for a subscription-based service provider, builds a prediction model, and includes a collaborative filtering recommendation engine to enhance customer retention. It also provides a Flask API for deploying the churn prediction model.


## 🚀 Features
- **Exploratory Data Analysis (EDA):** Gain insights into churn distribution, trends, and key patterns.
- **Predictive Modeling:** Logistic Regression, Decision Tree, and Random Forest models for churn prediction.
- **Feature Importance:** Identifies the most influential factors in customer churn.
- **Recommendation Engine:** Collaborative filtering to suggest additional services/products.
- **Deployment:** Flask API for churn prediction.

---

## 📂 Project Structure

📦Project Folder ├── 📄 app.py # Flask API code ├── 📄 churn_model.pkl # Trained Random Forest model ├── 📊 data/ # Dataset files ├── 📄 requirements.txt # Python dependencies ├── 📄 README.md # Project documentation ├── 📄 notebook.ipynb # Jupyter notebook with detailed analysis


---

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
📊 Results
Feature Importance

Recommendations
Collaborative filtering suggests personalized services to customers based on their similarity scores and usage patterns.

🤝 Contributing
Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add new feature".
Push to the branch: git push origin feature-name.
Open a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📞 Contact
Name: Himanshu Gupta
Email: himanshugupta95326@gmail.com
GitHub:https://github.com/Himansh9532

