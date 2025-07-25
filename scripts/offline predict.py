import pandas as pd
import joblib

# ✅ Load trained model
model = joblib.load("best_startup_model.pkl")

df = pd.read_csv("Final-startup_success_predictions.csv")

print("📄 Columns found in the input CSV:")
print(df.columns.tolist())

# ✅ Load expected feature names (manually rebuilt if needed)
expected_features = joblib.load("input_columns.pkl")

# ✅ Remove irrelevant columns (left over from previous predictions or encoding)
columns_to_remove = ['Success Category_Low', 'Success Category_Medium', 'Success Category_High', 'Actual', 'Predicted', 'Predicted Category']
df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)

# ✅ Add any missing expected columns with default value (e.g., 0)
for col in expected_features:
    if col not in df.columns:
        print(f"⚠️ Missing column in input: {col} — adding default value 0")
        df[col] = 0

# ✅ Ensure correct order of features for model input
X_input = df[expected_features]

# ✅ Predict categories
preds = model.predict(X_input)

# ✅ Map numerical predictions to readable labels
label_map = {0: "Low", 1: "Medium", 2: "High"}
df["Predicted Category"] = [label_map[p] for p in preds]

# ✅ Save prediction results
df.to_csv("startup_predictions.csv", index=False)
print("✅ Predictions saved to 'startup_predictions.csv'")

importances = model.feature_importances_
columns = X_input.columns  # Use actual input column order

feat_df = pd.DataFrame({
    "Feature": columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

feat_df.to_csv("feature_importance.csv", index=False)
print("✅ Feature importance saved to 'feature_importance.csv'")