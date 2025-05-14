from src.diagramValidation import ParsedPlantUML
import re

def extract_plantuml(text: str) -> str:
    match = re.search(r'@startuml.*?@enduml', text, re.DOTALL)
    if match:
        return match.group(0).strip()
    raise ValueError("No PlantUML block found in the text.")


def performDiagramValidation(textData: str):
    try:
        code = extract_plantuml(textData)
        result = ParsedPlantUML(plantuml_code=code)
        print(f"✅ Valid {result.diagram_type} diagram")
        return True, code  # return the validated code
    except Exception as e:
        print(f"❌ {e}")
        return False, None