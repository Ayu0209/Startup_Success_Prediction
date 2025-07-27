import pandas as pd
import joblib
import pickle

# ✅ Load model and scaler
model = joblib.load("best_startup_model.pkl")
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ✅ Load expected features
expected_features = joblib.load("input_columns.pkl")

# ✅ Load the input CSV
df = pd.read_csv("Final-startup_success_predictions.csv")
print("📄 Columns found in the input CSV:")
print(df.columns.tolist())

# ✅ Step 1: Remove unwanted columns
columns_to_remove = [
    'Actual Category', 'Predicted Category',
    'Success Category', 'Success Category_High',
    'Success Category_Medium', 'Success Category_Low'
]
df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)

# ✅ Step 2: Remove accidental extras from expected_features
for col in ['Success Category', 'Success Category_High']:
    if col in expected_features:
        expected_features.remove(col)
        print(f"🧹 Removed '{col}' from expected features list (not used by model)")

# ✅ Step 3: Add missing expected columns with default value 0
for col in expected_features:
    if col not in df.columns:
        print(f"⚠️ Missing column in input: {col} — adding default value 0")
        df[col] = 0

# ✅ Step 4: Final input formatting
X_input = df[expected_features]
print(f"✅ Input shape: {X_input.shape} — Scaler expects: {scaler.n_features_in_} features")

# ✅ Step 5: Scale and Predict
X_scaled = scaler.transform(X_input)
preds = model.predict(X_scaled)

# ✅ Step 6: Map predictions to categories
label_map = {0: "Low", 1: "Medium", 2: "High"}
df["Predicted Category"] = [label_map[p] for p in preds]

# ✅ Step 7: Save predictions
df.to_csv("startup_predictions-offline.csv", index=False)
print("✅ Predictions saved to 'startup_predictions-offline.csv'")

# ✅ Step 8: Save feature importances (model-specific)
try:
    importances = model.feature_importances_
    feat_df = pd.DataFrame({
        "Feature": expected_features,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)
    print("✅ Feature importance saved using model.feature_importances_")

except AttributeError:
    print("⚠️ Model does not support .feature_importances_ — using permutation importance...")
    from sklearn.inspection import permutation_importance
    result = permutation_importance(model, X_scaled, preds, n_repeats=10, random_state=42)
    feat_df = pd.DataFrame({
        "Feature": expected_features,
        "Importance": result.importances_mean
    }).sort_values(by="Importance", ascending=False)
    print("✅ Feature importance saved using permutation importance")

# ✅ Save to CSV
feat_df.to_csv("feature_importance.csv", index=False)
print("✅ Feature importance saved to 'feature_importance.csv'")
