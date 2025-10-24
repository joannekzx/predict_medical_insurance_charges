import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("Cleaned_Insurance.csv")

X = df[['age', 'sex_encoded', 'bmi', 'children', 'smoker_encoded', 'region_encoded',
        'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']]
y = df['charges_log']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

train_data = X_train.copy()
train_data['charges_log'] = y_train

test_data = X_test.copy()
test_data['charges_log'] = y_test

train_data.to_csv("training_data.csv", index=False)
test_data.to_csv("testing_data.csv", index=False)

print(f"Training data shape: {train_data.shape}")
print(f"Testing data shape: {test_data.shape}")
print("Files saved: training_data.csv and testing_data.csv")
