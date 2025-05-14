'''This is test driver function for the project'''
from models.createLlama3Instance import Llama3Instance
from src.performDiagramValidation import performDiagramValidation
from src.createPlantUMLDiagram import createPlantUMLDiagram
from dotenv import dotenv_values

config = dotenv_values(".env")

def main():
    client = Llama3Instance(config["NVIDIA_LLAMA3_API_KEY"])
    print("Model Instance Created!")

    user_input=None
    user_input = str(input("Enter your message: "))
    while (user_input!="quit"):
        responseMessage = client.sendSingleMessage(msg=user_input)
        validationStatus, extracted_content= performDiagramValidation(responseMessage)
        if validationStatus:
            createPlantUMLDiagram(extracted_content)

        print("#####")
        user_input = str(input("Enter your message: "))

if __name__ == "__main__":
    main()