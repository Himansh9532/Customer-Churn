from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models and encoders
random_forest_model = joblib.load('model/random_forest_best_model.pkl')
le_gender = joblib.load('model/le_gender.pkl')
le_payment_method = joblib.load('model/le_payment_method.pkl')
le_churn = joblib.load('model/le_churn.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        gender = int(request.form['Gender'])
        age = float(request.form['Age'])
        tenure = float(request.form['Tenure'])
        monthly_charges = float(request.form['MonthlyCharges'])
        total_charges = float(request.form['TotalCharges'])
        payment_method = int(request.form['PaymentMethod'])
        service_usage1 = float(request.form['ServiceUsage1'])
        service_usage2 = float(request.form['ServiceUsage2'])
        service_usage3 = float(request.form['ServiceUsage3'])
        average_spend_per_month = float(request.form['AverageSpendPerMonth'])

        # Prepare input for prediction
        features = np.array([[gender, age, tenure, monthly_charges, total_charges,
                              payment_method, service_usage1, service_usage2,
                              service_usage3, average_spend_per_month]])
        
        # Make prediction
        prediction = random_forest_model.predict(features)
        prediction_decoded = le_churn.inverse_transform(prediction)  # Decode if necessary
        
        result = 'Churn' if prediction_decoded[0] == 1 else 'No Churn'

        return render_template('index.html', prediction=result)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)