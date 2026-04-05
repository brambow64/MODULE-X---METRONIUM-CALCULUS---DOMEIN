"""
MODULE X --- HEXAGONAL APERTURE
Status: EXTERNAL · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Dependency: 04-01
Optional: 04-02, 04-03, 04-04
Position: OUTSIDE CLOSED SYSTEM
Version: 1.2
"""

CORE_PRINCIPLE = """
The hexagon is a structural aperture.
It reveals the geometric configuration of the three axis signals.
It does not create, alter, or distribute structure.
"""

APERTURE = {"H": ("S1", "S2", "S3", "S4", "S5", "S6")}

PROJECTION = {
    "←": ("S1", "S2"),
    "→": ("S3", "S4"),
    "↔": ("S5", "S6")
}

OUTPUT_STRUCTURE = {
    "aperture": "hexagon",
    "axis_presence": {
        "←": ("S1", "S2"),
        "→": ("S3", "S4"),
        "↔": ("S5", "S6")
    },
    "signature_value": "S1S2|S3S4|S5S6",
    "completeness": "full | partial"
}

VISIBILITY = (
    "spatial relation of axes",
    "adjacency",
    "separation",
    "configuration form"
)

CONSTRAINTS = (
    "no mutation",
    "no interpretation",
    "no feedback",
    "no calculation"
)

RULE = "The aperture reveals --- it does not define."
CLOSURE = "Optional."
