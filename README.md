# EcoTech
GFG Hackathon

## PM2.5 Prediction Project
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

## Instructions

To run the project, clone the repository and install the dependencies.

### Step 1: Run all the cells in Air Quality.ipynb
### Step 2: Run the command 
```
python app.py
```


I hope this helps!
