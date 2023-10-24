import unittest
import Jogo_final

class TestSudoku(unittest.TestCase):

    def test_salvar(self):
        result = Jogo_final.salvar(20, 700, 100)
        self.assertEqual(result, 620)