# 🚀 Startup Success Prediction Project

Welcome to the **Startup Success Prediction** project! This repository showcases a full machine learning pipeline to predict the success category of startups using structured data and features.

---

## 📌 Problem Statement

In today’s competitive business landscape, understanding the key drivers of startup success is essential. This project focuses on predicting whether a startup will have **Low**, **Medium**, or **High** success using machine learning techniques.

---

## 🎯 Business Objective

- Identify the factors contributing to startup success.  
- Classify startups into success categories.  
- Empower stakeholders to make informed investment and strategy decisions.

---

## 🔍 Dataset Overview

- **Source:** Kaggle  
- **Filename:** `global_startup_success_dataset.csv`  
- **Target Variable:** `Success_Category` (Low, Medium, High)

### 🔑 Key Features:

- Total Funding  
- Revenue  
- Valuation  
- Customer Base  
- Country, Industry  
- Funding Stage  
- Social Media Metrics

---

## 🧱 Project Architecture

```bash
Startup_Success_Prediction/
│
├── data/                       # Input & output datasets
│   ├── global_startup_success_dataset.csv
│   ├── Final-startup_success_predictions.csv
│   ├── startup_predictions-offline.csv
│   └── feature_importance.csv
│
├── model/                      # Trained model files
│   ├── best_startup_model.pkl
│   └── input_columns.pkl
│
├── dashboard/                  # Power BI dashboard file
│   └── startup dashboard.pbix
│
├── streamlit_app/              # Web app interface
│   ├── app.py
│   └── .streamlit/config.toml
│
├── notebooks/                  # Jupyter notebook
│   └── startup.ipynb
│
├── offline predict.py          # Script for batch prediction
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignored files
└── README.md                   # Project documentation
```

---

## 🧪 Tools & Technologies Used

| Category           | Tools/Libraries                        |
|-------------------|----------------------------------------|
| Data Manipulation | Pandas, NumPy                          |
| Visualization     | Matplotlib, Seaborn, Power BI          |
| Machine Learning  | Scikit-learn, Random Forest, SVM, etc. |
| Deployment        | Streamlit                              |
| Model Persistence | Pickle, Joblib                         |

---

## 🔁 End-to-End Workflow

- 📂 Data Preprocessing and Cleaning  
- 📊 Exploratory Data Analysis (EDA)  
- ⚙️ Feature Engineering  
- 🧠 Model Training and Evaluation  
- 💾 Save Trained Model using Pickle  
- 🌐 Streamlit App for Online Prediction  
- 📈 Power BI Dashboard for Visualization  

---

## 📊 Power BI Dashboard

Power BI provides dynamic and filterable dashboards to interactively explore the predictions:

- Industry-wise success distribution  
- Country-wise startup funding analysis  
- Key metrics like revenue, customer base, and success impact  

📌 Open `startup dashboard.pbix` in Power BI Desktop.

---

## 🌐 Streamlit Web App

The Streamlit app provides an interactive form for online predictions.

### ▶️ To Run Locally:

```bash
cd streamlit_app
streamlit run app.py
```

---

## 🔧 Installation Guide

### 🛠️ Install Requirements:

```bash
pip install -r requirements.txt
```

**Dependencies include:**

- pandas, numpy  
- scikit-learn  
- matplotlib, seaborn  
- streamlit  
- pickle, joblib

---

## 🧼 .gitignore Sample

```text
*.pkl
*.pbix
__pycache__/
.ipynb_checkpoints/
.env
.DS_Store
```

---

## 🔮 Future Enhancements

- Build a live data ingestion pipeline  
- Deploy on Streamlit Cloud or HuggingFace Spaces  
- Automate retraining with newer data  

---

## 🙋‍♀️ About Me

**👩‍💻 Ayushi Kedia**  
📧 Email: [ayushikedia0209@gmail.com](mailto:ayushikedia0209@gmail.com)  
🔗 GitHub: [@Ayu0209](https://github.com/Ayu0209)

---

## ⭐ Show Some ❤️

If you liked this project, please give it a ⭐ on GitHub!

Thank you for visiting! 🎉
