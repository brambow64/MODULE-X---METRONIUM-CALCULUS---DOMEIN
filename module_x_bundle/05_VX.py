"""
MODULE X --- VISUAL EXPORT LAYER
Code: 05-VX
Status: EXTERNAL · VISUAL_ONLY · NO INTERPRETATION · NO CALCULATION
Dependency: 04-EX
Position: AFTER EXIT
Version: 1.2
"""

CORE_PRINCIPLE = "Post-exit renderer. Consumes Ξ and emits visual file."

OUTPUT_FILE_PATTERN = "MX-XXXX.visual.txt"
OUTPUT_CONTAINS_SYMBOLS_ONLY = True

RENDERING_RULE = "AXIS + POSITION + STATE"

VOLUMETRIC_ORIENTATION = {
    "◐": "left",
    "◑": "right",
    "◒": "bottom",
    "◓": "top"
}
VOLUMETRIC_ORIENTATION_DOES_NOT_ALTER_STRUCTURAL_STATE = True

COMBINATION_RULES = {
    "order": ("left", "right", "bottom", "top"),
    "examples": ("◐◑", "◐◑◒")
}

CONSTRAINTS = (
    "no structure change",
    "no interpretation",
    "no feedback"
)

CLOSURE = "Final layer."
