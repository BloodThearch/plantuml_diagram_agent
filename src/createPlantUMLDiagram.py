import os
from plantuml import PlantUML

def createPlantUMLDiagram(uml_code: str, output_path: str = "", image_format: str = "jpg", plantuml_jar_path: str = "plantuml.jar"):
    """
    Generates a UML diagram using PlantUML and saves it as PNG or JPG.

    Args:
        uml_code (str): The UML code to be rendered.
        output_path (str): The path where the image will be saved.
        image_format (str): 'png' or 'jpg'.
        plantuml_jar_path (str): Path to plantuml.jar file.

    Returns:
        bool: True if generation is successful, False otherwise.
    """
    if image_format not in ["png", "jpg"]:
        raise ValueError("Only 'png' or 'jpg' formats are supported.")
    
    # Make sure the output path has the correct extension
    if not output_path.endswith(f".{image_format}"):
        output_path = os.path.join(os.getcwd(),"outputs",f"test.{image_format}")

    # Write the UML code to a temporary .uml file
    uml_file = output_path.replace(f".{image_format}", ".uml")
    with open(uml_file, "w") as f:
        f.write(uml_code)

    # Configure the PlantUML processor
    server = PlantUML(url=None, basic_auth={}, form_auth={}, http_opts={}, request_opts={})

    try:
        server.processes_file(uml_file)
        # Move generated file to the desired output name
        generated_file = uml_file.replace(".uml", f".{image_format}")
        if os.path.exists(generated_file):
            os.rename(generated_file, output_path)
            os.remove(uml_file)  # Clean up .uml file
            return True
        else:
            return False
    except Exception as e:
        print(f"Error generating diagram: {e}")
        return False