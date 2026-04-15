from flask import Flask, request, render_template
import numpy as np
import joblib

# Initialize Flask App
app = Flask(__name__)

# Load the scaler and label encoder
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')

# Load the models
models = {
    "Decision Tree": joblib.load('decision_tree.pkl'),
    "Random Forest": joblib.load('random_forest.pkl'),
    "SVM": joblib.load('svm.pkl'),
    "Logistic Regression": joblib.load('logistic_regression.pkl'),
    "KNN": joblib.load('knn.pkl')
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect all form inputs
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosphorus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    # Prepare input for prediction
    input_features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    scaled_input = scaler.transform(input_features)

    # Predict with all models
    predictions = {}
    for model_name, model in models.items():
        pred_label = model.predict(scaled_input)
        crop_name = le.inverse_transform(pred_label)[0]
        predictions[model_name] = crop_name

    return render_template('index.html', result=predictions)

if __name__ == '__main__':
    app.run(debug=True)
