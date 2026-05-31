import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
df = pd.read_csv("data/Clean_Dataset.csv")

# Drop useless columns
df = df.drop(columns=["Unnamed: 0", "flight"])

# Convert text columns to numbers
df = pd.get_dummies(df, columns=["airline", "source_city", "destination_city",
                                  "departure_time", "arrival_time", "stops", "class"])

# Split into input and output
X = df.drop(columns=["price"])
y = df["price"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train lighter model
print("Training model... please wait")
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test accuracy
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: ₹{mae:.2f}")

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(list(X.columns), "columns.pkl")
print("Model saved!")