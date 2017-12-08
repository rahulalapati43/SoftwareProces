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