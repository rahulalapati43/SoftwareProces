from unittest import TestCase
from IndigoGirls.recommendGame import recommendGame

class RecommendGameTest(TestCase):
    def test100_010_shouldvalidateMoves(self):
        inputDictionary = {}
        resultDictionary = {}
        resultDictionary["moves"] = 0
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)