from flask import Flask, request, jsonify, render_template
import torch
import numpy as np
import joblib
from model import FFNN

app = Flask(__name__)

# Load model dan scaler
model = FFNN(input_dim=13, hidden_dim=64, output_dim=2)
model.load_state_dict(torch.load('FNN_UAP.pth'))
model.eval()
scaler = joblib.load("scaler2.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    # Parsing input data
    features = np.array([
        float(data['Age']),
        {'male': 0, 'female': 1, 'non-binary': 2}[data['Gender']],
        float(data['Income']),
        {'bachelor': 0, 'master': 1, 'high school': 2, 'doctorate': 3, 'others': 4}[data['Education_Level']],
        float(data['Travel_Frequency']),
        {'skiing': 0, 'swimming': 1, 'hiking': 2, 'sunbathing': 3, 'others': 4}[data['Preferred_Activities']],
        float(data['Vacation_Budget']),
        {'urban': 0, 'suburban': 1, 'rural': 2}[data['Location']],
        float(data['Proximity_to_Mountains']),
        float(data['Proximity_to_Beaches']),
        {'summer': 0, 'fall': 1, 'winter': 2, 'spring': 3}[data['Favorite_Season']],
        int(data['Pets']),
        int(data['Environmental_Concerns']),
    ]).reshape(1, -1)

    # Standardize features
    scaled_features = scaler.transform(features)

    # Predict using the model
    input_tensor = torch.tensor(scaled_features, dtype=torch.float32)
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)

    prediction = 'Beach' if predicted.item() == 0 else 'Mountain'
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
