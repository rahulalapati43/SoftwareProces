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

    def test300_020_shouldvalidatecolumnCountInt(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = '2'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is not an integer"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_030_shouldvalidatecolumnCountGT1(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 1
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_040_shouldvalidatecolumnCountLE100(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 101
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_010_shouldvalidatemissingrowCount(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing rowCount"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_020_shouldvalidaterowCountInt(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = '1'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is not an integer"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_030_shouldvalidaterowCountGT1(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 1
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_040_shouldvalidaterowCountLE100(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 1001
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)