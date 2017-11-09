
def statusGame(messageDictionary):

    if "tile" not in messageDictionary.keys():
        messageDictionary["tile"] = 2048

    return messageDictionary
