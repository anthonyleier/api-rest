import unittest
import requests
from config import baseDelivery


url = "http://localhost:5000/"


class UsuarioTestes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('estrutura.sql', 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            baseDelivery.executar(dados)

    def test_getUsuario(self):
        endpoint = url + "usuarios/12"
        request = requests.get(endpoint)
        exemplo = {"id": 12, "nome": "Lara Costa", "email": "lara.costa@hotmail.com", "senha": "lara123"}
        self.assertEqual(exemplo, request.json())
        self.assertEqual(200, request.status_code)

    def test_getListaUsuarios(self):
        endpoint = url + "usuarios"
        request = requests.get(endpoint)
        exemplo1 = {"id": 3, "nome": "Lucas Carvalho", "email": "lucas.carvalho@gmail.com", "senha": "lucas123"}
        exemplo2 = {"id": 4, "nome": "Rafaela Barros", "email": "rafaela.barros@gmail.com", "senha": "rafaela123"}
        exemplo3 = {"id": 14, "nome": "Gabrielly Fernandes", "email": "gabrielly.fernandes@hotmail.com", "senha": "gabrielly123"}
        self.assertIn(exemplo1, request.json())
        self.assertIn(exemplo2, request.json())
        self.assertIn(exemplo3, request.json())
        self.assertEqual(200, request.status_code)

    def test_criarUsuario(self):
        endpoint = url + "usuarios"
        dados = {'id': 21, 'nome': 'Luke Skywalker', 'email': 'lukeskywalker@gmail.com', 'senha': 'luke123'}
        request = requests.post(endpoint, json=dados)
        self.assertEqual(dados, request.json())
        self.assertEqual(200, request.status_code)

    def test_atualizarUsuario(self):
        endpoint = url + "usuarios/2"
        dados = {'id': 2, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}
        request = requests.put(endpoint, json=dados)
        self.assertEqual(dados, request.json())
        self.assertEqual(200, request.status_code)

    def test_deletarUsuario(self):
        endpoint = url + "usuarios/1"
        request = requests.delete(endpoint)
        self.assertTrue(request.json)
        self.assertEqual(200, request.status_code)


if __name__ == '__main__':
    unittest.main()
