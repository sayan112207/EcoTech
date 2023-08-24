import pickle
import numpy as np
import requests
import datetime
from flask import Flask, request, render_template

# Load the trained model and scaler from the pickle file
with open('pm_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

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
            'X-RapidAPI-Key': "e512494693mshfb53e30cb046452p189817jsn44e6cd9f8fe6",
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
    app.run(debug=True)
