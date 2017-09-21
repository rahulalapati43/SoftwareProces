from random import *
def initializeGame(messageDictionary):
    """
         initializeGame is a function and is invoked in dispatch when the operation to be performed is initialization
         of the grid.
    :param messageDictionary: Is a dictionary which consists the following name value pairs: operation (op),
                             row count (rowCount) & column count (colCount). All the three params are optional.
    :return:                 A dictionary which consists of the following name value pairs: score, board, game status.
                             The board consists of another dictionary which consists of 3 name value pairs:
                             rowCount, columnCount & grid.
    """

    #outputDictionary is the dictionary which return to dispatch.
    outputDictionary = {}

    #boardDictionary is the dictionary which we use to store the rowCount, columnCount & grid. It is a part of the
    #  outputDictionary.
    boardDictionary = {}

    #Intializing the variable used in the program.
    x = 0
    y = 0
    i = 0

    #Check if rowCount is specified by the user, else default it to 4.
    if "rowCount" not in messageDictionary.keys():
        messageDictionary["rowCount"] = 4

    #Check if columnCount is specified by the user, else not default it to 4.
    if "columnCount" not in messageDictionary.keys():
        messageDictionary["columnCount"] = 4

    #Check the boundary values for rowCount, if rowCount is out of bounds, set gameStatus to error.
    if (messageDictionary["rowCount"] <= 1 or messageDictionary["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    #Check the boundary values for columnCount, if columnCount is out of bounds, set gameStatus to error.
    if (messageDictionary["columnCount"] <= 1 or messageDictionary["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    #Check if rowCount is a valid integer, else set gameStatus to error.
    if (isinstance(messageDictionary["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    #Check if columnCount is a valid integer, else set gameStatus to error.
    if (isinstance(messageDictionary["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    #Check if rowCount and colCount are with their boundary values.
    if (messageDictionary["rowCount"] > 1 and messageDictionary["rowCount"] <= 100):
        if (messageDictionary["columnCount"] > 1 and messageDictionary["columnCount"] <= 100):

            #get the length of the grid list.
            i = messageDictionary["rowCount"] * messageDictionary["columnCount"]
            gridList = []

            #set all the elements in the grid list to '0'.
            for index in range(0, i):
                gridList.append(0)

            #generate 1 with a probability of 0.75 and 2 with a probability of 0.25.
            randomList = [1, 1, 1, 2]
            a = sample(randomList, 2)

            #generate two random positions in the grid list where we can insert values 1,2.
            x = randint(0, i - 1)
            y = randint(0, i - 1)

            #to check if the 2 randomly generated positions are not equal.
            while (x == y):
                x = randint(0, i - 1)
                y = randint(0, i - 1)

            #populate 2 random elements in the grid list with either 1 or 2.
            gridList[x] = a[0]
            gridList[y] = a[1]

            #populate the outputDictionary name value pairs.
            outputDictionary["score"] = 0
            boardDictionary["rowCount"] = messageDictionary["rowCount"]
            boardDictionary["columnCount"] = messageDictionary["columnCount"]
            boardDictionary["grid"] = gridList
            outputDictionary["board"] = boardDictionary
            outputDictionary["gameStatus"] = "underway"

    #return the outputDictionary to dispatch.
    return outputDictionary