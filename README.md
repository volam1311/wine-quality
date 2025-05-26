# 🍷 Wine Quality Prediction - End-to-End ML Project

This project aims to build an end-to-end machine learning pipeline to predict wine quality based on various physicochemical features. It includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment via a simple web app.

---

## 📊 Problem Statement

Given a dataset of red or white wines with several physicochemical properties (like acidity, pH, and alcohol), the goal is to predict the wine quality score assigned by wine tasters.

---

## ⚙️ Technologies Used

- Python 3.12.7  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Elasticnet  
- Flask
- Joblib

---

## 📥 Dataset

The dataset is publicly available from the UCI Machine Learning Repository:  
🔗 https://archive.ics.uci.edu/ml/datasets/Wine+Quality

You can download either the red or white wine dataset (or both).

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/wine-quality-prediction.git
cd wine-quality-prediction
```
2. Create and activate a virtual environme
```bash
python -m venv venv

source venv/bin/activate

 # On Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run Jupyter notebooks for EDA and training
Navigate to the notebooks/ folder and open:
``` bash
01_EDA.ipynb: For exploring and understanding the data

02_Model_Training.ipynb: For training and evaluating the models
```
5. Run the web app
If using Flask:
```bash
cd app
python app.py
```
Visit http://127.0.0.1:8080
