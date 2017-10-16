from unittest import TestCase
from swipeGame import swipeGame

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

       def test100_090_shouldValidateGridElementsforatleast2ormoreelementsgreaterthan0(self):
           inputDictionary = {}
           inputDictionary["op"] = "swipe"
           inputDictionary["direction"] = "left"
           boardDictionary = {}
           boardDictionary["rowCount"] = 4
           boardDictionary["columnCount"] = 4
           gridList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
           boardDictionary["grid"] = gridList
           inputDictionary["board"] = boardDictionary
           resultDictionary = {}
           resultDictionary["gameStatus"] = "error: Each item in the grid must be GE 0"
           outputDictionary = swipeGame(inputDictionary)
           self.assertEquals(resultDictionary,outputDictionary)