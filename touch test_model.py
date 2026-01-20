from model.normalization import normalize_inputs
from model.risk_scoring import calculate_base_risk, apply_outbreak_stage_multiplier
from model.bsl_mapping import map_risk_to_bsl

sample_input = {
    "R0": 2.5,
    "CFR": 3,
    "transmission": 2,
    "mutation_rate": 0.2,
    "host_range": 1,
    "env_stability": 0.3,
    "countermeasures": 0,
    "stage": "emerging"
}

norm = normalize_inputs(sample_input)
risk = calculate_base_risk(norm)
risk = apply_outbreak_stage_multiplier(risk, sample_input["stage"])
score, bsl = map_risk_to_bsl(risk)

print("Risk Score:", round(score, 2))
print("Predicted BSL:", bsl)
