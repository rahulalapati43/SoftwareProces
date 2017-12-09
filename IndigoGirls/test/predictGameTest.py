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

    def test200_050_shouldValidatecolumnCountLE100(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 101
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_060_shouldValidatemissingrowCount(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing rowCount"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_070_shouldValidateinvalidrowCount(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = '2'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is not an integer"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_080_shouldValidaterowCountGT1(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 1
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test200_090_shouldValidaterowCountLE100(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 1000
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_010_shouldValidatemissingGrid(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 100
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing grid"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_020_shouldValidateGridLength(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        boardDictionary["grid"] = []
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid length"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_030_shouldValidateGridElementsType(self):
        inputDictionary = {}
        inputDictionary["op"] = "predict"
        inputDictionary["direction"] = "LEft"
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        boardDictionary["grid"] = ['1',2,3,4]
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid elements"
        outputDictionary = predictGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    # def test300_040_shouldValidateGridElementsGE0(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "predict"
    #     inputDictionary["direction"] = "LEft"
    #     inputDictionary["moves"] = 1
    #     boardDictionary = {}
    #     boardDictionary["columnCount"] = 2
    #     boardDictionary["rowCount"] = 2
    #     boardDictionary["grid"] = [-1,2,3,4]
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: grid elements must be GE 0"
    #     outputDictionary = predictGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)