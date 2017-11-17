from unittest import TestCase
from IndigoGirls.recommendGame import recommendGame

class RecommendGameTest(TestCase):
    # def test100_010_shouldvalidateMoves(self):
    #     inputDictionary = {}
    #     resultDictionary = {}
    #     resultDictionary["moves"] = 0
    #     outputDictionary = recommendGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

    # def test100_020_shouldvalidateMovesInt(self):
    #     inputDictionary = {}
    #     inputDictionary["moves"] = '2'
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: moves is not an integer"
    #     outputDictionary = recommendGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)
    #
    # def test100_030_shouldvalidateMovesGE0(self):
    #     inputDictionary = {}
    #     inputDictionary["moves"] = -1
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: moves must be GE 0"
    #     outputDictionary = recommendGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

    def test200_010_shouldvalidateBoard(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing board"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_010_shouldvalidatecolumnCount(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing columnCount"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_020_shouldvalidatecolumnCountInt(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = '1'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is not an integer"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_030_shouldvalidatecolumnCountGT1(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 0
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test300_040_shouldvalidatecolumnCountLE100(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 101
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_010_shouldvalidaterowCount(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing rowCount"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_020_shouldvalidaterowCountInt(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = '2'
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is not an integer"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_030_shouldvalidaterowCountGT1(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 1
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test400_040_shouldvalidaterowCountLE100(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 304
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_010_shouldvalidateGrid(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 100
        boardDictionary["rowCount"] = 100
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing grid"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_020_shouldvalidateGridLength(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = []
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid length"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_030_shouldvalidateGridLength(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [1,2,3,4,5]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid grid length"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_040_shouldvalidateGridElementsInt(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = ['1',2,3,'4']
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: grid elements are not integers"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_050_shouldvalidateGridElementsGE0(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [-1,2,3,4]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: grid elements must be GE 0"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_060_shouldvalidateGridElementsUpperBound(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0,2,16,17]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        # resultDictionary["gameStatus"] = "error: grid elements must be LE 2 ** grid Length"
        resultDictionary["gameStatus"] = "error: grid elements must be LE grid Length"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test500_070_shouldvalidateNofewerthan2GridElementsGT0(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 2
        boardDictionary["rowCount"] = 2
        gridList = [0,2,0,0]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: No fewer than 2 items can be GT 0"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test600_010_shouldvalidatemoves0(self):
        inputDictionary = {}
        inputDictionary["moves"] = 0
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        outputDictionary = recommendGame(inputDictionary)
        self.assertTrue(outputDictionary["score"] == 16 or outputDictionary["score"] == 4)

    def test600_020_shouldvalidatemoves1(self):
        inputDictionary = {}
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        outputDictionary = recommendGame(inputDictionary)
        self.assertTrue(outputDictionary["score"] == 16)

    def test600_030_shouldvalidatemoves2(self):
        inputDictionary = {}
        inputDictionary["moves"] = 2
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        outputDictionary = recommendGame(inputDictionary)
        # self.assertTrue(outputDictionary["score"] == 20 or outputDictionary["score"] == 36 or outputDictionary["score"] == 40)
        self.assertTrue(outputDictionary["score"] == 16 or outputDictionary["score"] == 4)

    def test600_040_shouldvalidatenotilescanbeshifted(self):
        inputDictionary = {}
        inputDictionary["moves"] = 1
        boardDictionary = {}
        boardDictionary["columnCount"] = 4
        boardDictionary["rowCount"] = 4
        gridList = [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]
        boardDictionary["grid"] = gridList
        inputDictionary["board"] = boardDictionary
        outputDictionary = recommendGame(inputDictionary)
        resultDictionary = {}
        # resultDictionary["gameStatus"] = "error: no tiles can be shifted in 1 move"
        resultDictionary["gameStatus"] = "error: no tiles can be shifted on a subsequent swipe"
        self.assertEquals(resultDictionary,outputDictionary)