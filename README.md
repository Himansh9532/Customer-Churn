Here is a refined version of your report with improved formatting, headings, and icons suitable for inclusion in a GitHub README file:

---

# **Customer Churn Analysis Report**

## 📝 **Overview**
This report summarizes the findings from an analysis of customer churn data for a subscription-based service provider. The primary objectives of the analysis were to identify churn patterns, predict churn likelihood, and propose actionable strategies to improve customer retention. The report also includes the development of a recommendation engine and deployment of a churn prediction API.

---

## 🔍 **1. Exploratory Data Analysis (EDA)**

### **Churn Distribution:**
- **Imbalance**: The dataset exhibits a slight imbalance, with a higher number of retained customers (`No Churn`) than churned customers (`Churn`).

### **Key Observations:**
- **Tenure**: Customers with shorter tenures tend to have higher churn rates.
- **Monthly Charges**: Higher charges correlate with a greater likelihood of churn.
- **Service Usage**: Low usage across various service metrics is a significant churn indicator.

### **Correlations:**
- **Positive Correlation**: Monthly charges and churn likelihood.
- **Negative Correlation**: Tenure and churn likelihood.

---

## ⚙️ **2. Model Performance**

### **Models Evaluated:**
- Logistic Regression
- Decision Trees
- Random Forest

### **Best Model: Random Forest**
- **Accuracy**: 80%
- **Precision**: 81%
- **Recall**: 82%
- **F1-score**: 83%

### **Confusion Matrix Insights:**
- The Random Forest model effectively classified both churned and retained customers with minimal false positives and negatives.

---

## 📊 **3. Feature Importance**

![Feature Importance](images/Feature%20importance.png)

### **Top Factors Contributing to Churn:**
1. **Tenure**: Longer tenures reduce churn probability.
2. **Monthly Charges**: Higher charges increase the risk of churn.
3. **Service Usage**: Active engagement significantly lowers churn likelihood.
4. **Total Charges**: Cumulative spending reflects customer loyalty and retention.

---

## 📈 **4. Recommendations for Customer Retention**

### **Early Engagement:**
- Implement programs designed to engage new customers, particularly those with short tenures, to improve retention from the outset.

### **Cost Optimization:**
- Offer discounts or incentives for customers on high-priced plans.
- Introduce budget-friendly pricing options for cost-sensitive customers.

### **Service Promotion:**
- Encourage customers who underutilize services to engage more by offering personalized incentives or targeted campaigns.

### **Personalized Recommendations:**
- Use a collaborative filtering recommendation engine to suggest relevant services/products, thereby increasing customer satisfaction and engagement.

---

## 🧐 **Insights from EDA**

### **Data Types:**
- **Numerical**: Age, Tenure, MonthlyCharges, TotalCharges, ServiceUsage1, ServiceUsage2, ServiceUsage3.
- **Categorical**: CustomerID, Gender, PaymentMethod, Churn.

### **Missing Values**: 
- The dataset contains no missing values.

### **Statistics**:
- **Age**: Ranges from 18 to 69 years, with a mean of ~42 years.
- **Tenure**: Ranges from 1 to 70 months, with a mean of ~36 months.
- **Monthly Charges**: Vary between 20.16 and 149.44, with a mean of ~$83.
- **Service Usage**: Service usage metrics show diverse patterns.

---

## 📉 **Univariate Analysis Summary**

- **Churn**: The dataset has a slight imbalance with more retained customers.
- **Tenure**: Customers with shorter tenures are more likely to churn, indicating the need for early intervention.
- **Monthly Charges**: Higher monthly charges correlate with churn, suggesting that cost dissatisfaction may play a role.
- **Total Charges**: Retained customers generally have higher total charges, indicating long-term engagement.
- **Service Usage**: Lower service usage correlates with higher churn rates, highlighting the importance of engagement.

### **Categorical Variables**:
- No significant trends were found between gender or other categorical features directly affecting churn.

---

## 🔄 **Bivariate Analysis Summary**

### **Tenure vs. Churn**:
- Shorter tenure customers exhibit higher churn rates, indicating early dissatisfaction or unmet expectations.

### **Monthly Charges vs. Churn**:
- A strong positive correlation between higher monthly charges and churn, suggesting pricing issues may lead to customer loss.

### **Total Charges vs. Churn**:
- Churned customers tend to have lower total charges, possibly due to early service discontinuation.

### **Gender vs. Churn**:
- No significant relationship between gender and churn, indicating churn behavior is gender-neutral.

### **Service Usage vs. Churn**:
- Low service usage strongly correlates with churn, emphasizing the need for strategies to boost engagement.

### **Tenure vs. Total Charges**:
- Long-tenure customers with higher total charges are less likely to churn, underlining the importance of sustained engagement.

---

## 🚀 **Conclusion**
The analysis provides valuable insights into customer churn behaviors and offers actionable strategies for improving retention. The Random Forest model's strong performance in predicting churn will support targeted interventions, while the recommendation engine presents an opportunity to enhance engagement through personalized service suggestions.

By applying these findings, the service provider can enhance customer satisfaction and reduce churn rates, ensuring a more loyal customer base.












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

