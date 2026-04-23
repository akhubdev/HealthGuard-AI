import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/diabetes_data.csv")

# Features
X = data[["BMI", "Age", "HighBP", "HighChol", "Smoker"]]

# Target
y = data["Diabetes_012"]

# Convert multi-class to binary
y = y.apply(lambda x: 1 if x > 0 else 0)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "diabetes_model.pkl")

print("Model trained successfully")