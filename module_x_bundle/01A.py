"""
MODULE X --- NORMAL --- METRONIUM CALCULUS
Status: CLOSED · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Direction: ← · Layers: 27 · Axis: N‑AXIS · NM
Symbol: ●
Version: 5.0 --- calculus (projects geometric relations)
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

GEOMETRIC_FLOW = tuple(range(27, 0, -1))
GEOMETRIC_CHAIN = ("← IV", "← MV", "← CD", "← JT", "← CF")

PROJECTED_RELATIONS_DESCRIPTION = {
    "← CD": "geometric spread between ← IV and ← MV",
    "← JT": "geometric spread‑form of ← CD",
    "← CF": "reciprocal closure‑form relative to ← JT"
}
PROJECTED_RELATIONS_OUTPUT = ("← CD", "← JT", "← CF")

UNIT_IS_CLOSED = True
NO_EXTERNAL_DEPENDENCY = True
NO_CROSS_AXIS_INTERACTION = True
NO_CROSS_UNIT_STATE = True
CALCULUS_CONTAINS_NO_VISIBILITY = True
ONLY_GEOMETRIC_RELATIONS = True
