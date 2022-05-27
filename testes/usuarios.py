import unittest
import requests


dominio = "http://localhost:5000/"
autenticacao = {'api_key': '974ff5366ebab83585cf8406e8548ca3', 'Content-Type': 'application/json'}
jsonErro = {"mensagem": "Ocorreu um erro ao processar este recurso"}


class UsuarioTestes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        usuarioTeste = {'nome': 'Luke Skywalker', 'email': 'lukeskywalker@gmail.com', 'senha': 'luke123'}

        endpoint = "usuarios"
        url = dominio + endpoint

        json = {**usuarioTeste, **autenticacao}
        request = requests.post(url, json=json)
        requestJSON = request.json()

        cls.usuarioExemplo = requestJSON['id']

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

        json = {**usuarioTeste, **autenticacao}
        request = requests.post(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(usuarioTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_atualizarUsuario(self):
        usuarioTeste = {'id': 5, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}

        endpoint = "usuarios/5"
        url = dominio + endpoint

        json = {**usuarioTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(usuarioTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_deletarUsuario(self):
        endpoint = f"usuarios/{self.usuarioExemplo}"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


class UsuarioTestesFalhas(unittest.TestCase):
    def test_getUsuario_inexistente(self):
        endpoint = "usuarios/7456"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonErro, requestJSON)
        self.assertEqual(500, statusCode)

    def test_criarUsuario_camposFaltantes(self):
        jsonErro = {"mensagem": "Erro na aplicação: campos faltantes"}
        usuarioTeste = {'nome': 'Luke Skywalker', 'senha': 'luke123'}

        endpoint = "usuarios"
        url = dominio + endpoint

        json = {**usuarioTeste, **autenticacao}
        request = requests.post(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonErro, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarUsuario_inexistente(self):
        usuarioTeste = {'id': 5, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}

        endpoint = "usuarios/5789"
        url = dominio + endpoint

        json = {**usuarioTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonErro, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarUsuario_chaveInvalida(self):
        jsonErro = {"mensagem": "API Key não reconhecida. Por favor, utilize uma API Key válida."}
        usuarioTeste = {'id': 5, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}

        endpoint = "usuarios/5"
        url = dominio + endpoint

        autenticacao = {'api_key': '2fb74eed31df38eead96278c6349b8fe', 'Content-Type': 'application/json'}
        json = {**usuarioTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonErro, requestJSON)
        self.assertEqual(400, statusCode)

    def test_deletarUsuario_inexistente(self):
        endpoint = "usuarios/7897"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(jsonErro, requestJSON)
        self.assertEqual(500, statusCode)


if __name__ == '__main__':
    unittest.main()
