"""
MODULE X --- SYMBOL BASE
Status: EXTERNAL · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Version: 1.2
"""

POSITION_IN_SYSTEM = """
This layer exists outside the core system.
It does not define or alter constant, calculus, geometric relations, field, domein.
It only makes visible structural states.
"""

CORE_PRINCIPLE = "The symbol base is a projection. It does not create structure. It marks structure."

SYMBOL_DEFINITION = "SYMBOL = AXIS + POSITION + STATE"

AXIS = {
    "←": "100 --- NORMAL",
    "→": "001 --- ANTI",
    "↔": "100-010-001 --- INVERSION"
}
AXIS_IS_FIXED_AND_IMMUTABLE = True

POSITIONS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
POSITION_HAS_NO_MEANING = True

STATE = {
    "•": "entry",
    "--": "passage",
    "∠": "angle-state",
    "◉": "center interaction",
    "×": "terminal",
    "↺": "cycle"
}
STATE_MARKS_STRUCTURAL_CONDITION_ONLY = True

CONSTRAINTS = (
    "Symbols do not define structure",
    "Symbols do not calculate",
    "Symbols do not interpret",
    "Symbols do not introduce relations"
)

CLOSURE = "Optional external layer."
