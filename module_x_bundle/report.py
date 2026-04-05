"""
MODULE X --- REPORT
Status: DECLARATIVE_SUPPORT · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: SUMMARY REPORT
"""

from pathlib import Path

import manifest
import validator
import audit


REPORT_STATUS = (
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

REPORT_SCOPE = (
    "manifest summary",
    "validator summary",
    "audit summary",
    "read-only reporting",
)

REPORT_RULES = (
    "report reads only",
    "report does not mutate files",
    "report does not reinterpret structure",
    "report does not calculate derived behavior",
)


def build_manifest_summary() -> dict[str, object]:
    return {
        "project_name": manifest.PROJECT_NAME,
        "project_status": manifest.PROJECT_STATUS,
        "root_folder": manifest.ROOT_FOLDER,
        "file_count": manifest.FILE_COUNT,
        "core_count": manifest.CORE_COUNT,
        "observation_count": manifest.OBSERVATION_COUNT,
        "export_count": manifest.EXPORT_COUNT,
        "document_count": manifest.DOCUMENT_COUNT,
    }


def build_validator_summary(base_path: str | Path = ".") -> dict[str, object]:
    return validator.validate_manifest_integrity(base_path)


def build_audit_summary(base_path: str | Path = ".") -> dict[str, object]:
    return audit.audit_all(base_path)


def build_report(base_path: str | Path = ".") -> dict[str, object]:
    return {
        "manifest": build_manifest_summary(),
        "validator": build_validator_summary(base_path),
        "audit": build_audit_summary(base_path),
    }


def report_is_clean(base_path: str | Path = ".") -> bool:
    data = build_report(base_path)

    validator_summary = data["validator"]
    audit_summary = data["audit"]

    validator_ok = (
        validator_summary["file_count_valid"]
        and validator_summary["group_counts_valid"]
        and validator_summary["no_duplicate_manifest_entries"]
        and validator_summary["constitutional_order_membership_valid"]
        and validator_summary["all_required_files_exist"]
    )

    core_constant_ok = all(
        item["has_constant"]
        and item["constant_is_dict"]
        and item["has_segments"]
        and item["segments_is_tuple"]
        and item["visibility_is_internal_only"]
        and item["ownership_is_unit_bound"]
        for item in audit_summary["core_constant_policy"].values()
    )

    closed_units_ok = all(
        item["has_unit_is_closed"]
        and item["unit_is_closed_true"]
        for item in audit_summary["closed_units"].values()
    )

    calculus_ok = all(
        item["has_calculus_contains_no_visibility"]
        and item["calculus_contains_no_visibility_true"]
        for item in audit_summary["calculus_files"].values()
    )

    domein_ok = all(
        item["has_domein_contains_no_relations_of_its_own"]
        and item["domein_contains_no_relations_of_its_own_true"]
        and item["has_only_structural_visibility"]
        and item["only_structural_visibility_true"]
        for item in audit_summary["domein_files"].values()
    )

    special_03A_ok = (
        audit_summary["special_03A_rule"]["has_projected_relations_description"]
        and audit_summary["special_03A_rule"]["projected_relations_description_is_tuple"]
        and audit_summary["special_03A_rule"]["projected_relations_description_is_tuple_of_pairs"]
    )

    special_04_EX_ok = (
        audit_summary["special_04_EX_rule"]["has_exit_json_template"]
        and audit_summary["special_04_EX_rule"]["has_layer_set"]
        and audit_summary["special_04_EX_rule"]["layer_set_is_tuple"]
        and audit_summary["special_04_EX_rule"]["layer_set_is_empty_tuple"]
    )

    return (
        validator_ok
        and core_constant_ok
        and closed_units_ok
        and calculus_ok
        and domein_ok
        and special_03A_ok
        and special_04_EX_ok
    )
