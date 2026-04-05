"""
MODULE X --- LOADER
Status: DECLARATIVE_SUPPORT · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: FILE LOADER
"""

from pathlib import Path
import importlib.util

import manifest


LOADER_STATUS = (
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

LOADER_SCOPE = (
    "load declarative files",
    "inspect exported symbols",
    "preserve source structure",
)

LOADER_RULES = (
    "loader reads files only",
    "loader does not mutate files",
    "loader does not reinterpret definitions",
    "loader does not calculate derived behavior",
)


def get_file_path(file_name: str, base_path: str | Path = ".") -> Path:
    return Path(base_path) / file_name


def file_exists(file_name: str, base_path: str | Path = ".") -> bool:
    return get_file_path(file_name, base_path).exists()


def read_file_text(file_name: str, base_path: str | Path = ".") -> str:
    path = get_file_path(file_name, base_path)
    return path.read_text(encoding="utf-8")


def load_module_from_file(file_name: str, base_path: str | Path = "."):
    path = get_file_path(file_name, base_path)
    module_name = path.stem

    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create import spec for {file_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_all_modules(base_path: str | Path = ".") -> dict[str, object]:
    loaded = {}

    for file_name in manifest.ALL_FILES:
        loaded[file_name] = load_module_from_file(file_name, base_path)

    return loaded


def get_public_symbols(module) -> tuple[str, ...]:
    return tuple(
        name
        for name in dir(module)
        if not name.startswith("_")
    )


def inspect_module_symbols(file_name: str, base_path: str | Path = ".") -> dict[str, object]:
    module = load_module_from_file(file_name, base_path)

    return {
        "file_name": file_name,
        "module_name": module.__name__,
        "public_symbols": get_public_symbols(module),
    }


def inspect_all_module_symbols(base_path: str | Path = ".") -> dict[str, dict[str, object]]:
    inspected = {}

    for file_name in manifest.ALL_FILES:
        inspected[file_name] = inspect_module_symbols(file_name, base_path)

    return inspected
