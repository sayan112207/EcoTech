import pickle
import numpy as np

# Load the trained model and scaler from the pickle file
with open('pm_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    selected_date = request.form['selected_date']
    year, month, day = map(int, selected_date.split('-'))

    # Predict PM2.5 values for the entire day (0 to 23 hours)
    start_hour = 0
    end_hour = 23

    # Prepare the input date and hour range
    input_dates = [[year, month, day, hour] for hour in range(start_hour, end_hour + 1)]
    input_dates_scaled = scaler.transform(input_dates)
    pm_predictions_log = model.predict(input_dates_scaled)
    pm_predictions = np.expm1(pm_predictions_log)

    # Display the predictions
    return render_template('result.html', predictions=pm_predictions)

if __name__ == '__main__':
    app.run(debug=True)