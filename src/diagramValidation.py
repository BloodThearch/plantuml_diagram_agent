from pydantic import BaseModel, field_validator, model_validator
import re
from typing import Optional, Literal


class ParsedPlantUML(BaseModel):
    diagram_type: Optional[Literal[
        'sequence', 'usecase', 'class', 'object', 'activity',
        'component', 'deployment', 'state', 'timing'
    ]] = None
    plantuml_code: str

    @field_validator('plantuml_code')
    @classmethod
    def check_startuml_enduml(cls, value: str) -> str:
        if not value.strip().startswith('@startuml') or not value.strip().endswith('@enduml'):
            raise ValueError("Code must start with '@startuml' and end with '@enduml'")
        return value

    @model_validator(mode='after')
    def infer_and_validate(self) -> 'ParsedPlantUML':
        code = self.plantuml_code
        dtype = self.infer_diagram_type(code)
        self.diagram_type = dtype

        if not self.check_diagram_syntax(code, dtype):
            raise ValueError(f"Invalid or missing syntax for inferred '{dtype}' diagram.")

        return self

    @staticmethod
    def infer_diagram_type(code: str) -> str:
        patterns = {
            'sequence': r'\b\w+\s*[-.]*[<>]?[-]+[<>]?[-.]*>\s*\w+',
            'usecase': r'\b(actor|usecase)\b|\b:\w+:\b|\(.*?\)',
            'class': r'\bclass\s+\w+|\w+\s+[-.<|*o+#^x}]+[-.<>|*o+#^x}]+\s+\w+',
            # 'object': r'\bobject\s+\w+',
            # 'activity': r'\bstart\b.*\bend\b',
            # 'component': r'\bcomponent\s+\w+',
            # 'deployment': r'\bnode\s+\w+',
            # 'state': r'\bstate\s+\w+',
            # 'timing': r'\brobust\s+\w+',
        }
        for dtype, pattern in patterns.items():
            if re.search(pattern, code, re.DOTALL):
                return dtype
        return "unknown"

    @staticmethod
    def check_diagram_syntax(code: str, dtype: str) -> bool:
        checks = {
            'sequence': lambda c: re.search(r'\b\w+\s*[-.]*[<>]?[-]+[<>]?[-.]*>\s*\w+', c),
            'usecase': lambda c: re.search(r'\b(actor|usecase)\b|\b:\w+:\b|\(.*?\)', c),
            'class': lambda c: re.search(r'\bclass\s+\w+|\w+\s+[-.<|*o+#^x}]+[-.<>|*o+#^x}]+\s+\w+', c),
            # 'object': lambda c: re.search(r'\bobject\s+\w+', c),
            # 'activity': lambda c: re.search(r'\bstart\b.*\bend\b', c, re.DOTALL),
            # 'component': lambda c: re.search(r'\bcomponent\s+\w+', c),
            # 'deployment': lambda c: re.search(r'\bnode\s+\w+', c),
            # 'state': lambda c: re.search(r'\bstate\s+\w+', c),
            # 'timing': lambda c: re.search(r'\brobust\s+\w+', c),
        }
        return checks.get(dtype, lambda c: False)(code)
