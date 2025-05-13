from tests import readTestData
from src.performDiagramValidation import performDiagramValidation

def allTests():
    dataList = readTestData.readTestData()
    n = len(dataList)
    for i, data in enumerate(dataList):
        print("Running Test {}/{}...".format(i+1,n))
        if performDiagramValidation(data):
            print("Data Valid!")
        else:
            print("Data Invalid.")

if __name__ == "__main__":
    allTests()

    