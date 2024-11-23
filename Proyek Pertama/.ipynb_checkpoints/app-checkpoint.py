import pickle
from flask import Flask, request, jsonify
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model yang sudah disimpan
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('lr_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

with open('xgb_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

# Fungsi untuk prediksi
def predict(model, data):
    prediction = model.predict([data])
    return prediction[0]

@app.route('/predict', methods=['POST'])
def predict_model():
    # Ambil data dari request JSON
    data = request.get_json(force=True)
    features = data['features']  # Misalnya {"features": [val1, val2, val3, ...]}

    # Pilih model yang digunakan
    model_choice = data.get('model', 'rf')  # Default ke random forest
    
    if model_choice == 'rf':
        result = predict(rf_model, features)
    elif model_choice == 'lr':
        result = predict(lr_model, features)
    elif model_choice == 'xgb':
        result = predict(xgb_model, features)
    else:
        return jsonify({'error': 'Model not found'}), 404
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
