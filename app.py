import pickle
import numpy as np
import requests
import datetime
from flask import Flask, request, render_template

# Load the trained model and scaler from the pickle file
with open('pm_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_pm():
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

    # Create a list of tuples, each containing an hour and its prediction
    predictions = [(f"{hour:02}:00", prediction) for hour, prediction in enumerate(pm_predictions)]

    # Display the predictions
    return render_template('result.html', predictions=predictions)

    # Display the predictions
    return render_template('result.html', predictions=pm_predictions)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        # Get user input from the form
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        pincode = request.form['pincode']

        # Make an API request to get weather data
        headers = {
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': "weather-by-api-ninjas.p.rapidapi.com"
        }
        params = {
            'zip': pincode,
            'city': city,
            'state': state,
            'country': country
        }
        response = requests.get("https://weather-by-api-ninjas.p.rapidapi.com/v1/weather", headers=headers, params=params)
        weather_data = response.json()

        # Convert timestamps to readable date and time
        weather_data['sunrise'] = datetime.datetime.fromtimestamp(weather_data['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        weather_data['sunset'] = datetime.datetime.fromtimestamp(weather_data['sunset']).strftime('%Y-%m-%d %H:%M:%S')

        return render_template('weather.html', weather_data=weather_data)

    return render_template('weather.html', weather_data=None)

if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
