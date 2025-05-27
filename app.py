from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("mobile_price_predictor.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(request.form.get(f)) for f in [
        "battery_power", "blue", "clock_speed", "dual_sim", "fc", "four_g", "int_memory",
        "m_dep", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram",
        "sc_h", "sc_w", "talk_time", "three_g", "touch_screen", "wifi"
    ]]
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)[0]
    labels = ["Low", "Medium", "High", "Very High"]
    return render_template("index.html", prediction_text=f"Predicted Price Range: {labels[prediction]}")

if __name__ == "__main__":
    app.run(debug=True)
