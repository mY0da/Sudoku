import unittest
import Jogo_final

class TestSudoku(unittest.TestCase):

    def test_check(self):
        result = Jogo_final.check(([[5, 6, ' ', 4, 9, 7, 8, 2, 3],
                [3, 4, 2, 1, 8, 5, 7, 9, 6],
                [7, 9, 8, 2, 3, 6, 5, 1, 4],
                [6, 3, 9, 7, 4, 2, 1, 8, 5],
                [8, 7, 4, 5, 1, 3, 2, 6, 9],
                [1, 2, 5, 8, 6, 9, 3, 4, 7],
                [2, 1, 6, 3, 5, 4, 9, 7, 8],
                [9, 5, 7, 6, 2, 8, 4, 3, 1],
                [4, 8, 3, 9, 7, 1, 6, 5, 2]]), 0, 2, 3)
        self.assertEqual(result, 4)