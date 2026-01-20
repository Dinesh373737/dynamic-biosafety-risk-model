# model/normalization.py
import math

def normalize_inputs(data):
    """
    Normalizes all epidemiological parameters to 0–1 scale
    """

    R0_n = math.log(data["R0"]) / math.log(5)          # R0 normalization
    CFR_n = (data["CFR"] / 100) ** 0.5                 # CFR normalization
    T_n = data["transmission"] / 3                     # Transmission
    M_n = data["mutation_rate"]                        # Mutation rate
    H_n = data["host_range"] / 2                       # Host range
    E_n = data["env_stability"]                        # Environmental stability
    C_n = 1 - data["countermeasures"]                  # No countermeasure → higher risk

    return [R0_n, CFR_n, T_n, M_n, H_n, E_n, C_n]
