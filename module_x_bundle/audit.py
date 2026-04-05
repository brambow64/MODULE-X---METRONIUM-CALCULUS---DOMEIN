"""
MODULE X --- AUDIT
Status: DECLARATIVE_SUPPORT · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: CONTENT AUDIT
"""

from pathlib import Path

import loader
import manifest


AUDIT_STATUS = (
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

AUDIT_SCOPE = (
    "constant policy",
    "closure flags",
    "core declarative integrity",
    "special file rule checks",
)

AUDIT_RULES = (
    "audit reads definitions only",
    "audit does not mutate files",
    "audit does not reinterpret structure",
    "audit does not calculate derived system behavior",
)

CORE_FILES_WITH_CONSTANT = (
    "01.py",
    "01A.py",
    "01B.py",
    "02.py",
    "02A.py",
    "02B.py",
    "03.py",
    "03A.py",
    "03B.py",
)

CALCULUS_FILES = (
    "01A.py",
    "02A.py",
    "03A.py",
)

DOMEIN_FILES = (
    "01B.py",
    "02B.py",
    "03B.py",
)

PRIME_DIRECTIVE_FILES = (
    "01.py",
    "02.py",
    "03.py",
)

CLOSED_UNIT_FILES = (
    "01.py",
    "01A.py",
    "01B.py",
    "02.py",
    "02A.py",
    "02B.py",
    "03.py",
    "03A.py",
    "03B.py",
)


def _load(file_name: str, base_path: str | Path = "."):
    return loader.load_module_from_file(file_name, base_path)


def audit_constant_policy(file_name: str, base_path: str | Path = ".") -> dict[str, object]:
    module = _load(file_name, base_path)
    constant = getattr(module, "CONSTANT", None)

    return {
        "file_name": file_name,
        "has_constant": constant is not None,
        "constant_is_dict": isinstance(constant, dict),
        "has_segments": isinstance(constant, dict) and "segments" in constant,
        "segments_is_tuple": isinstance(constant, dict) and isinstance(constant.get("segments"), tuple),
        "visibility_is_internal_only": isinstance(constant, dict) and constant.get("visibility") == "internal_only",
        "ownership_is_unit_bound": isinstance(constant, dict) and constant.get("ownership") == "unit_bound",
    }


def audit_unit_closed_flag(file_name: str, base_path: str | Path = ".") -> dict[str, object]:
    module = _load(file_name, base_path)

    return {
        "file_name": file_name,
        "has_unit_is_closed": hasattr(module, "UNIT_IS_CLOSED"),
        "unit_is_closed_true": getattr(module, "UNIT_IS_CLOSED", False) is True,
    }


def audit_calculus_visibility_flag(file_name: str, base_path: str | Path = ".") -> dict[str, object]:
    module = _load(file_name, base_path)

    return {
        "file_name": file_name,
        "has_calculus_contains_no_visibility": hasattr(module, "CALCULUS_CONTAINS_NO_VISIBILITY"),
        "calculus_contains_no_visibility_true": getattr(module, "CALCULUS_CONTAINS_NO_VISIBILITY", False) is True,
    }


def audit_domein_visibility_flag(file_name: str, base_path: str | Path = ".") -> dict[str, object]:
    module = _load(file_name, base_path)

    return {
        "file_name": file_name,
        "has_domein_contains_no_relations_of_its_own": hasattr(module, "DOMEIN_CONTAINS_NO_RELATIONS_OF_ITS_OWN"),
        "domein_contains_no_relations_of_its_own_true": getattr(module, "DOMEIN_CONTAINS_NO_RELATIONS_OF_ITS_OWN", False) is True,
        "has_only_structural_visibility": hasattr(module, "ONLY_STRUCTURAL_VISIBILITY"),
        "only_structural_visibility_true": getattr(module, "ONLY_STRUCTURAL_VISIBILITY", False) is True,
    }


def audit_03A_special_rule(base_path: str | Path = ".") -> dict[str, object]:
    module = _load("03A.py", base_path)
    value = getattr(module, "PROJECTED_RELATIONS_DESCRIPTION", None)

    pairs_shape = (
        isinstance(value, tuple)
        and all(isinstance(item, tuple) and len(item) == 2 for item in value)
    )

    return {
        "file_name": "03A.py",
        "has_projected_relations_description": value is not None,
        "projected_relations_description_is_tuple": isinstance(value, tuple),
        "projected_relations_description_is_tuple_of_pairs": pairs_shape,
    }


def audit_04_EX_special_rule(base_path: str | Path = ".") -> dict[str, object]:
    module = _load("04_EX.py", base_path)
    template = getattr(module, "EXIT_JSON_TEMPLATE", None)

    layer_set_value = None
    if isinstance(template, dict):
        layer_set_value = template.get("layer_set")

    return {
        "file_name": "04_EX.py",
        "has_exit_json_template": isinstance(template, dict),
        "has_layer_set": isinstance(template, dict) and "layer_set" in template,
        "layer_set_is_tuple": isinstance(layer_set_value, tuple),
        "layer_set_is_empty_tuple": layer_set_value == (),
    }


def audit_core_constant_policy(base_path: str | Path = ".") -> dict[str, dict[str, object]]:
    return {
        file_name: audit_constant_policy(file_name, base_path)
        for file_name in CORE_FILES_WITH_CONSTANT
    }


def audit_closed_units(base_path: str | Path = ".") -> dict[str, dict[str, object]]:
    return {
        file_name: audit_unit_closed_flag(file_name, base_path)
        for file_name in CLOSED_UNIT_FILES
    }


def audit_calculus_files(base_path: str | Path = ".") -> dict[str, dict[str, object]]:
    return {
        file_name: audit_calculus_visibility_flag(file_name, base_path)
        for file_name in CALCULUS_FILES
    }


def audit_domein_files(base_path: str | Path = ".") -> dict[str, dict[str, object]]:
    return {
        file_name: audit_domein_visibility_flag(file_name, base_path)
        for file_name in DOMEIN_FILES
    }


def audit_all(base_path: str | Path = ".") -> dict[str, object]:
    return {
        "core_constant_policy": audit_core_constant_policy(base_path),
        "closed_units": audit_closed_units(base_path),
        "calculus_files": audit_calculus_files(base_path),
        "domein_files": audit_domein_files(base_path),
        "special_03A_rule": audit_03A_special_rule(base_path),
        "special_04_EX_rule": audit_04_EX_special_rule(base_path),
    }
