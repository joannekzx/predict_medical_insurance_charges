# Predicting Medical Insurance Charges

This project explores various regression models to predict medical insurance costs, based on the **NUS SDS Mini-Datathon 2025** challenge. The analysis moves from a simple baseline model to more complex ensemble methods, focusing on model accuracy, feature importance, and fairness.

## 🎯 Project Goals

Based on the datathon brief (`NUS SDS Mini-Datathon 2025.pdf`), the primary objectives are:

1.  **Prediction:** Build regression models (baseline and advanced) to accurately predict insurance charges.
2.  **Feature Analysis:** Identify and analyze the key factors that drive insurance costs.
3.  **Fairness Check:** Assess whether the model's predictions and errors differ significantly across demographic groups (e.g., sex, region).

---

## 📂 File Structure

Here is an overview of the key files in this project:

* `NUS SDS Mini-Datathon 2025.pdf`: The original project brief, dataset description, and datathon rules.
* `requirements.txt`: A list of Python libraries required to run the Jupyter notebooks.
* `splitdata.py`: A Python script to preprocess the data and split it into `training_data.csv` and `testing_data.csv`.
* `hack.Rmd` / `hack.html`: An R notebook (and its HTML output) that details data exploration and a baseline Linear Regression model.
* `randomtree.ipynb`: A Jupyter notebook implementing a **Random Forest Regressor** and conducting a fairness analysis.
* `xgbregressor.ipynb`: A Jupyter notebook implementing an **XGBoost Regressor**, including feature importance (SHAP) and a fairness analysis.

---

## 🚀 Getting Started

Follow these steps to set up and run the analysis.

### 1. Prerequisites

You will need both **Python (3.x)** and **R** installed.

* **Python Dependencies:** Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
* **R Dependencies:** (For `hack.Rmd`) Ensure you have the following R packages installed:
    * `readr`
    * `dplyr`
    * `openxlsx`
    * `lmtest`
    * `sandwich`
    * `ggcorrplot`

### 2. Data Preparation

This project assumes you have the dataset `Cleaned_Insurance.csv` in the root directory.

Run the `splitdata.py` script to generate the `training_data.csv` and `testing_data.csv` files, which are used by all the models:

```bash
python splitdata.py
```

3. . Running the Models
You can now explore the different modeling approaches:

Linear Regression (R): Open and run the hack.Rmd file in an R environment (like RStudio).

Random Forest (Python): Open and run the randomtree.ipynb notebook using Jupyter.

XGBoost (Python): Open and run the xgbregressor.ipynb notebook using Jupyter.

📖 Models & Analysis
This project implements and compares three different regression models.

1. Baseline: Linear Regression (in hack.Rmd)
Goal: Establish a baseline performance metric.

Method: A multiple linear regression model (lm) was built in R to predict the log of insurance charges.

Findings: Identified age, bmi, children, and smoker status as highly significant linear predictors.

2. Advanced: Random Forest (in randomtree.ipynb)
Goal: Improve upon the baseline using a non-linear ensemble method.

Method: Implemented RandomForestRegressor from scikit-learn.

Analysis: Includes hyperparameter tuning (GridSearchCV) and a fairness analysis that breaks down model error metrics by sex and region.

3. Advanced: XGBoost (in xgbregressor.ipynb)
Goal: Achieve high predictive accuracy using a gradient-boosting algorithm.

Method: Implemented XGBRegressor and used GridSearchCV for hyperparameter tuning.

Analysis:

Feature Importance: Uses SHAP (SHapley Additive exPlanations) to provide clear, visual explanations of which features have the most impact on predictions.

Fairness Check: Performs a detailed group error analysis to check for disparities in RMSE and MAE across different regions, fulfilling a key requirement of the datathon.
