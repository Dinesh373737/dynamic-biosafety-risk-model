# model/risk_scoring.py

def calculate_base_risk(normalized_inputs):
    """
    Calculates weighted biosafety risk score
    """

    weights = [
        0.25,  # R0
        0.20,  # CFR
        0.15,  # Transmission
        0.15,  # Mutation rate
        0.10,  # Host range
        0.10,  # Environmental stability
        0.05   # Countermeasures
    ]

    risk = sum(w * x for w, x in zip(weights, normalized_inputs))
    return risk


def apply_outbreak_stage_multiplier(risk, stage):
    """
    Adjusts risk based on outbreak stage
    """

    multipliers = {
        "emerging": 1.25,
        "peak": 1.15,
        "controlled": 0.85
    }

    return risk * multipliers.get(stage, 1.0)
