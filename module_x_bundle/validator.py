"""
MODULE X --- VALIDATOR
Status: DECLARATIVE_SUPPORT · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: STRUCTURE VALIDATOR
"""

from pathlib import Path

import manifest


VALIDATOR_STATUS = (
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

VALIDATOR_SCOPE = (
    "file membership",
    "file count",
    "role count",
    "required file presence",
)

VALIDATOR_RULES = (
    "validator reads only",
    "validator does not mutate files",
    "validator does not interpret file meaning",
    "validator does not calculate derived system behavior",
)


def get_expected_files() -> tuple[str, ...]:
    return manifest.ALL_FILES


def get_root_folder() -> str:
    return manifest.ROOT_FOLDER


def validate_file_count() -> bool:
    return len(manifest.ALL_FILES) == manifest.FILE_COUNT


def validate_group_counts() -> bool:
    return (
        len(manifest.CORE_FILES) == manifest.CORE_COUNT
        and len(manifest.OBSERVATION_FILES) == manifest.OBSERVATION_COUNT
        and len(manifest.EXPORT_FILES) == manifest.EXPORT_COUNT
        and len(manifest.DOCUMENT_FILES) == manifest.DOCUMENT_COUNT
    )


def validate_no_duplicate_manifest_entries() -> bool:
    return len(set(manifest.ALL_FILES)) == len(manifest.ALL_FILES)


def validate_constitutional_order_membership() -> bool:
    return set(manifest.CONSTITUTIONAL_ORDER) == set(manifest.ALL_FILES) - set(manifest.DOCUMENT_FILES)


def validate_required_files_exist(base_path: str | Path = ".") -> tuple[str, ...]:
    root = Path(base_path)
    missing = []

    for file_name in manifest.ALL_FILES:
        if not (root / file_name).exists():
            missing.append(file_name)

    return tuple(missing)


def validate_manifest_integrity(base_path: str | Path = ".") -> dict[str, object]:
    missing_files = validate_required_files_exist(base_path)

    return {
        "file_count_valid": validate_file_count(),
        "group_counts_valid": validate_group_counts(),
        "no_duplicate_manifest_entries": validate_no_duplicate_manifest_entries(),
        "constitutional_order_membership_valid": validate_constitutional_order_membership(),
        "missing_files": missing_files,
        "all_required_files_exist": len(missing_files) == 0,
    }
