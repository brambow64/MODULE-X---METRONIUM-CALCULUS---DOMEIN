"""
MODULE X --- EXIT READOUT LAYER
Status: EXTERNAL · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Version: 1.3
"""

CORE_PRINCIPLE = "RAW → READOUT → EXIT. EXIT emits JSON."

EXIT_JSON_TEMPLATE = {
    "report_id": "string",
    "axis": "NORMAL | ANTI | INVERSION | null",
    "axis_code": "100 | 001 | 100-010-001 | null",
    "entry": None,
    "terminal": None,
    "path_signature": "string | null",
    "state_signature": "string | null",
    "echo": "present | absent | null",
    "aperture": "present | absent | null",
    "aperture_configuration": "string | null",
    "layer_set": (),
    "completeness": "full | partial"
}

RULE = "All fields must exist. Missing data = null."

CONSTRAINTS = (
    "no interpretation",
    "no calculation",
    "no mutation"
)

CLOSURE = "Terminal output layer."
