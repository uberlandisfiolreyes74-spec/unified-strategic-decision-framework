from sma03 import calculate_irreversibility
from msca_v6 import evaluate_options

def unified_decision(structural, beliefs, bio, fd, options):
    """
    Ejecuta el flujo completo del marco unificado.

    Retorna:
    - ii, risk_level, ranked_options
    """
    ii, risk = calculate_irreversibility(structural, beliefs, bio, fd)
    ranked = evaluate_options(options, ii)
    return ii, risk, ranked
