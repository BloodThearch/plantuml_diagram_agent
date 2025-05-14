from models.createLlama3Instance import Llama3Instance
from dotenv import dotenv_values

config = dotenv_values(".env")

def runModel():
    client = Llama3Instance(key=config["NVIDIA_LLAMA3_API_KEY"])
    print("Model Instance Created!")

    user_input=None
    user_input = str(input("Enter your message: "))
    while (user_input!="quit"):
        client.sendSingleMessage(msg=user_input)
        print("#####")
        user_input = str(input("Enter your message: "))

if __name__ == "__main__":
    runModel()