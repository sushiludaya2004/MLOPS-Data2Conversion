# Social Media Ad Campaign Conversion Prediction

## Overview
This project focuses on predicting the number of conversions from social media ad campaigns using regression models. The dataset contains information on user demographics, ad performance, and engagement metrics.

---

## Table of Contents
1. [Dataset Description](#dataset-description)
2. [Motivation](#motivation)
3. [Project Workflow](#project-workflow)
4. [Data Preprocessing](#data-preprocessing)
5. [Modeling](#modeling)
6. [Results](#results)
7. [Setup and Installation](#setup-and-installation)
8. [Key Features](#key-features)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

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
   
   **Key File:** `data_ingestion.py`  
   **Output Files:**  
   - `artifacts/data.csv` (Raw Data)  
   - `artifacts/train.csv` (Training Data)  
   - `artifacts/test.csv` (Testing Data)

### 2. **Data Transformation**
   - Preprocesses the data using separate pipelines for numerical and categorical features.
     - **Numerical Pipeline:** Imputation with the median, followed by standard scaling.  
     - **Categorical Pipeline:** Imputation with the most frequent value, followed by one-hot encoding.
   - Applies preprocessing to train and test datasets.
   - Saves the preprocessor object as a pickle file.
   
   **Key File:** `data_transformation.py`  
   **Output Files:**  
   - `artifacts/preprocessor.pkl` (Preprocessor Object)  

### 3. **Model Training**
   - Trains multiple regression models:
     - Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, and AdaBoost.
   - Tunes hyperparameters using predefined configurations.
   - Evaluates models and selects the best one based on performance metrics.
   - Saves the best-performing model as a pickle file.
   
   **Key File:** `model_trainer.py`  
   **Output Files:**  
   - `artifacts/model.pkl` (Best Model)  

## Models Used
- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Gradient Boosting Regressor**
- **Linear Regression**
- **XGBoost Regressor**
- **CatBoost Regressor**
- **AdaBoost Regressor**


## Project Workflow
The project follows a structured pipeline:
1. **Data Ingestion**: Loading and verifying data integrity.
2. **Data Transformation**: Handling missing values, encoding categorical variables, scaling numerical features, and feature engineering.
3. **Model Prediction**: Building and evaluating regression models to predict conversions.

---

## Data Preprocessing
### Steps:
- **Data Cleaning**: Removing inconsistencies and handling missing values.
- **Feature Engineering**: Encoding gender and interest, scaling impressions, clicks, and spent.
- **Splitting Data**: Dividing into training and testing sets (e.g., 80-20 split).

---

## Modeling
### Techniques Used:
- Regression models:
  - Linear Regression
  - Decision Tree Regression
  - Random Forest Regression
- **Hyperparameter Tuning**: Optimizing model performance.
- **Evaluation Metrics**: 
  - R² Score
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)

---

## Results
### Key Findings:
- Best-performing model: [Your Best Model]
- Performance Metrics:
  - R²: [Value]
  - MSE: [Value]
  - MAE: [Value]

---

## Setup and Installation
### Prerequisites:
- Python (>= 3.8)
- Libraries:
  ```bash
  pip install pandas numpy scikit-learn matplotlib seaborn