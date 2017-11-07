
def recommendGame(messageDictionary):

    outputDictionary = {}

    if "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 0

    elif (isinstance(messageDictionary["moves"], int) == False):
        outputDictionary["gameStatus"] = "error: moves is not an integer"


    return outputDictionary