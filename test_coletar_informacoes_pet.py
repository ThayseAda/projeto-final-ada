import unittest
from io import StringIO
import sys

# Importa as funções que serão testadas
from info_pet import validar_entrada_numerica, coletar_informacoes_pet

class TestColetarInformacoesPet(unittest.TestCase):
    def test_validar_entrada_numerica_inteiro(self):
        entrada = StringIO('5\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 5)
        
    def test_validar_entrada_numerica_float(self):
        entrada = StringIO('12.5\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Peso do pet (em kg): ", tipo=float)
        self.assertEqual(resultado, 12.5)
    
    def test_validar_entrada_numerica_negativo(self):
        entrada = StringIO('-5\n0\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 0)
    
    def test_validar_entrada_numerica_invalida(self):
        entrada = StringIO('abc\n10\n')
        sys.stdin = entrada
        resultado = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)
        self.assertEqual(resultado, 10)
    
    def test_coletar_informacoes_pet(self):
        entrada = StringIO('Rex\n3\n15.2\n')
        sys.stdin = entrada
        saida = StringIO()
        sys.stdout = saida
        coletar_informacoes_pet()
        saida_esperada = "\nInformações do pet:\nNome: Rex\nIdade: 3 anos\nPeso: 15.2 kg\n"
        self.assertIn(saida_esperada.strip(), saida.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
