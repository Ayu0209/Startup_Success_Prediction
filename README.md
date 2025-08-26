# 🚀 Startup Success Prediction Project

Welcome to the **Startup Success Prediction** project! This repository uses data analytics and ML concepts and showcases a machine learning pipeline to predict the success category of startups using structured data and features.

---

## 📑 Table of Contents  
1. [Overview](#overview)
2. [Live Demo](#Live Demo)
3. [Business Problem](#business-problem)  
4. [Dataset](#dataset)  
5. [Tools and Technologies](#tools-and-technologies)  
6. [Project Structure](#project-structure)  
7. [Data Cleaning & Preparation](#data-cleaning--preparation)  
8. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
9. [Research Questions & Key Findings](#research-questions--key-findings)  
10. [Dashboard/Model](#dashboardmodel)  
11. [How to Run this Project?](#how-to-run-this-project)  
12. [Results & Conclusion](#results--conclusion)  
13. [Future Work](#future-work)  
14. [Author & Contact](#author--contact)  

---

## 📌 Overview

In today’s competitive business landscape, Startups face high uncertainty, and predicting their chances of success can support investors, founders, and policymakers in making informed decisions. This project leverages machine learning techniques to predict whether a startup will have **Low**, **Medium**, or **High** success using machine learning techniques.

---
## 🔗 Live Demo
https://startupsuccessprediction-aczujymxdib2wdxu2fkto2.streamlit.app/

---

## 🎯 Business Problem  
- Investors often struggle to identify high-potential startups.  
- Founders lack data-driven insights for decision-making.  
- Policymakers aim to support successful ecosystems but face uncertainty.  

**Goal** → Build a machine learning model that can **predict startup success probability** and provide insights into the key factors influencing outcomes. 

---

## 🔍 Dataset Overview

- **Source:** Kaggle  
- **Filename:** `global_startup_success_dataset.csv`  
- **Target Variable:** `Success_Category` (Low, Medium, High)

---

## 🧱 Project Architecture

```bash
Startup_Success_Prediction/
│
├── data/                                   # Datasets used for training & prediction
│ ├── global_startup_success_dataset.csv         # Original dataset of global startups
│ ├── feature_importance.csv                     # Feature importance scores from the model
│ ├── startup_predictions-offline.csv            # Offline prediction dataset for testing
│ └── Final-startup_success_predictions.csv      # Final dataset with model predictions
│
├── model/                                  # Saved ML model artifacts
│ ├── best_startup_model.pkl                     # Trained ML model (best version)
│ ├── input_columns.pkl                          # Stores input feature columns
│ ├── label_encoder.pkl                          # Encodes categorical variables
│ └── scaler.pkl                                 # Data scaler for preprocessing
│
├── notebook/                               # Jupyter notebooks for analysis & modeling
│ └── startup.ipynb                               # Main notebook (EDA + model training)
│
├── script/                                 # Python scripts for predictions
│ └── offline predict.py                          # Script to test predictions offline
│
├── app.py                                  # Streamlit app for interactive predictions
├── requirements.txt                        # Required Python dependencies
├── README.md                               # Project documentation
└── .gitignore                              # Ignored files & folders (cache, venv, etc.)
```

---

## 🧪 Tools & Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn, XGBoost)  
- **Jupyter Notebook** (Exploration & EDA)  
- **Pickle** (Model Saving)  
- **Streamlit** (Deployment with `app.py`)  
- **Visualization** (Matplotlib, Seaborn, Plotly) 
---

## 🧹 Data Cleaning & Preparation  
- Handled missing values and categorical encoding.  
- Standardized and scaled numerical features.  
- Applied label encoding for categorical outputs.  
- Balanced the dataset using oversampling techniques.  

---

## 📊 Exploratory Data Analysis (EDA)  
- Distribution of successful vs failed startups.  
- Funding patterns by geography and industry.  
- Feature importance analysis to identify key predictors.  

---

## ❓ Research Questions & Key Findings  
- Which industries show the highest success rate?  
- Does geography influence startup outcomes?  
- How does funding impact the probability of success?  
- **Finding**: Funding, location, and sector significantly influence startup success.  

## 🌐 Streamlit Web App

- The Streamlit app provides a **multi-page, interactive dashboard** to explore startup data, visualize trends, and make predictions using a trained machine learning model.
- ML models compared: Logistic Regression, Random Forest, XGBoost.  
- Best model saved in `model/best_startup_model.pkl`.  
- Feature importance stored in `feature_importance.csv`.  
- Interactive prediction via `app.py`.  

---

### ▶️ To Run Locally:

```bash
cd streamlit_app
streamlit run app.py
```

---

## 📊 Streamlit Dashboard Overview

This interactive **4-page Streamlit dashboard** presents a complete view of startup success predictions using machine learning insights, business metrics, and industry trends.

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

### 🔹 Page 4: **Startup Growth Success Score Predictor**
**Purpose:** Provide an interactive prediction tool where users can input startup details and instantly receive a success score/category.
**Key Features:**
- 📝 Input Form: Users enter details such as funding, revenue, valuation, employees, age, industry, and geography.
- ⚡ Real-Time Prediction: ML model predicts the probability of success and assigns a success category (e.g., High, Medium, Low).
- 🎨 User-Friendly UI: Intuitive sliders, dropdowns, and numeric fields for quick data entry.
- 🔍 Scenario Testing: Founders, investors, or analysts can simulate different funding/revenue levels and test success probabilities.


---

## 🏃 How to Run this Project?  
1. Clone the repository  
   ```bash
   git clone https://github.com/Ayu0209/Startup_Success_Prediction.git
   cd Startup_Success_Prediction
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application  
   ```bash
   python app.py
   ```
4. Use the UI to input startup details and get predictions.  

---

## ✅ Results & Conclusion  
- Built a machine learning pipeline to predict startup success.  
- Achieved good accuracy using **XGBoost** with well-defined features.  
- Identified key factors influencing success: **Funding Amount, Geography, and Industry Sector**.
- This dashboard empowers:
     💡 **Founders** to assess where their startup stands  
     💰 **Investors** to identify high-potential opportunities  
     📊 **Analysts** to explore patterns and success drivers  

---

## 🔮 Future Work  
- Extend dataset with real-time startup data.  
- Deploy as a web dashboard with Power BI integration.  
- Incorporate additional features like team size, patents, and partnerships.  

---

## 👤 Author & Contact  
**Ayushi Kedia**  
📧 Email: ayushikediahm@gmail.com    
🔗 [LinkedIn](https://www.linkedin.com/in/ayushi-kedia-81bb7520b/)  

---

## ⭐ Show Some ❤️

If you liked this project, please give it a ⭐ on GitHub!

Thank you for visiting! 🎉
