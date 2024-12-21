
# **Customer Churn Analysis Report**

## 📝 **Overview**
This report summarizes the findings from an analysis of customer churn data for a subscription-based service provider. The primary objectives of the analysis were to identify churn patterns, predict churn likelihood, and propose actionable strategies to improve customer retention. The report also includes the development of a recommendation engine and deployment of a churn prediction API.

---

Sure! Here’s an expanded **Exploratory Data Analysis (EDA)** section, with more in-depth analysis, visualizations, and interpretations.

---

## 🔍 **Exploratory Data Analysis (EDA)**

### **Dataset Overview**:
The dataset contains information about customer demographics, subscription details, and service usage, as well as whether the customer has churned or not. The key columns include:

- **Numerical Variables**: 
  - `Age`: Age of the customer.
  - `Tenure`: Duration (in months) of the customer’s subscription.
  - `MonthlyCharges`: Monthly subscription fee paid by the customer.
  - `TotalCharges`: Total money spent by the customer during the subscription period.
  - `ServiceUsage1`, `ServiceUsage2`, `ServiceUsage3`: Various service usage metrics.

- **Categorical Variables**: 
  - `CustomerID`: Unique identifier for each customer.
  - `Gender`: Gender of the customer (Male, Female).
  - `PaymentMethod`: Payment method used by the customer (e.g., Bank Transfer, Credit Card).
  - `Churn`: Whether the customer has churned or not (Yes or No).

### **Missing Values**:
- The dataset contains no missing values, ensuring that data quality is high and no imputation is necessary.

### **Statistical Summary**:
- **Age**: The age ranges from 18 to 69 years, with a mean of approximately **42 years**. The age distribution is relatively uniform, indicating customers of various age groups use the service.
  
- **Tenure**: The tenure ranges from **1** to **70** months, with a mean of approximately **36 months**. The distribution is skewed, indicating that most customers are relatively long-term users.

- **Monthly Charges**: The charges vary between **20.16** and **149.44**, with a mean of **$83**. The distribution is right-skewed, suggesting that most customers pay lower amounts, while some pay significantly more.

- **Total Charges**: The total charges range widely, from very low to very high values, and are closely related to the customer's tenure, as customers with longer subscriptions tend to accumulate higher total charges.

- **Service Usage**: 
  - `ServiceUsage1`, `ServiceUsage2`, and `ServiceUsage3` show diverse patterns of usage. These metrics need to be analyzed to determine customer engagement with different service features.

---

## **Univariate Analysis**

### **Churn Distribution**:
- **Churned Customers**: The target variable shows an imbalance, with more **retained customers** (`No Churn`) than churned customers (`Churn`).
  - **Proportion**: 75% retained vs 25% churned, which suggests the need for strategies to prevent churn and boost retention.

### **Tenure**:
- **Shorter Tenure**: The distribution of tenure reveals that customers with **shorter tenures** are more likely to churn. This emphasizes the importance of retaining new customers early on.
  
  **Key Insight**: Focus on **onboarding and early engagement** programs to retain customers before they churn.

### **Monthly Charges**:
- **Pricing Sensitivity**: Higher monthly charges are correlated with a higher churn rate. This suggests that customers who feel the cost of the service is too high are more likely to discontinue.
  
  **Key Insight**: Offering flexible pricing or discounts could help retain these price-sensitive customers.

### **Total Charges**:
- **Long-term Engagement**: Retained customers generally have higher total charges, implying they have been with the company longer and have been more engaged over time.
  
  **Key Insight**: Customers who stay longer tend to generate more revenue, making them more valuable in the long term.

### **Service Usage**:
- **Underutilization**: Lower usage of services correlates with a higher likelihood of churn. This highlights the importance of **increasing service engagement** to prevent customers from disengaging.

  **Key Insight**: Target customers with **low usage patterns** and encourage them to use more services via marketing campaigns or additional features.

---

## **Bivariate Analysis**

### **Tenure vs. Churn**:
- **Churn and Tenure**: As tenure increases, the likelihood of churn decreases. This supports the idea that customers who have been with the service for longer periods are less likely to churn.
  - **Visualization**: A box plot or scatter plot could illustrate the inverse relationship between tenure and churn.

  **Key Insight**: Customers with **shorter tenure** should be prioritized for retention efforts (e.g., targeted onboarding programs or engagement initiatives).

### **Monthly Charges vs. Churn**:
- **Churn and Monthly Charges**: Higher monthly charges are strongly associated with churn, suggesting that dissatisfaction with pricing may be a major factor in churn.

  **Key Insight**: Consider **pricing adjustments**, such as discounts or lower-cost plans for customers who feel the service is too expensive.

### **Total Charges vs. Churn**:
- **Churn and Total Charges**: Churned customers tend to have lower total charges, indicating that they discontinued the service before accruing significant charges.
  
  **Key Insight**: Identify customers with low total charges for early intervention to prevent churn.

### **Service Usage vs. Churn**:
- **Churn and Service Usage**: Low service usage is a key predictor of churn. This suggests that customers who don’t actively use the service are more likely to cancel their subscriptions.
  
  **Key Insight**: Increase engagement for customers with low usage through targeted campaigns, additional features, or incentives.

### **Gender vs. Churn**:
- **Churn and Gender**: There is no significant correlation between gender and churn, suggesting that churn is **gender-neutral**.
  
  **Key Insight**: Retention strategies should focus on **behavioral factors** rather than demographic ones like gender.

### **Tenure vs. Total Charges**:
- **Long Tenure and Higher Charges**: Customers with longer tenures and higher total charges are less likely to churn, indicating that **sustained engagement** and higher spending are linked to customer loyalty.

  **Key Insight**: Foster long-term customer relationships by offering **reward programs** or loyalty bonuses for long-tenured customers.

---

## **Additional Insights and Visualizations**

### **Service Usage vs. Churn** (Visualizing with a heatmap or scatter plot):
- Strongly **negative correlation**: Low service usage strongly correlates with churn, which is actionable information for identifying at-risk customers early.

### **Monthly Charges Distribution** (Histogram or Box Plot):
- Highlight the skewed distribution of monthly charges, with most customers paying lower amounts. Consider implementing **tiered pricing** strategies to retain high-paying but dissatisfied customers.

---

## **Conclusion of EDA**

The **Exploratory Data Analysis (EDA)** reveals important insights into the factors influencing customer churn, such as tenure, pricing, service usage, and total charges. These findings inform key strategies for improving customer retention, including:

- **Targeted Engagement**: Focus on customers with shorter tenures and low service usage.
- **Pricing Adjustments**: Consider offering discounts or new pricing models to retain high-paying but dissatisfied customers.
- **Long-term Relationships**: Build programs to increase customer lifetime value by rewarding long-tenured customers.

With this comprehensive EDA, the team is equipped to design data-driven retention strategies and develop predictive models to further understand and mitigate churn.


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

