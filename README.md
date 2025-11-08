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
