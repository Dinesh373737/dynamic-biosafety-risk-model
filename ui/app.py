from flask import Flask, render_template, request, jsonify

from model.normalization import normalize_inputs
from model.risk_scoring import calculate_base_risk, apply_outbreak_stage_multiplier
from model.bsl_mapping import map_risk_to_bsl

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    normalized = normalize_inputs(data)
    risk = calculate_base_risk(normalized)
    risk = apply_outbreak_stage_multiplier(risk, data["stage"])
    score, bsl = map_risk_to_bsl(risk)

    return jsonify({
        "risk_score": round(score, 2),
        "bsl": bsl
    })

if __name__ == "__main__":
    app.run(debug=True)
