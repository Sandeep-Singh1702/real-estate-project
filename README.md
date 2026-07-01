# 🏠Property Vision : Real Estate Data Science Application

A comprehensive end-to-end Data Science project that provides property price prediction, analytics, and recommendation systems for the real estate domain. The application leverages machine learning, data visualization, and recommendation engines to help users make informed real estate decisions.

## 🚀 Features

### 📊 Property Price Prediction
- Predicts property prices using Machine Learning models.
- Supports various property attributes and features.
- Interactive prediction interface built with Streamlit.

### 📈 Analytics Dashboard
- Geographical visualizations and maps.
- Property distribution analysis.
- Amenities word clouds.
- Scatter plots, pie charts, and box plots.
- Market trend insights.

### 🎯 Recommendation System
- Facility-based recommendations.
- Price-based recommendations.
- Location-based recommendations.
- Personalized property suggestions.

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- SHAP

### Cloud Platform
- AWS (Amazon Web Services)

## 📂 Project Workflow

### 1. Data Collection
- Real estate data scraped from 99acres and other property listing websites.

### 2. Data Cleaning
- Handling missing values.
- Data consistency checks.
- Dataset merging.

### 3. Feature Engineering
- Additional room indicators.
- Area specifications.
- Age of possession.
- Furnishing details.
- Luxury score generation.

### 4. Exploratory Data Analysis (EDA)
- Univariate analysis.
- Multivariate analysis.
- Data profiling and visualization.

### 5. Data Preprocessing
- Outlier detection and removal.
- Missing value imputation.
- Feature transformation.

### 6. Feature Selection
Techniques used:
- Correlation Analysis
- Random Forest Importance
- Gradient Boosting Importance
- Permutation Importance
- LASSO
- Recursive Feature Elimination (RFE)
- SHAP (Explainable AI)

### 7. Machine Learning Models Evaluated
- Linear Regression
- Support Vector Regression (SVR)
- Random Forest Regressor
- Multi-layer Perceptron (MLP)
- LASSO Regression
- Ridge Regression
- Gradient Boosting Regressor
- Decision Tree Regressor
- K-Nearest Neighbors Regressor
- ElasticNet Regression

### 8. Model Deployment
- Selected best-performing model.
- Built prediction pipeline.
- Deployed using Streamlit.

### 9. AWS Deployment
- Hosted the complete application on AWS.
- Ensured scalability and accessibility.

## 📸 Application Modules

### Price Prediction Module
Predicts property prices based on user inputs.

### Analytics Module
Provides visual insights into the real estate market.

### Recommendation Module
Suggests properties based on:
- Facilities
- Price
- Location

## 📁 Project Structure

```bash
├── data/
├── notebooks/
├── models/
├── app/
├── recommender/
├── analytics/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/your-username/your-repository.git

cd your-repository

pip install -r requirements.txt

streamlit run streamlit_app.py
```

## 🎯 Objectives

- Build an accurate real estate price prediction system.
- Generate actionable market insights through analytics.
- Provide personalized property recommendations.
- Deploy a production-ready application on AWS.

## 📌 Future Enhancements

- Real-time property data integration.
- Advanced recommendation engine.
- User authentication and profiles.
- Market trend forecasting.
- Mobile-responsive interface.

## 👨‍💻 Author

Developed as a Data Science Capstone Project focused on solving real-world problems in the real estate industry.

---
⭐ If you found this project useful, consider giving it a star on GitHub.
