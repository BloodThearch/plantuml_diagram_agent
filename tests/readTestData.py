import os

def readTestData():
    # Get test data file paths
    cwd = os.getcwd()
    testDataPath = os.path.join(cwd,"tests","testData")
    testDataFileNames = os.listdir(testDataPath)
    testDataFilePaths = [os.path.join(testDataPath,testDataFileName) for testDataFileName in testDataFileNames]
    
    # Read data from them one by one
    results = []
    n = len(testDataFilePaths)
    for i,testDataFilePath in enumerate(testDataFilePaths):
        print("Reading file {}/{}...".format(i+1,n))
        with open(testDataFilePath, "r", encoding="utf-8") as f:
            data = f.read()
            results.append(data)
        print("File {}/{} Completed!".format(i+1,n))
    return results

