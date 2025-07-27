import pandas as pd
import joblib
import pickle

# Load model and scaler
model = joblib.load("best_startup_model.pkl")
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load expected features
expected_features = joblib.load("input_columns.pkl")

# Load the input CSV
df = pd.read_csv("Final-startup_success_predictions.csv")

print("📄 Columns found in the input CSV:")
print(df.columns.tolist())

# Step 1: Remove unwanted columns FIRST (like previous predictions or target)
columns_to_remove = ['Actual Category', 'Predicted Category', 'Success Category', 'Success Category_High',
                     'Success Category_Medium', 'Success Category_Low']
df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)

# Step 2: Add any missing expected features
for col in expected_features:
    if col not in df.columns:
        print(f"⚠️ Missing column in input: {col} — adding default value 0")
        df[col] = 0

# Step 3: Keep only expected columns (in correct order)
X_input = df[expected_features]

# Final check
print(f"✅ Input shape: {X_input.shape} — Scaler expects: {scaler.n_features_in_} features")

# Step 4: Scale and Predict
X_scaled = scaler.transform(X_input)
preds = model.predict(X_scaled)

# Map predictions to readable categories
label_map = {0: "Low", 1: "Medium", 2: "High"}
df["Predicted Category"] = [label_map[p] for p in preds]

# Save results
df.to_csv("startup_predictions.csv", index=False)
print("✅ Predictions saved to 'startup_predictions.csv'")

# Save feature importances
if hasattr(model, "feature_importances_"):
    feat_df = pd.DataFrame({
        "Feature": expected_features,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    feat_df.to_csv("feature_importance.csv", index=False)
    print("✅ Feature importance saved to 'feature_importance.csv'")
else:
    print("⚠️ Model does not support feature_importances_")
