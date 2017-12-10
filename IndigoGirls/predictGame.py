from IndigoGirls.swipeGame import swipeGame

def predictGame(messageDictionary):
    """
                     predictGame is a function and is invoked in dispatch when the operation to be performed is predict
                     high score, low score & average score for lookahead moves.
                :param messageDictionary: Is a dictionary which consists the following name value pairs: operation (op), direction, moves,
                                         board dictionary which consists of row count (rowCount), column count (columnCount) and grid.
                                         All the params are mandatory.
                :return:                 A dictionary which consists of the following name value pairs: prediction, game status.
                                         The prediction consists of another dictionary which consists of 3 name value pairs:
                                         highScore, lowScore and averageScore.
                """

    #output dictionary is returned to dispatch after the calculations are done
    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    #call to validatePredict to validate the input dictionary
    outputDictionary = validatePredict(messageDictionary, outputDictionary)

    #if every element of the input dictionary are validated
    if (outputDictionary["gameStatus"] == "underway"):

        inputDictionary = {}
        predictDictionary = {}
        outputListDictionary = {}

        #if number of lookahead moves is 1
        if (messageDictionary["moves"] == 1):
            resultDictionary = swipeGame(messageDictionary)
            predictDictionary["highScore"] = resultDictionary["score"]
            predictDictionary["lowScore"] = resultDictionary["score"]
            predictDictionary["averageScore"] = resultDictionary["score"]
            outputDictionary["prediction"] = predictDictionary
            outputDictionary["gameStatus"] = "underway"

        #if number of lookahead moves is greater than 1
        elif (messageDictionary["moves"] > 1):
            outputList = []
            scoresList = []
            start = 0
            weightScore = 0
            sumScore = 0

            try:
                for move in range(1,messageDictionary["moves"] + 1):
                    if (move == 1):
                        resultDictionary = swipeGame(messageDictionary)
                        if (resultDictionary["gameStatus"] == "underway"):
                            firstScore = resultDictionary["score"]
                            resultDictionary["score"] = 0
                        else:
                            return resultDictionary

                        outputList.append(resultDictionary)
                        outputListDictionary[move] = outputList
                        outputList = []
                    else:
                        end = len(outputListDictionary[move - 1])
                        scoresList = []
                        for index in range(start,end):
                            resultDictionary = outputListDictionary[move-1][index]
                            if (resultDictionary["gameStatus"] == "underway"):
                                inputDictionary["op"] = "predict"
                                inputDictionary["board"] = resultDictionary["board"]
                                inputDictionary["score"] = resultDictionary["score"]

                                for element in range(0,len(inputDictionary["board"]["grid"])):
                                    if (inputDictionary["board"]["grid"][element] == 0):
                                        inputDictionary["board"]["grid"][element] = 1
                                        inputDictionary["direction"] = "left"
                                        leftDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "right"
                                        rightDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "up"
                                        upDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "down"
                                        downDictionary = swipeGame(inputDictionary)

                                        if (leftDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (3 * leftDictionary["score"])
                                            weightScore = weightScore + 3
                                            leftDictionary["score"] = leftDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(leftDictionary["score"])

                                        if (rightDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (3 * rightDictionary["score"])
                                            weightScore = weightScore + 3
                                            rightDictionary["score"] = rightDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(rightDictionary["score"])

                                        if (upDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (3 * upDictionary["score"])
                                            weightScore = weightScore + 3
                                            upDictionary["score"] = upDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(upDictionary["score"])

                                        if (downDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (3 * downDictionary["score"])
                                            weightScore = weightScore + 3
                                            downDictionary["score"] = downDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(downDictionary["score"])

                                        outputList.append(leftDictionary)
                                        outputList.append(rightDictionary)
                                        outputList.append(upDictionary)
                                        outputList.append(downDictionary)

                                        inputDictionary["board"]["grid"][element] = 2
                                        inputDictionary["direction"] = "left"
                                        leftDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "right"
                                        rightDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "up"
                                        upDictionary = swipeGame(inputDictionary)
                                        inputDictionary["direction"] = "down"
                                        downDictionary = swipeGame(inputDictionary)

                                        if (leftDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (1 * leftDictionary["score"])
                                            weightScore = weightScore + 1
                                            leftDictionary["score"] = leftDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(leftDictionary["score"])

                                        if (rightDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (1 * rightDictionary["score"])
                                            weightScore = weightScore + 1
                                            rightDictionary["score"] = rightDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(rightDictionary["score"])

                                        if (upDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (1 * upDictionary["score"])
                                            weightScore = weightScore + 1
                                            upDictionary["score"] = upDictionary["score"] +  inputDictionary["score"]
                                            scoresList.append(upDictionary["score"])

                                        if (downDictionary["gameStatus"] == "underway"):
                                            sumScore = sumScore + (1 * downDictionary["score"])
                                            weightScore = weightScore + 1
                                            downDictionary["score"] = downDictionary["score"] + inputDictionary["score"]
                                            scoresList.append(downDictionary["score"])

                                        outputList.append(leftDictionary)
                                        outputList.append(rightDictionary)
                                        outputList.append(upDictionary)
                                        outputList.append(downDictionary)

                                        inputDictionary["board"]["grid"][element] = 0

                        outputListDictionary[move] = outputList
                        outputList = []

                predictDictionary["highScore"] = firstScore + max(scoresList)
                predictDictionary["lowScore"] = firstScore + min(scoresList)
                averageScore = int(round(float(sumScore)/float(weightScore)))
                predictDictionary["averageScore"] = firstScore + averageScore
                outputDictionary["prediction"] = predictDictionary
                outputDictionary["gameStatus"] = "underway"

            #to handle all kind of exceptions
            except:
                outputDictionary["gameStatus"] = "error: an unexpected event occured"

    return outputDictionary

#method to validate input dictionary for Predict
def validatePredict(messageDictionary, outputDictionary):
    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"].lower() != "up" and messageDictionary["direction"].lower() != "down" and
                  messageDictionary["direction"].lower() != "left" and messageDictionary[
        "direction"].lower() != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    elif "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 1

    elif (isinstance(messageDictionary["moves"], int) == False):
        outputDictionary["gameStatus"] = "error: invalid moves"

    elif (messageDictionary["moves"] < 1):
        outputDictionary["gameStatus"] = "error: moves must be GE 1"

    if (outputDictionary["gameStatus"] == "underway"):
        outputDictionary = validateBoard(messageDictionary, outputDictionary)

    return outputDictionary

#method to validate board
def validateBoard(messageDictionary, outputDictionary):

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif ((messageDictionary["board"]["columnCount"] <= 1) or (messageDictionary["board"]["columnCount"] > 100)):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    elif ((messageDictionary["board"]["rowCount"] <= 1) or (messageDictionary["board"]["rowCount"] > 100)):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif "grid" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing grid"

    elif (len(messageDictionary["board"]["grid"]) != (
                messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
        outputDictionary["gameStatus"] = "error: invalid grid length"

    elif (len(messageDictionary["board"]["grid"]) == (
                messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
        for index in range(0, len(messageDictionary["board"]["grid"])):
            if (isinstance(messageDictionary["board"]["grid"][index], int) == False):
                outputDictionary["gameStatus"] = "error: invalid grid elements"

        if (outputDictionary["gameStatus"] != "error: invalid grid elements"):
            for index in range(0, len(messageDictionary["board"]["grid"])):
                if (messageDictionary["board"]["grid"][index] < 0):
                    outputDictionary["gameStatus"] = "error: grid elements must be GE 0"

            if (outputDictionary["gameStatus"] != "error: grid elements must be GE 0"):
                for index in range(0, len(messageDictionary["board"]["grid"])):
                    if (messageDictionary["board"]["grid"][index] > (
                                messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
                        outputDictionary["gameStatus"] = "error: grid elements must be LE gridLength"

                if (outputDictionary["gameStatus"] != "error: grid elements must be LE gridLength"):
                    countGT0 = 0
                    for index in range(0, len(messageDictionary["board"]["grid"])):
                        if (messageDictionary["board"]["grid"][index] > 0):
                            countGT0 = countGT0 + 1

                    if (countGT0 < 2):
                        outputDictionary["gameStatus"] = "error: No fewer than 2 grid elements must be GT 0"

    return outputDictionary


