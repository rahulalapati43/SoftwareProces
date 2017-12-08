from unittest import TestCase
from IndigoGirls.predictGame import predictGame

class predictGameTest(TestCase):
    def test100_010_shouldValidatemissingdirection(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing direction"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary,outputDictionary)

    def test100_020_shouldValidateinvaliddirection(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "out"
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid direction"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test100_030_shouldValidatemovestype(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = '1'
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid moves"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test100_040_shouldValidatemovesGE1(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 0
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: moves must be GE 1"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_010_shouldValidatemissingBoard(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing board"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_020_shouldValidatemissingcolumnCount(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        inputDictionary["board"] = {}
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing columnCount"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_030_shouldValidateinvalidcolumnCount(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = '1'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is not an integer"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_040_shouldValidatecolumnCountGT1(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 1
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)