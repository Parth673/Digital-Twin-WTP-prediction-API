from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import tensorflow as tf

# Constants----------------
R = 41.0  # rotor radius (m)
A = 5281.0  # swept area   (m^2)
gear = 106.0  # gear ratio
rho = 1.225  # air density  (kg/m^3)

# Load mode
# with open('model.pkl', 'rb') as file:
# model = pickle.load(file)
model = tf.keras.models.load_model('model.h5')


# Functions
def P_fromT(T, W):
    Pturbina = gear * T * W
    return Pturbina


app = Flask(__name__)


# Home--------
@app.route("/", methods=['GET'])
def home():
    return "Welcome to pratibhimb api"


# API---------
@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    turb = pd.json_normalize(data['unity'], meta = (['wind_speed'], ['pitch'], ['rpm']))
    # Metrices tras
    turb.iloc[:, 1] = turb.iloc[:, 1] * np.pi / 180.0
    turb.iloc[:, 2] = turb.iloc[:, 2] * 2 * np.pi / 60.0
    turb_norm = (turb - turb.mean()) / turb.std()
    turb_mean = np.nanmean(turb, axis=0)
    turb_std = np.nanstd(turb, axis=0)
    T_pred = model.predict(turb_norm).flatten()
    T_pred = T_pred * 7769.23 + 6244.07
    W_true = turb.iloc[:, 2]
    W_true = W_true.to_numpy()
    P_pred = P_fromT(T_pred, W_true) / 1000
    result = np.ndarray.tolist(P_pred.astype('float64'))
    dic = {"pow": result}

    return jsonify(dic)


if __name__ == "__main__":
    app.run(debug=True)
