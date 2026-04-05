"""
MODULE X --- ANTI --- DOMEIN
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: → · Layers: 27 · Axis: A‑AXIS · AT
Symbol: □
Version: 5.0 --- domein (makes visible what calculus projects)
"""

CONSTANT = {
    "segments": (
        "-137.",
        "0359",
        "998280248117905841809260891750454902648925781250",
    ),
    "visibility": "internal_only",
    "ownership": "unit_bound"
}

VISIBLE_ELEMENTS = {
    "→ ZN": "Zone",
    "→ ST": "Structure",
    "→ DR": "{→}",
    "→ SC": "Scale (n > 1, n = 1 boundary)",
    "→ C": "Crystal",
    "→ D": "Diamond",
    "→ M": "Cell Center",
    "→ h(n)": "Scale Step",
    "→ r(n)": "Radius"
}

DOMEIN_CONTAINS_NO_RELATIONS_OF_ITS_OWN = True
ONLY_STRUCTURAL_VISIBILITY = True
NO_CALCULATIONS = True
NO_EXTERNAL_DEPENDENCY = True
NO_CROSS_AXIS_INTERACTION = True
