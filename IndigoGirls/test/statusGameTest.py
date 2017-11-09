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

    def test100_030_shouldvalidatetileUpperBound(self):
        inputDictionary = {}
        inputDictionary["tile"] = 200
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid tile value"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test100_040_shouldvalidatetileInt(self):
        inputDictionary = {}
        inputDictionary["tile"] = '3'
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: tile is not an integer"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

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

    def test500_010_shouldvalidatemissingGrid(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 100
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing grid"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_020_shouldvalidateGridLength(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0,1,1,0,1]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid length"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_030_shouldvalidateGridElementsInt(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0,1,1,'0']
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid Elements"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_040_shouldvalidateGridElementsGE0(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0, 1, 1, -1]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: grid Elements must be GE 0"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_050_shouldvalidateGrid2ElementsGT0(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0, 1, 0, 0]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: No fewer than two items can be GT 0"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test600_010_shouldvalidateWin(self):
        inputDictionary = {}
        inputDictionary["tile"] = 16
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [0,0,0,0,0,4,0,0,0,0,1,0,0,0,1,0]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "win"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test600_020_shouldvalidateLose(self):
        inputDictionary = {}
        inputDictionary["tile"] = 32
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "lose"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test600_030_shouldvalidateUnderway(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2048
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "underway"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)