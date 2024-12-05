# Social Media Ad Campaign Conversion Prediction

## Overview
This project focuses on predicting the number of conversions from social media ad campaigns using regression models. The dataset contains information on user demographics, ad performance, and engagement metrics.

---

## Table of Contents
1. [Dataset Description](#dataset-description)
2. [Motivation](#motivation)
3. [Project Workflow](#project-workflow)
5. [Modeling](#modeling)
6. [Results](#results)
7. [Setup and Installation](#setup-and-installation)
8. [Key Features](#key-features)
9. [Project Screenshots](#project-screenshots)


---

## Dataset Description
### Source:
The data is from an anonymous organization's social media ad campaign and can be downloaded [here](#).

### Content:
The dataset `conversion_data.csv` contains 1,143 observations with the following features:
- **Age**: Age of the person who saw the ad.
- **Gender**: Gender of the person who saw the ad.
- **Interest**: A code representing the interest category from the person's Facebook profile.
- **Impressions**: Number of times the ad was displayed.
- **Clicks**: Number of times the ad was clicked.
- **Spent**: Amount paid by the company to show the ad.
- **Total Conversion**: Target variable—total number of inquiries about the product.

---

## Motivation
Social media ad campaigns are crucial for driving sales and conversions. This project aims to help businesses optimize their ad spending by predicting potential conversions based on key metrics. Insights can improve marketing strategies, especially for platforms like Google Adwords.

---

## Project Workflow

### 1. **Data Ingestion**
   - Reads the dataset (`upd_data.csv`).
   - Splits the data into training (80%) and testing (20%) sets.
   - Saves the raw, train, and test datasets as CSV files in the `artifacts` folder.

### 2. **Data Transformation**
   - Preprocesses the data using separate pipelines for numerical and categorical features.
     - **Numerical Pipeline:** Imputation with the median, followed by standard scaling.  
     - **Categorical Pipeline:** Imputation with the most frequent value, followed by one-hot encoding.
   - Applies preprocessing to train and test datasets.
   - Saves the preprocessor object as a pickle file.

### 3. **Model Training**
   - Trains multiple regression models:
     - Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, and AdaBoost.
   - Tunes hyperparameters using predefined configurations.
   - Evaluates models and selects the best one based on performance metrics.
   - Saves the best-performing model as a pickle file.

---

## Modeling
### Techniques Used:
- Regression models:
  - Linear Regression
  - Decision Tree Regression
  - Random Forest Regression
  - Gradient Boosting
  - XGBoost
  - AdaBoost
- **Hyperparameter Tuning**: Optimizing model performance.
- **Evaluation Metrics**: 
  - R² Score
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)

---

## Results
### Key Findings:
- Best-performing model: Random Forest Regressor
- Performance Metrics:
  - R²: 81%

---

## Setup and Installation

### Run Locally

1. Clone the project

```bash
git clone https://github.com/sushiludaya2004/MLOPS-Data2Conversion.git
```

2. Go to the project directory

```bash
cd MLOPS-Data2Conversion
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```
---


## Key Features

- **Data Ingestion**: Efficiently reads, splits, and saves data for model training.
- **Data Transformation**: Automated preprocessing pipeline for numerical and categorical data.
- **Modeling**: Multiple regression models with hyperparameter tuning and evaluation.
- **Prediction**: Real-time prediction interface using Streamlit.
- **Best Model Selection**: Automatically selects and saves the best-performing model based on evaluation.
---


## Project Screenshots

Here are some screenshots of the project in action:

![Screenshot 1](path_to_screenshot1.png)
*Description of Screenshot 1*

![Screenshot 2](path_to_screenshot2.png)
*Description of Screenshot 2*
