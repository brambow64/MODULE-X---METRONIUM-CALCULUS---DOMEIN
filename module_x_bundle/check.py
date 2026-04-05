"""
MODULE X --- CHECK
Status: DECLARATIVE_SUPPORT · STRUCTURAL_ONLY · NO INTERPRETATION · NO CALCULATION
Type: CHECK ENTRY
"""

from pathlib import Path
from pprint import pprint

import report


CHECK_STATUS = (
    "STRUCTURAL_ONLY",
    "NO_INTERPRETATION",
    "NO_CALCULATION",
)

CHECK_SCOPE = (
    "run report build",
    "run clean-state check",
    "display read-only results",
)

CHECK_RULES = (
    "check reads only",
    "check does not mutate files",
    "check does not reinterpret structure",
    "check does not calculate derived behavior",
)


def build_check_output(base_path: str | Path = ".") -> dict[str, object]:
    return {
        "report": report.build_report(base_path),
        "report_clean": report.report_is_clean(base_path),
    }


def main(base_path: str | Path = ".") -> None:
    result = build_check_output(base_path)
    pprint(result)
    print()
    print(f"REPORT CLEAN = {result['report_clean']}")


if __name__ == "__main__":
    main()
