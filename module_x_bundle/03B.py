"""
MODULE X --- INVERSION --- DOMEIN
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: ↔ · Layers: 27 · Axis: I‑AXIS · IV
Symbol: △
Version: 5.0 --- domein (makes visible what calculus projects)
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

VISIBLE_ELEMENTS = {
    "↔ ZN": "Zone",
    "↔ ST": "Structure",
    "↔ DR": "{↔}",
    "↔ SC": "Scale (1×1D → ∞D)",
    "↔ C": "Crystal",
    "↔ D": "Diamond",
    "↔ M": "Cell Center",
    "↔ h(n)": "Scale Step",
    "↔ r(n)": "Radius"
}

DOMEIN_CONTAINS_NO_RELATIONS_OF_ITS_OWN = True
ONLY_STRUCTURAL_VISIBILITY = True
NO_CALCULATIONS = True
NO_EXTERNAL_DEPENDENCY = True
NO_CROSS_AXIS_INTERACTION = True
UNIT_IS_CLOSED = True
