from unittest import TestCase
from IndigoGirls.statusGame import statusGame

class StatusGameTest(TestCase):
    # def test100_010_shouldValidatetiledefault(self):
    #     inputDictionary = {}
    #     resultDictionary = {}
    #     resultDictionary["tile"] = 2048
    #     outputDictionary = statusGame(inputDictionary)
    #     self.assertEquals(resultDictionary,outputDictionary)

    def test100_020_shouldValidatetileGE2(self):
        inputDictionary = {}
        inputDictionary["tile"] = 0
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: invalid tile value"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary,outputDictionary)

    def test200_010_shouldvalidateBoard(self):
        inputDictionary = {}
        inputDictionary["tile"] = 2
        boardDictionary = {}
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: missing board"
        outputDictionary = statusGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)


