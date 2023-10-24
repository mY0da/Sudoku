import unittest
import Jogo_final

class TestSudoku(unittest.TestCase):

    def test_jogada_1(self):
        #ação = c
        result = Jogo_final.jogada([
            [5, 6, " ", " ", " ", " ", " ", " ", 3],
            [" ", " ", 2, " ", " ", " ", 7, " ", " "],
            [" ", 9, " ", " ", 3, " ", " ", 1, " "],
            [" ", " ", 9, " ", " ", 2, " ", " ", " "],
            [" ", 7, " ", " ", " ", " ", " ", 6, " "],
            [" ", " ", " ", 8, " ", " ", 3, " ", " "],
            [" ", 1, " ", " ", 5, " ", " ", 7, " "],
            [" ", " ", 7, " ", " ", " ", 4, " ", " "],
            [4, " ", " ", " ", " ", " ", " ", 5, 2]], [
            [5, 6, " ", " ", " ", " ", " ", " ", 3],
            [" ", " ", 2, " ", " ", " ", 7, " ", " "],
            [" ", 9, " ", " ", 3, " ", " ", 1, " "],
            [" ", " ", 9, " ", " ", 2, " ", " ", " "],
            [" ", 7, " ", " ", " ", " ", " ", 6, " "],
            [" ", " ", " ", 8, " ", " ", 3, " ", " "],
            [" ", 1, " ", " ", 5, " ", " ", 7, " "],
            [" ", " ", 7, " ", " ", " ", 4, " ", " "],
            [4, " ", " ", " ", " ", " ", " ", 5, 2]], [
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True]])
        self.assertEqual(result, 2)

    def test_jogada_2(self):
        #ação = p
        result = Jogo_final.jogada([
            [5, 6, " ", " ", " ", " ", " ", " ", 3],
            [" ", " ", 2, " ", " ", " ", 7, " ", " "],
            [" ", 9, " ", " ", 3, " ", " ", 1, " "],
            [" ", " ", 9, " ", " ", 2, " ", " ", " "],
            [" ", 7, " ", " ", " ", " ", " ", 6, " "],
            [" ", " ", " ", 8, " ", " ", 3, " ", " "],
            [" ", 1, " ", " ", 5, " ", " ", 7, " "],
            [" ", " ", 7, " ", " ", " ", 4, " ", " "],
            [4, " ", " ", " ", " ", " ", " ", 5, 2]], [
            [5, 6, " ", " ", " ", " ", " ", " ", 3],
            [" ", " ", 2, " ", " ", " ", 7, " ", " "],
            [" ", 9, " ", " ", 3, " ", " ", 1, " "],
            [" ", " ", 9, " ", " ", 2, " ", " ", " "],
            [" ", 7, " ", " ", " ", " ", " ", 6, " "],
            [" ", " ", " ", 8, " ", " ", 3, " ", " "],
            [" ", 1, " ", " ", 5, " ", " ", 7, " "],
            [" ", " ", 7, " ", " ", " ", 4, " ", " "],
            [4, " ", " ", " ", " ", " ", " ", 5, 2]], [
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True]])
        self.assertEqual(result, 163)