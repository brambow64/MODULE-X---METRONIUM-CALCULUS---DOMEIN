"""
MODULE X --- PROJECT README
Status: DECLARATIVE · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: PROJECT OVERVIEW
"""

PROJECT_NAME = "MODULE X — METRONIUM CALCULUS & DOMEIN"

STATUS = (
    "CLOSED",
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

DESCRIPTION = """
This project contains the declarative Python specification of Module X.

The files define:
- constitutional rules
- directional units
- calculus units
- domein units
- observation layers
- export layers
- closure layer

No file performs calculation.
No file performs interpretation.
No file contains hidden runtime logic.
"""

PROJECT_STRUCTURE = (
    "module_x_clean/",
    "README.py",
    "00.py",
    "01.py",
    "01A.py",
    "01B.py",
    "02.py",
    "02A.py",
    "02B.py",
    "03.py",
    "03A.py",
    "03B.py",
    "04_01.py",
    "04_02.py",
    "04_03.py",
    "04_04.py",
    "04_05.py",
    "04_EX.py",
    "05_VX.py",
    "06_EM.py",
    "07_CL.py",
)

NO_SUBFOLDERS_REQUIRED = True

CORE_FILES = (
    ("00.py", "Global Constitution"),
    ("01.py", "Normal Prime Directive"),
    ("01A.py", "Normal Metronium Calculus"),
    ("01B.py", "Normal Domein"),
    ("02.py", "Anti Prime Directive"),
    ("02A.py", "Anti Metronium Calculus"),
    ("02B.py", "Anti Domein"),
    ("03.py", "Inversion Prime Directive"),
    ("03A.py", "Inversion Metronium Calculus"),
    ("03B.py", "Inversion Domein"),
)

OBSERVATION_FILES = (
    ("04_01.py", "Symbol Base"),
    ("04_02.py", "Live Observation"),
    ("04_03.py", "Circular Projection"),
    ("04_04.py", "Structural Echo"),
    ("04_05.py", "Hexagonal Aperture"),
    ("04_EX.py", "Exit Readout Layer"),
)

EXPORT_AND_TERMINAL_FILES = (
    ("05_VX.py", "Visual Export Layer"),
    ("06_EM.py", "Emergent Pattern Projection"),
    ("07_CL.py", "Closure Layer"),
)

CONSTANT_POLICY = {
    "structure": (
        "CONSTANT",
        "segments",
        "visibility",
        "ownership",
    ),
    "visibility": "internal_only",
    "ownership": "unit_bound",
    "plain_text_exposure": False,
    "calculation_used": False,
}

SYSTEM_RULES = (
    "no global shared constant",
    "no cross-axis mixing",
    "no interpretation",
    "no calculation",
    "no mutation of structural meaning",
    "no hidden execution logic",
)

USAGE = (
    "read",
    "preserve",
    "inspect",
    "use as formal structural reference",
)

RUNTIME_STATUS = "not intended as active runtime modules in current form"

NOTES = (
    "03A.py uses a tuple of pairs for projected relation descriptions to avoid duplicate key collision.",
    "04_EX.py uses layer_set = () as a frozen empty structural container.",
    "The entire set is designed as a closed declarative specification.",
)

LICENSE = "No license defined. Formal structural system only."
