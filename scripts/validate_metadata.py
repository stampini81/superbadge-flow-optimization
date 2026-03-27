from pathlib import Path
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "sfdx-project.json",
    ROOT / "manifest" / "package.xml",
    ROOT / "force-app" / "main" / "default" / "flows" / "Staff_Recommendation.flow-meta.xml",
    ROOT / "force-app" / "main" / "default" / "flows" / "Book_Order_Count_1.flow-meta.xml",
    ROOT / "force-app" / "main" / "default" / "flows" / "Create_QA_Task_for_Book_Order.flow-meta.xml",
]


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for file_path in REQUIRED_FILES:
        if not file_path.exists():
            errors.append(f"Missing required file: {file_path}")
    return errors


def validate_xml_files() -> list[str]:
    errors: list[str] = []
    for xml_file in ROOT.rglob("*.xml"):
        try:
            ET.parse(xml_file)
        except ET.ParseError as exc:
            errors.append(f"Invalid XML in {xml_file}: {exc}")
    return errors


def main() -> int:
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_xml_files())

    if errors:
        for error in errors:
            print(error)
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
