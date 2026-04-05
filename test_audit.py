import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent / "module_x_bundle"
sys.path.insert(0, str(PROJECT_DIR))

import audit


CORE_CONSTANT_FILES = (
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


def test_audit_core_constant_policy() -> None:
    result = audit.audit_core_constant_policy(PROJECT_DIR)

    for file_name in CORE_CONSTANT_FILES:
        item = result[file_name]
        assert item["has_constant"] is True
        assert item["constant_is_dict"] is True
        assert item["has_segments"] is True
        assert item["segments_is_tuple"] is True
        assert item["visibility_is_internal_only"] is True
        assert item["ownership_is_unit_bound"] is True


def test_audit_closed_units() -> None:
    result = audit.audit_closed_units(PROJECT_DIR)

    for item in result.values():
        assert item["has_unit_is_closed"] is True
        assert item["unit_is_closed_true"] is True


def test_audit_calculus_files() -> None:
    result = audit.audit_calculus_files(PROJECT_DIR)

    for item in result.values():
        assert item["has_calculus_contains_no_visibility"] is True
        assert item["calculus_contains_no_visibility_true"] is True


def test_audit_domein_files() -> None:
    result = audit.audit_domein_files(PROJECT_DIR)

    for item in result.values():
        assert item["has_domein_contains_no_relations_of_its_own"] is True
        assert item["domein_contains_no_relations_of_its_own_true"] is True
        assert item["has_only_structural_visibility"] is True
        assert item["only_structural_visibility_true"] is True


def test_audit_03A_special_rule() -> None:
    result = audit.audit_03A_special_rule(PROJECT_DIR)
    assert result["has_projected_relations_description"] is True
    assert result["projected_relations_description_is_tuple"] is True
    assert result["projected_relations_description_is_tuple_of_pairs"] is True


def test_audit_04_EX_special_rule() -> None:
    result = audit.audit_04_EX_special_rule(PROJECT_DIR)
    assert result["has_exit_json_template"] is True
    assert result["has_layer_set"] is True
    assert result["layer_set_is_tuple"] is True
    assert result["layer_set_is_empty_tuple"] is True
