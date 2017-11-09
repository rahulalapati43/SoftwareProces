from unittest import TestCase
from IndigoGirls.statusGame import statusGame

class StatusGameTest(TestCase):
    # def test100_010_shouldValidatetiledefault(self):
    #     inputDictionary = {}
    #     resultDictionary = {}
    #     resultDictionary["tile"] = 2048
    #     outputDictionary = statusGame(inputDictionary)
    #     self.assertEquals(resultDictionary,outputDictionary)

    # def test100_020_shouldValidatetileGE2(self):
    #     inputDictionary = {}
    #     inputDictionary["tile"] = 0
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: invalid tile value"
    #     outputDictionary = statusGame(inputDictionary)
    #     self.assertEquals(resultDictionary,outputDictionary)

    def test200_010_shouldvalidateBoard(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing board"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_010_shouldvalidatemissingcolumnCount(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing columnCount"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_010_shouldvalidatecolumnCountInt(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = '2'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is not an integer"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)


