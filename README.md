# 🚀 Startup Success Prediction using Public Data

<div align="center">
  <img src="https://github.com/Ayu0209/Startup_Success_Prediction/assets/your-banner-path/banner.png" alt="Startup Success Prediction" width="800"/>
</div>

<h2 align="center">📊 Startup Success Prediction Using Machine Learning</h2>

<p align="center">
  A full end-to-end machine learning project to predict the success level of startups using classification models.
</p>

---

## 🧠 Objective

Predict whether a startup will be **Low**, **Medium**, or **High** success based on its features like industry, location, funding stage, and more.

---

## 🗂️ Project Overview

| Area              | Details |
|-------------------|---------|
| 📁 Dataset        | [Global Startup Success Dataset (Kaggle)](https://www.kaggle.com/) |
| 🛠️ Techniques     | EDA, Label Encoding, Feature Importance, Model Training |
| 🤖 Models Used    | Logistic Regression, Random Forest, SVM, Naive Bayes |
| 📈 Dashboard Tool | Power BI |
| 🖥 Deployment     | Offline Prediction Script / Streamlit-ready |

---

## 📁 Folder Structure

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
