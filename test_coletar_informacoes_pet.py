import unittest
from io import StringIO
import sys
from unittest.mock import patch
from info_pet import validar_entrada_numerica, processar_informacoes

class TestColetarInformacoesPet(unittest.TestCase):

    def setUp(self):
        self.original_stdout = sys.stdout
        self.original_stdin = sys.stdin

    def tearDown(self):
        sys.stdout = self.original_stdout
        sys.stdin = self.original_stdin

    @patch('info_pet.messagebox.showerror')
    def test_validar_entrada_numerica_inteiro(self, mock_showerror):
        entrada = StringIO('5\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 5)

    @patch('info_pet.messagebox.showerror')
    def test_validar_entrada_numerica_float(self, mock_showerror):
        entrada = StringIO('12.5\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Peso do pet (em kg): ", tipo=float)
        self.assertEqual(resultado, 12.5)

    @patch('info_pet.messagebox.showerror')
    def test_validar_entrada_numerica_negativo(self, mock_showerror):
        entrada = StringIO('-5\n0\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 0)

    @patch('info_pet.messagebox.showerror')
    def test_validar_entrada_numerica_invalida(self, mock_showerror):
        entrada = StringIO('abc\n10\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 10)

    @patch('info_pet.messagebox.showinfo')
    def test_processar_informacoes(self, mock_showinfo):
        mock_showinfo.return_value = None
        resultado = processar_informacoes("Rex", 3, 15.2)
        esperado = "Nome: Rex\nIdade: 3 anos\nPeso: 15.2 kg"
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
