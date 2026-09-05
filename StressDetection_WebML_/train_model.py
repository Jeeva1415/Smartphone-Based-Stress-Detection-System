import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
# Load dataset
data = pd.read_csv("stress_data.csv")

# Encode target
le = LabelEncoder()
data["stress_encoded"] = le.fit_transform(data["stress"])

X = data[[
    "heart_rate",
    "temperature",
    "physical_activity",
    "digital_activity",
    "sleep_hours",
    "screen_time",
    "activity_balance",
    "context_score"
]]

y = data["stress_encoded"]

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("Model trained successfully")
