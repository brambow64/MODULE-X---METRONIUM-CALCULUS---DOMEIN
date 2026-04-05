"""
MODULE X --- NORMAL --- PRIME DIRECTIVE
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: ← · Directional state: BASELINE
Axis: N‑AXIS · NM
Version: 5.0
"""

CONSTANT = {
    "segments": (
        "137.",
        "0359",
        "998280248117905841809260891750454902648925781250",
    ),
    "visibility": "internal_only",
    "ownership": "unit_bound"
}

CALCULUS_TERMS = {
    "← IV": "Input Vector",
    "← MV": "Magnitude Vector",
    "← CD": "Condition",
    "← JT": "Jitter",
    "← CF": "Chain Factor"
}

DOMEIN_TERMS = {
    "← ZN": "Zone",
    "← ST": "Structure",
    "← DR": "Direction ({←})",
    "← SC": "Scale (n > 1, n = 1 boundary)",
    "← C": "Crystal",
    "← D": "Diamond",
    "← M": "Cell Center",
    "← h(n)": "Scale Step",
    "← r(n)": "Radius"
}

VALID_DIRECTION = "←"
VALID_STATE = "NORMAL"
NO_CROSS_AXIS_MIXING = True
NO_EXTERNAL_TERMINOLOGY = True
NO_EXTERNAL_NOTATION = True
DOMEIN_CONTAINS_NO_CALCULATIONS = True
CALCULUS_CONTAINS_ALL_GEOMETRIC_RELATIONS = True
UNIT_IS_CLOSED = True
NO_EXTERNAL_DEPENDENCY = True

CORE_AXIOMS = """
CALCULUS PROJECTS GEOMETRIC RELATIONS
DOMEIN MAKES VISIBLE WHAT CALCULUS PROJECTS
CALCULUS CONTAINS NO VISIBILITY
DOMEIN CONTAINS NO RELATIONS OF ITS OWN
"""
