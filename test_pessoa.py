"""
class Pessoa
    __init__
    nome str
    sobrenome str
    dados obtidos bool inicia como False

    API:
    obter todos os dados -> method
    ok
    404
"""

import unittest
from unittest.mock import patch

from Pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Luis', 'Fofinho')
        self.p2 = Pessoa('Maria', 'Miranda')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Luis')
        self.assertEqual(self.p2.nome, 'Maria')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)
    
    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Fofinho')
        self.assertEqual(self.p2.sobrenome, 'Miranda')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
        
            self.assertEqual(self.p1.obter_todos_os_dados(), 'Conectado')
            self.assertTrue(self.p1.dados_obtidos)

                 
            self.assertEqual(self.p2.obter_todos_os_dados(), 'Conectado')
            self.assertTrue(self.p2.dados_obtidos)
   

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
        
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)
    
    
    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True


            self.assertEqual(self.p1.obter_todos_os_dados(), 'Conectado')
            self.assertTrue(self.p1.dados_obtidos)

                 
            self.assertEqual(self.p2.obter_todos_os_dados(), 'Conectado')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)





if __name__=='__main__':
    unittest.main(verbosity=2)
