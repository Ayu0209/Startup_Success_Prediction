🚀 Startup Success Prediction Project

Welcome to the Startup Success Prediction repository! This project uses machine learning and data analytics to predict the success category of a startup using structured features like funding, revenue, age, country, and more. This includes a full pipeline from data cleaning to model deployment, with both an interactive Streamlit app and a detailed Power BI dashboard.

📌 Problem Statement

In today’s competitive environment, predicting the success of a startup is a complex and critical task. By leveraging machine learning, we aim to automate the classification of startups into categories — Low, Medium, or High success — to support investors, analysts, and entrepreneurs in making informed decisions.

🎯 Business Goals

Analyze global startup data to identify key factors contributing to success.

Build a robust machine learning model that can predict the success category.

Provide offline and online prediction options for real-world usability.

Create visual insights using Power BI.

🗂️ Project Structure

Startup_Success_Prediction/
│
├── 📁 data/
│   ├── global_startup_success_dataset.csv     # Raw dataset from Kaggle
│   ├── Final-startup_success_predictions.csv  # Cleaned and feature-engineered data
│   ├── startup_predictions-offline.csv        # Output of offline predictions
│   ├── feature_importance.csv                 # Feature importance results
│
├── 📁 model/
│   ├── best_startup_model.pkl                 # Trained ML model
│   ├── input_columns.pkl                      # Feature names used during training
│
├── 📁 dashboard/
│   └── startup dashboard.pbix                 # Power BI Dashboard
│
├── 📁 streamlit_app/
│   ├── app.py                                 # Streamlit app for online prediction
│   └── .streamlit/config.toml                 # Custom theming configuration
│
├── 📁 notebooks/
│   └── startup.ipynb                          # EDA, training & evaluation notebook
│
├── offline predict.py                        # Python script for offline prediction
├── requirements.txt                          # All dependencies used in the project
├── .gitignore                                 # Files and folders to ignore in Git
└── README.md                                  # You are here 🚀

📊 Dataset Overview

Source: Kaggle — global_startup_success_dataset.csv

Records global startups with features like:

Total Funding, Revenue, Valuation

Customer Base, Social Media, Tech Stack

Country, Industry, Funding Stage

Target: Success Category (Low, Medium, High)

🔁 Workflow Summary

Data Cleaning & Preprocessing (startup.ipynb)

EDA & Feature Engineering

Model Building & Evaluation (Random Forest, SVM, Logistic Regression, etc.)

Saving Best Model (best_startup_model.pkl + input_columns.pkl)

Offline Prediction via script

Online Prediction via Streamlit

Visualization using Power BI Dashboard

💡 Key Features

Clean ML pipeline

Model: Random Forest Classifier

Accuracy: ~85% on validation data

Offline/Batch prediction ready

Streamlit app with custom theme

Power BI dashboard with key metrics and filters

▶️ Running the Streamlit App

cd streamlit_app
streamlit run app.py

📈 Power BI Dashboard

Open startup dashboard.pbix in Power BI Desktop.

Explore success predictions, filter by country/industry/funding stage, and visualize feature impact.

🔧 Requirements

Install dependencies using:

pip install -r requirements.txt

🧼 .gitignore Highlights

*.pkl
*.pbix
__pycache__/
.ipynb_checkpoints/
.env

📌 Future Scope

Model retraining pipeline

Web scraping to fetch live startup data

Deploy with Docker or HuggingFace Spaces

🙌 Acknowledgements

Kaggle for the dataset

Streamlit for app framework




## 🗂️ Project Overview

| Area              | Details |
|-------------------|---------|
| 📁 Dataset        | [Global Startup Success Dataset (Kaggle)](https://www.kaggle.com/) |
| 🛠️ Techniques     | EDA, Label Encoding, Feature Importance, Model Training |
| 🤖 Models Used    | Logistic Regression, Random Forest, SVM, Naive Bayes |

---

## 📁 Folder Structure

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
