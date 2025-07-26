# 🚀 Startup Success Prediction using Public Data

This project uses machine learning models to predict the **success category** (Low, Medium, High) of a startup based on key business and funding factors. It includes complete steps from data cleaning to model deployment, as well as an interactive **Power BI dashboard**.

---

## 📂 Project Structure

```bash
Startup_Success_Prediction/
├── 📁 data/                     # Cleaned and raw datasets
│   ├── global_startup_success_dataset.csv
│   ├── Final-startup_success_predictions.csv
│   └── startup_predictions-offline.csv
│
├── 📁 model/                    # Trained models and encoders
│   ├── best_startup_model.pkl
│   └── input_columns.pkl
|   ├──label_encoder.pkl
│
├── 📁 streamlit_app/            # Streamlit UI
│   └── app.py
│
├── startup.ipynb               # Main notebook (EDA + modeling)
├── offline predict.py          # Offline prediction script
├── feature_importance.csv      # Feature ranking from model
├── requirements.txt            # Required libraries
├── .gitignore
└── README.md
