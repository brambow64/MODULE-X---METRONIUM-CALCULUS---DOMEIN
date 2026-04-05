import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

import report


def test_build_manifest_summary() -> None:
    summary = report.build_manifest_summary()
    assert summary["project_name"] == "MODULE X — METRONIUM CALCULUS & DOMEIN"
    assert summary["file_count"] == 20
    assert summary["core_count"] == 10
    assert summary["observation_count"] == 6
    assert summary["export_count"] == 3
    assert summary["document_count"] == 1


def test_build_report_contains_sections() -> None:
    data = report.build_report(PROJECT_DIR)
    assert "manifest" in data
    assert "validator" in data
    assert "audit" in data


def test_report_is_clean() -> None:
    assert report.report_is_clean(PROJECT_DIR) is True
