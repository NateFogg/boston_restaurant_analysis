# Data Analysis of Boston Restaurants Using The Yelp Fusion API

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Machine Learning Models](#machine-learning-models)
  - [Random Forest Regressor](#random-forest-regressor)
  - [XGBoost Regressor](#xgboost-regressor)
- [Feature Importance](#feature-importance)
- [Conclusion](#conclusion)

## Introduction
This project involves the analysis and modeling of Boston restaurant data using the Yelp Fusion API. It includes data preprocessing, exploratory data analysis (EDA), and the development of machine learning models to predict a Balanced Rating Score (BRS) for restaurants. 

## Getting Started

- You must obtain authorization to Yelp's Devloper Services here: https://docs.developer.yelp.com/docs/getting-started
- Replace the TOKEN variable in data_load.py with your API key
- Adhere to Yelp's API Terms of Use: https://www.yelp.com/developers/v3/api_terms

### Prerequisites

Before running the code, make sure you have the following prerequisites installed:

- Python 3.x
- Required Python libraries (NumPy, pandas, scikit-learn, XGBoost, geopandas, geoplot, seaborn, matplotlib)


## Data Preprocessing

The code begins with data preprocessing, which includes flattening JSON data, encoding categorical features, handling missing values, and creating new features such as the Balanced Rating Score (BRS).

## Exploratory Data Analysis (EDA)

EDA is a crucial step in understanding the data. The code provides various visualizations to explore the distribution of BRS, review counts, restaurant ratings, and other key features. It also investigates the relationships between different variables.

## Machine Learning Models

### Random Forest Regressor

The Random Forest Regressor is trained and tuned to predict the BRS of restaurants. The code includes hyperparameter tuning using both randomized search and grid search.

### XGBoost Regressor

The XGBoost Regressor is another machine learning model used for BRS prediction. Similar to the Random Forest Regressor, hyperparameter tuning is performed to optimize model performance.

## Feature Importance

The code presents feature importance analysis for both the Random Forest and XGBoost models. It visualizes the importance of each feature in predicting the BRS.

## Conclusion

This README provides an overview of the code's functionality and how to get started. For more detailed information, please refer to the code comments.

If you have any questions or need further assistance, feel free to reach out.


