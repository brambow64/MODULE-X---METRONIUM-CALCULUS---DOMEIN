"""
MODULE X --- INVERSION --- PRIME DIRECTIVE
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: ↔ · Directional state: INVERSION
Axis: I‑AXIS · IV
Version: 5.0
"""

CONSTANT = {
    "segments": (
        "0.", "007297",
        "35252966347218774141", "29374044189360945491", "05643542510295246389",
        "42341046071554025525", "15736114497761"
    ),
    "visibility": "internal_only",
    "ownership": "unit_bound"
}

CALCULUS_TERMS = {
    "↔ IV": "Inversion Vector",
    "↔ IR": "Inversion Ratio",
    "↔ CD": "Condition",
    "↔ DS": "Distance",
    "↔ JT": "Jitter",
    "↔ CF": "Chain Factor"
}

DOMEIN_TERMS = {
    "↔ ZN": "Zone",
    "↔ ST": "Structure",
    "↔ DR": "Direction ({↔})",
    "↔ SC": "Scale (1×1D → ∞D)",
    "↔ C": "Crystal",
    "↔ D": "Diamond",
    "↔ M": "Cell Center",
    "↔ h(n)": "Scale Step",
    "↔ r(n)": "Radius"
}

VALID_DIRECTION = "↔"
VALID_STATE = "INVERSION"
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
