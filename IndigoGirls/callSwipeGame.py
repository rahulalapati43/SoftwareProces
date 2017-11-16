from IndigoGirls.swipeGame import swipeGame

def callSwipeGame(messageDictionary):

    if (messageDictionary != {'gameStatus': 'error: no tiles can be shifted'}):
        messageDictionary["direction"] = "left"
        leftDict = swipeGame(messageDictionary)

        messageDictionary["direction"] = "right"
        rightDict = swipeGame(messageDictionary)

        messageDictionary["direction"] = "up"
        upDict = swipeGame(messageDictionary)

        messageDictionary["direction"] = "down"
        downDict = swipeGame(messageDictionary)

        if (leftDict["gameStatus"] == "underway"):
            leftDict["score"] = leftDict["score"] + messageDictionary["score"]

        if (rightDict["gameStatus"] == "underway"):
            rightDict["score"] = rightDict["score"] + messageDictionary["score"]

        if (upDict["gameStatus"] == "underway"):
            upDict["score"] = upDict["score"] + messageDictionary["score"]

        if (downDict["gameStatus"] == "underway"):
            downDict["score"] = downDict["score"] + messageDictionary["score"]

    else:

        leftDict = messageDictionary
        rightDict = messageDictionary
        upDict = messageDictionary
        downDict = messageDictionary

    return leftDict,rightDict,upDict,downDict