# 🚀 Startup Success Prediction Project

Welcome to the **Startup Success Prediction** project! This repository uses data analytics and ML concepts and showcases a machine learning pipeline to predict the success category of startups using structured data and features.

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
|   └── label_encoder.pkl
│
├── streamlit_app/              # Web app interface
│   ├── app.py
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
| Visualization     | Matplotlib, Seaborn                    |
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

```
---
---
## 🌐 Streamlit Web App

The Streamlit app provides a **multi-page, interactive dashboard** to explore startup data, visualize trends, and make predictions using a trained machine learning model.

---

### ▶️ To Run Locally:

```bash
cd streamlit_app
streamlit run app.py
```

---

## 📊 Streamlit Dashboard Overview

This interactive **3-page Streamlit dashboard** presents a complete view of startup success predictions using machine learning insights, business metrics, and industry trends.

---

### 🔹 Page 1: **Startup Overview & Success Analysis**
**Purpose:** High-level summary of the startup success landscape.  
**Key Features:**
- 📌 KPI Cards: Total Startups, Avg. Funding, Avg. Valuation, Total Acquisitions
- 🍩 Donut Chart: Distribution of predicted success categories
- 📊 Bar Chart: Funding Stage vs Predicted Success
- 🌲 Treemap: Industry-wise performance
- 🎯 Dynamic Filters: Country, Industry, and Funding Stage

---

### 🔹 Page 2: **Startup Profile & Geography**
**Purpose:** Deep dive into startup characteristics, global distribution, and financial indicators.  
**Key Features:**
- 🗺️ Geo Map: Country-wise startup distribution
- 🏭 Clustered Bar Chart: Industry-wise funding and count
- 🎯 Scatter Plot: Startup Age vs Valuation (colored by success level)
- 🔵 Bubble Chart: Employees, Revenue, Valuation correlation
- 🔎 Interactive Filters: Filter by geography and funding stage

---

### 🔹 Page 3: **Model Insights & Drill-Down**
**Purpose:** Understand ML model behavior and explore detailed predictions.  
**Key Features:**
- 📊 Bar Chart: Top feature importances influencing predictions
- 📋 Data Table: Scrollable, filterable view of the prediction dataset
- 🔍 Drillthrough: Row-level exploration of individual startup records

---

### ✅ Outcome

This dashboard empowers:

- 💡 **Founders** to assess where their startup stands  
- 💰 **Investors** to identify high-potential opportunities  
- 📊 **Analysts** to explore patterns and success drivers  

It serves as an accessible interface for real-time exploration, data filtering, and model-backed predictive insights in the startup ecosystem.


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
