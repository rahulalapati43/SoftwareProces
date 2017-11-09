from unittest import TestCase
from IndigoGirls.statusGame import statusGame

class StatusGameTest(TestCase):
    def test100_010_shouldValidatetiledefault(self):
        inputDictionary = {}
        resultDictionary = {}
        resultDictionary["tile"] = 2048
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary,outputDictionary)
