from unittest import TestCase
from IndigoGirls.swipeGame import swipeGame

class SwipeGameTest(TestCase):
    # def test100_010_shouldValidateopanddirection(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "out"
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: invalid direction"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary,outputDictionary)

     # def test100_020_shouldValidatemissingdirection(self):
     #     inputDictionary = {}
     #     inputDictionary["op"] = "swipe"
     #     resultDictionary = {}
     #     resultDictionary["gameStatus"] = "error: missing direction"
     #     outputDictionary = swipeGame(inputDictionary)
     #     self.assertEquals(resultDictionary,outputDictionary)

       # def test100_030_shouldValidaterowCount(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 0
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: rowCount is out of bounds"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

        # def test100_032_shouldValidatemissingrowCount(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "left"
        #     boardDictionary = {}
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["gameStatus"] = "error: missing rowCount"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary,outputDictionary)
        #
        # def test100_034_shouldValidatemissingcolumnCount(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "left"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["gameStatus"] = "error: missing columnCount"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)

       # def test100_040_shouldValidaterowCountType(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = "1"
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: rowCount is not an integer"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

       # def test100_050_shouldValidatecolCount(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 4
       #     boardDictionary["columnCount"] = 1
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: columnCount is out of bounds"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)
       #
       # def test100_060_shouldValidatecolCountType(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 4
       #     boardDictionary["columnCount"] = "100"
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: columnCount is not an integer"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

       # def test100_070_shouldValidateGridLength(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 4
       #     boardDictionary["columnCount"] = 5
       #     gridList = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0]
       #     boardDictionary["grid"] = gridList
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: invalid board"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

       # def test100_080_shouldValidateGridElements(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 4
       #     boardDictionary["columnCount"] = 4
       #     gridList = [0,0,0,0,0,0,0,0,0,0,'A',0,0,0,1,0]
       #     boardDictionary["grid"] = gridList
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: invalid grid elements"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

       # def test100_090_shouldValidateGridElementsgreaterthan0(self):
       #     inputDictionary = {}
       #     inputDictionary["op"] = "swipe"
       #     inputDictionary["direction"] = "left"
       #     boardDictionary = {}
       #     boardDictionary["rowCount"] = 4
       #     boardDictionary["columnCount"] = 4
       #     gridList = [0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
       #     boardDictionary["grid"] = gridList
       #     inputDictionary["board"] = boardDictionary
       #     resultDictionary = {}
       #     resultDictionary["gameStatus"] = "error: Each item in the grid must be GE 0"
       #     outputDictionary = swipeGame(inputDictionary)
       #     self.assertEquals(resultDictionary,outputDictionary)

    # def test100_095_shouldValidateatleast2GridElementsgreaterthan0(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "left"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: No fewer than two items can be GT 0"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

    # def test200_010_shouldSwipeLeft(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "left"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["score"] = 0
    #     resboardDictionary = {}
    #     resboardDictionary["columnCount"] = 4
    #     resboardDictionary["rowCount"] = 4
    #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    #     resultDictionary["board"] = resboardDictionary
    #     resultDictionary["gameStatus"] = "underway"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)
    #
    # def test200_020_shouldSwipeLeft(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "left"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["score"] = 4
    #     resboardDictionary = {}
    #     resboardDictionary["columnCount"] = 4
    #     resboardDictionary["rowCount"] = 4
    #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0]
    #     resultDictionary["board"] = resboardDictionary
    #     resultDictionary["gameStatus"] = "underway"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)
    #
    # def test200_030_validateNoTilesShift(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "left"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["gameStatus"] = "error: no tiles can be shifted"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

    # def test300_010_shouldSwipeRight(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "right"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["score"] = 0
    #     resboardDictionary = {}
    #     resboardDictionary["columnCount"] = 4
    #     resboardDictionary["rowCount"] = 4
    #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    #     resultDictionary["board"] = resboardDictionary
    #     resultDictionary["gameStatus"] = "underway"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)
    #
    # def test300_020_shouldSwipeRight(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "right"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["score"] = 4
    #     resboardDictionary = {}
    #     resboardDictionary["columnCount"] = 4
    #     resboardDictionary["rowCount"] = 4
    #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2]
    #     resultDictionary["board"] = resboardDictionary
    #     resultDictionary["gameStatus"] = "underway"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)
    #
    # def test300_030_validateNoTilesShift(self):
    #     inputDictionary = {}
    #     inputDictionary["op"] = "swipe"
    #     inputDictionary["direction"] = "right"
    #     boardDictionary = {}
    #     boardDictionary["rowCount"] = 4
    #     boardDictionary["columnCount"] = 4
    #     gridList = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
    #     boardDictionary["grid"] = gridList
    #     inputDictionary["board"] = boardDictionary
    #     resultDictionary = {}
    #     resultDictionary["score"] = 0
    #     resboardDictionary = {}
    #     resboardDictionary["columnCount"] = 4
    #     resboardDictionary["rowCount"] = 4
    #     resboardDictionary["grid"] = [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    #     resultDictionary["board"] = resboardDictionary
    #     resultDictionary["gameStatus"] = "underway"
    #     outputDictionary = swipeGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

        # def test400_010_shouldSwipeUp(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "up"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 4
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test400_020_shouldSwipeUp(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "up"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 4
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test400_030_shouldSwipeUp(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "up"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 0
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test400_040_shouldSwipeUp(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "up"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 8
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)

        # def test500_010_shouldSwipeDown(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "down"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 4
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test500_020_shouldSwipeDown(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "down"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 4
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test500_030_shouldSwipeDown(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "down"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 0
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)
        #
        # def test500_040_shouldSwipeDown(self):
        #     inputDictionary = {}
        #     inputDictionary["op"] = "swipe"
        #     inputDictionary["direction"] = "down"
        #     boardDictionary = {}
        #     boardDictionary["rowCount"] = 4
        #     boardDictionary["columnCount"] = 4
        #     gridList = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]
        #     boardDictionary["grid"] = gridList
        #     inputDictionary["board"] = boardDictionary
        #     resultDictionary = {}
        #     resultDictionary["score"] = 8
        #     resboardDictionary = {}
        #     resboardDictionary["columnCount"] = 4
        #     resboardDictionary["rowCount"] = 4
        #     resboardDictionary["grid"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3]
        #     resultDictionary["board"] = resboardDictionary
        #     resultDictionary["gameStatus"] = "underway"
        #     outputDictionary = swipeGame(inputDictionary)
        #     self.assertEquals(resultDictionary, outputDictionary)

        def test600_010_shouldValidateGridElementsLE2timesrowcol(self):
            inputDictionary = {}
            inputDictionary["op"] = "swipe"
            inputDictionary["direction"] = "down"
            boardDictionary = {}
            boardDictionary["rowCount"] = 2
            boardDictionary["columnCount"] = 2
            gridList = [5,4,0,0]
            boardDictionary["grid"] = gridList
            inputDictionary["board"] = boardDictionary
            resultDictionary = {}
            resultDictionary["gameStatus"] = "error: Each item in the grid must be LE (rowCount * columnCount)"
            outputDictionary = swipeGame(inputDictionary)
            self.assertEquals(resultDictionary,outputDictionary)


        def test600_020_shouldValidateGridElementsLE2timesrowcol(self):
            inputDictionary = {}
            inputDictionary["op"] = "swipe"
            inputDictionary["direction"] = "down"
            boardDictionary = {}
            boardDictionary["columnCount"] = 2
            boardDictionary["rowCount"] = 2
            gridList = [0,1,5,0]
            boardDictionary["grid"] = gridList
            inputDictionary["board"] = boardDictionary
            resultDictionary = {}
            resultDictionary["gameStatus"] = "error: Each item in the grid must be LE (rowCount * columnCount)"
            outputDictionary = swipeGame(inputDictionary)
            self.assertEquals(resultDictionary, outputDictionary)