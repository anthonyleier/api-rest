import unittest
import requests


dominio = "http://localhost:5000/"


class UsuarioTestes(unittest.TestCase):
    def test_getUsuario(self):
        usuarioTeste = {"id": 12, "nome": "Lara Costa", "email": "lara.costa@hotmail.com", "senha": "lara123"}

        endpoint = "usuarios/12"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(usuarioTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_getListaUsuarios(self):
        usuarioTeste1 = {"id": 3, "nome": "Lucas Carvalho", "email": "lucas.carvalho@gmail.com", "senha": "lucas123"}
        usuarioTeste2 = {"id": 4, "nome": "Rafaela Barros", "email": "rafaela.barros@gmail.com", "senha": "rafaela123"}
        usuarioTeste3 = {"id": 14, "nome": "Gabrielly Fernandes", "email": "gabrielly.fernandes@hotmail.com", "senha": "gabrielly123"}

        endpoint = "usuarios"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertIn(usuarioTeste1, requestJSON)
        self.assertIn(usuarioTeste2, requestJSON)
        self.assertIn(usuarioTeste3, requestJSON)
        self.assertEqual(200, statusCode)

    def test_criarUsuario(self):
        usuarioTeste = {'nome': 'Luke Skywalker', 'email': 'lukeskywalker@gmail.com', 'senha': 'luke123'}

        endpoint = "usuarios"
        url = dominio + endpoint

        request = requests.post(url, json=usuarioTeste)
        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(usuarioTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_atualizarUsuario(self):
        usuarioTeste = {'id': 5, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}

        endpoint = "usuarios/5"
        url = dominio + endpoint

        request = requests.put(url, json=usuarioTeste)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(usuarioTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_deletarUsuario(self):
        endpoint = "usuarios/10"
        url = dominio + endpoint

        request = requests.delete(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


if __name__ == '__main__':
    unittest.main()
