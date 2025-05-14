import os
import subprocess

def createPlantUMLDiagram(uml_code: str):
    """
    Generates a PlantUML diagram for the given .puml file using the PlantUML JAR.

    Args:
        file_name (str): The name of the .puml file (e.g., "example.puml")
                         The file is assumed to be in the 'outputs/' directory.
    """
    jar_path = os.path.join("plantuml", "plantuml.jar")
    puml_file_path = os.path.join("outputs", "out1.puml")
    with open(puml_file_path, "w", encoding="utf-8") as f:
        f.write(uml_code)

    # Ensure file exists
    if not os.path.isfile(puml_file_path):
        raise FileNotFoundError(f"{puml_file_path} does not exist.")

    # Build and run the command
    command = ["java", "-jar", jar_path, puml_file_path]
    
    try:
        subprocess.run(command, check=True)
        print(f"Diagram generated!")
    except subprocess.CalledProcessError as e:
        print(f"Error generating diagram: {e}")