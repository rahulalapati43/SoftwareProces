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

     def test100_020_shouldValidatemissingdirection(self):
         inputDictionary = {}
         inputDictionary["op"] = "swipe"
         resultDictionary = {}
         resultDictionary["gameStatus"] = "error: missing direction"
         outputDictionary = swipeGame(inputDictionary)
         self.assertEquals(resultDictionary,outputDictionary)