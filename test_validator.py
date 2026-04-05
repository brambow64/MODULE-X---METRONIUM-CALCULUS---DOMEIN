import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent / "module_x_bundle"
sys.path.insert(0, str(PROJECT_DIR))

import validator


def test_validator_file_count() -> None:
    assert validator.validate_file_count() is True


def test_validator_group_counts() -> None:
    assert validator.validate_group_counts() is True


def test_validator_no_duplicates() -> None:
    assert validator.validate_no_duplicate_manifest_entries() is True


def test_validator_constitutional_order_membership() -> None:
    assert validator.validate_constitutional_order_membership() is True


def test_validator_required_files_exist() -> None:
    missing = validator.validate_required_files_exist(PROJECT_DIR)
    assert missing == ()


def test_validator_manifest_integrity() -> None:
    result = validator.validate_manifest_integrity(PROJECT_DIR)
    assert result["file_count_valid"] is True
    assert result["group_counts_valid"] is True
    assert result["no_duplicate_manifest_entries"] is True
    assert result["constitutional_order_membership_valid"] is True
    assert result["all_required_files_exist"] is True
    assert result["missing_files"] == ()
