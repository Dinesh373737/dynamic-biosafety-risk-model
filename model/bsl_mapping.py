# model/bsl_mapping.py

def map_risk_to_bsl(risk):
    """
    Maps final risk score to Biosafety Level
    """

    score = min(risk * 100, 100)

    if score < 30:
        return score, "BSL-2"
    elif score < 55:
        return score, "BSL-2+"
    elif score < 80:
        return score, "BSL-3"
    else:
        return score, "BSL-3+"
