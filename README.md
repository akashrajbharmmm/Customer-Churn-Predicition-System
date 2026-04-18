# 📊 Customer Churn Prediction System

## 📌 Project Overview
This project is a Customer Churn Prediction System built using Logistic Regression.
It predicts whether a customer will churn (leave) or stay based on historical data.

---

## 🎯 Objective
- Identify customers at risk of leaving  
- Improve customer retention  
- Support business decision making  

---

## 🧠 Model Used
- Logistic Regression  
- Binary Classification (0 = Stay, 1 = Churn)  

---

## 📂 Dataset
The dataset contains:
- Gender
- Age
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method

---

## ⚙️ Workflow
1. Data Collection  
2. Data Preprocessing  
   - Handling missing values  
   - Encoding categorical variables  
3. Feature Selection  
4. Model Training (Logistic Regression)  
5. Model Evaluation  
6. Prediction  

---

## 📊 Model Performance

### Churn Distribution
Churn (1): 57%  
Not Churn (0): 43%  

### Classification Report
```
              precision    recall  f1-score   support

        0.0       0.85      0.93      0.89     47637
        1.0       0.94      0.87      0.91     62571

    accuracy                           0.90    110208
   macro avg       0.89      0.90      0.90    110208
weighted avg       0.90      0.90      0.90    110208
```

### Key Insights
- Accuracy: 90%  
- High precision for churn prediction (0.94)  
- Good recall (0.87)  
- Balanced performance  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  

---

## ▶️ How to Run

```
git clone <your-repo-link>
cd customer-churn-prediction
pip install -r requirements.txt
python main.py
```

---

## 📈 Output
- 0 → Customer will stay  
- 1 → Customer will churn  

---

## 🚀 Future Improvements
- Use advanced models (Random Forest, XGBoost)  
- Deploy using Streamlit / Flask  
- Add real-time prediction  

---

## 📌 Conclusion
Logistic Regression provides an effective and simple approach for predicting customer churn and helping businesses take proactive actions.

---

## 🙌 Author
Aakash Rajbhar
