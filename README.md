# EcoTech
GFG Hackathon

## PM2.5 Prediction
Data Analysis of PM2.5 levels over time and the performance of machine learning models for predicting PM2.5 levels.

## Data Visualization

The following images are the distributions of PM2.5 over a time-period.
<br>
<br>

![PM2.5 levels over a prolonged time-period](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/PM%20time%20Series.png?raw=true)
<br>
![PM2.5 levels vs Month](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/PM%20vs%20month%20bar.png?raw=true)
<br>
![PM2.5 levels vs Year](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/PM%20vs%20year%20bar.png?raw=true)

## Machine Learning Models

The following machine learning models were used for prediction:

* AutoRegressive Model
  ![Auto Regressive Model](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/AutoRegressive%20Model.png?raw=true)
* Explainable Boosting Model
  ![Explainable Boosting Model](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/Explainable%20Boosting%20Model.png?raw=true)
* Random forest
  ![Random Forest](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/RandomForestRegressor%20Model.png?raw=true)
* MLP Regressor
  ![MLP Regressor](https://github.com/sayan112207/EcoTech/blob/main/Images/Air%20Pollution/NN%20MLPRegressor%20Model.png?raw=true)

The performance of each model was evaluated using the root mean squared error (RMSE) and mean absolute error (MSE).

#### Analysis of the ML Models
From the analysis Neural Networks seems to be the best performing model. The Autoregressive model, as a benchmark, shows poor result. Random Forest and Explainable Boosting Machine follow in a good way shape of observations, but the previous one overfit. Neural Networks are able to capture spikes in the observations following the shape of them. In all models the lag feature shifted by an hour is the most relevant to explain the outcome, the others change depending by the model. From the Partial Dependence Plot there is a confirm about the positive correlation between the ”lagged 1h” feature and the air pollution.


## Climate Patterns (Weather) Data
The Climate Patterns feature allows users to retrieve current weather data for a specified location, including temperature, humidity, wind speed, and more.

### API Used for Climate Patterns Data
The weather data is retrieved from the [Weather by API-Ninjas](https://rapidapi.com/apininjas/api/weather-by-api-ninjas) using [RapidAPI](https://rapidapi.com/hub) furnishing real-time insights.

### Features Retrieved for Climate Patterns
The app retrieves the following weather data:

- Temperature: Current temperature in Celsius.
- Feels Like: The "feels like" temperature in Celsius.
- Humidity: Humidity percentage.
- Min Temperature: Minimum temperature in Celsius.
- Max Temperature: Maximum temperature in Celsius.
- Wind Speed: Wind speed in meters per second.
- Wind Degrees: Wind direction in degrees.
- Sunrise: Time of sunrise.
- Sunset: Time of sunset.
- Cloud Coverage: Cloud coverage percentage.

## How to Use the App

1. Clone this repository to your local machine.

2. Install the required Python libraries using `pip install -r requirements.txt`.

3. Replace `"API_KEY"` with your actual API key in the Flask app code (`app.py`).

4. Run the Flask app using ```python app.py```.

5. Access the app in your web browser at `http://localhost:5000`.

6. Use the "Air Quality" and "Climate Patterns" buttons to access the respective functionalities.

7. For "Air Quality," input a date to get PM2.5 predictions.

8. For "Climate Patterns," input a city, state, country, and pincode to retrieve weather data.

## Author
[Sayan Banerjee](https://github.com/sayan112207), [Rahul Naugariya](https://github.com/RahulNaugariya), [Shubham Patel](https://github.com/shubhampatel001)


