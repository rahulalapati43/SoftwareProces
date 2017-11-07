
def recommendGame(messageDictionary):

    outputDictionary = {}

    if "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 0

    elif (isinstance(messageDictionary["moves"], int) == False):
        outputDictionary["gameStatus"] = "error: moves is not an integer"

    elif (messageDictionary["moves"] < 0):
        outputDictionary["gameStatus"] = "error: moves must be GE 0"

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    return outputDictionary