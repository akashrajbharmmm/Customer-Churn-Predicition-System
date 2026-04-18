from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

pipeline = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))  # ← NEW

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Raw DataFrame banao — np.array nahi!
        raw = {
            'Age':              float(data['age']),
            'Gender':           data['gender'],          # string 'Male'/'Female'
            'Tenure':           float(data['tenure']),
            'Usage Frequency':  float(data['usage_frequency']),
            'Support Calls':    float(data['support_calls']),
            'Payment Delay':    float(data['payment_delay']),
            'Total Spend':      float(data['total_spend']),
            'Last Interaction': float(data['last_interaction']),
            'Subscription Type': data['subscription_type'],
            'Contract Length':   data['contract_length']
        }

        df_in = pd.DataFrame([raw])

        # Wahi encoding jo training mein thi
        df_in['Gender'] = df_in['Gender'].map({'Male': 1, 'Female': 0})
        df_in = pd.get_dummies(df_in, columns=['Subscription Type','Contract Length'], drop_first=True)

        # Missing columns 0 se fill karo
        for col in model_columns:
            if col not in df_in.columns:
                df_in[col] = 0

        # Exact same order
        df_in = df_in[model_columns]

        prediction = pipeline.predict(df_in)[0]
        probability = round(float(pipeline.predict_proba(df_in)[0][1]) * 100, 2)

        return jsonify({
            "churn": int(prediction),
            "churn_label": "Will Churn" if int(prediction) == 1 else "Will Not Churn",
            "probability": probability
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)