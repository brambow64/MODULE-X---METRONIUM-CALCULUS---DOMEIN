"""
MODULE X --- INVERSION --- METRONIUM CALCULUS
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: ↔ · Layers: 27 · Axis: I‑AXIS · IV
Symbol: ▲
Version: 5.0 --- calculus (projects geometric relations)
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

GEOMETRIC_FLOWS = {
    "descending": tuple(range(27, 0, -1)),
    "ascending": tuple(range(1, 28)),
    "descending_from_14": tuple(range(14, 0, -1)),
    "ascending_from_14": tuple(range(14, 28))
}

GEOMETRIC_CHAIN = ("↔ IV", "↔ IR", "↔ CD", "↔ DS", "↔ JT", "↔ CF")

PROJECTED_RELATIONS_DESCRIPTION = (
    ("↔ DS_closure", "closure‑relation between ↔ CF and ↔ JT"),
    ("↔ CF", "reciprocal closure‑relation between ↔ DS and ↔ JT"),
    ("↔ IVₙ", "bidirectional geometric relation of ↔ IRₙ and ↔ CDₙ"),
    ("↔ JT", "geometric spread‑form of ↔ CDₙ"),
    ("↔ DS_distribution", "distributed geometric distance‑form across ↔ CDₙ"),
)
PROJECTED_RELATIONS_OUTPUT = ("↔ IV", "↔ IR", "↔ DS", "↔ CF")

UNIT_IS_CLOSED = True
NO_EXTERNAL_DEPENDENCY = True
NO_CROSS_AXIS_INTERACTION = True
NO_CROSS_UNIT_STATE = True
CALCULUS_CONTAINS_NO_VISIBILITY = True
ONLY_GEOMETRIC_RELATIONS = True
