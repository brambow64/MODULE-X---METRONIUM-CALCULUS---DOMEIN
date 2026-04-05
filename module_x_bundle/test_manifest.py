import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

import manifest


def test_manifest_file_count_matches_all_files() -> None:
    assert len(manifest.ALL_FILES) == manifest.FILE_COUNT


def test_manifest_group_counts_match() -> None:
    assert len(manifest.CORE_FILES) == manifest.CORE_COUNT
    assert len(manifest.OBSERVATION_FILES) == manifest.OBSERVATION_COUNT
    assert len(manifest.EXPORT_FILES) == manifest.EXPORT_COUNT
    assert len(manifest.DOCUMENT_FILES) == manifest.DOCUMENT_COUNT


def test_manifest_has_no_duplicate_entries() -> None:
    assert len(set(manifest.ALL_FILES)) == len(manifest.ALL_FILES)


def test_manifest_is_closed() -> None:
    assert manifest.MANIFEST_IS_CLOSED is True
