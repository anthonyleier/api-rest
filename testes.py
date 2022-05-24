import unittest
import requests


url = "http://localhost:5000/"


class UsuarioTestes(unittest.TestCase):
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
        dados = {'nome': 'Luke Skywalker', 'email': 'lukeskywalker@gmail.com', 'senha': 'luke123'}
        request = requests.post(endpoint, json=dados)
        json = request.json()
        json.pop('id', None)
        self.assertEqual(dados, json)
        self.assertEqual(200, request.status_code)

    def test_atualizarUsuario(self):
        endpoint = url + "usuarios/5"
        dados = {'id': 5, 'nome': 'Ahsoka Tano', 'email': 'ahsokatano@gmail.com', 'senha': 'ahsoka123'}
        request = requests.put(endpoint, json=dados)
        self.assertEqual(dados, request.json())
        self.assertEqual(200, request.status_code)

    def test_deletarUsuario(self):
        endpoint = url + "usuarios/10"
        request = requests.delete(endpoint)
        self.assertTrue(request.json)
        self.assertEqual(200, request.status_code)


class ProdutoTestes(unittest.TestCase):
    def test_getProduto(self):
        endpoint = url + "produtos/1"
        request = requests.get(endpoint)
        exemplo = {
            "id": 1,
            "nome": "X-Salada",
            "descricao": "Pão, maionese, alface, tomate, queijo e hambúrguer artesanal.",
            "valor": 11.0,
            "imagem": "https://static.deliverymuch.com.br/images/products/602ff217d5554.png"
        }
        self.assertEqual(exemplo, request.json())
        self.assertEqual(200, request.status_code)

    def test_getListaProdutos(self):
        endpoint = url + "produtos"
        request = requests.get(endpoint)

        exemplo1 = {
            "id": 2,
            "nome": 'X-Calabresa',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e calabresa.',
            "valor": 16,
            "imagem": 'https://static.deliverymuch.com.br/images/products/60217fc2316e8.png'
        }

        exemplo2 = {
            "id": 3,
            "nome": 'X-Bacon',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e bacon.',
            "valor": 17,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff18425507.png'
        }

        self.assertIn(exemplo1, request.json())
        self.assertIn(exemplo2, request.json())
        self.assertEqual(200, request.status_code)

    def test_criarProduto(self):
        endpoint = url + "produtos"

        dados = {
            "nome": 'X-Contra Filé',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e contra filé.',
            "valor": 19.0,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff28c23895.png'
        }

        request = requests.post(endpoint, json=dados)
        json = request.json()
        del json['id']
        self.assertEqual(dados, json)
        self.assertEqual(200, request.status_code)

    def test_atualizarProduto(self):
        endpoint = url + "produtos/4"

        dados = {
            "id": 4,
            "nome": 'X-Picanha',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e picanha.',
            "valor": 20,
            "imagem": 'https://static.deliverymuch.com.br/images/products/6021880d5b686.png'
        }

        request = requests.put(endpoint, json=dados)
        self.assertEqual(dados, request.json())
        self.assertEqual(200, request.status_code)

    def test_deletarProduto(self):
        endpoint = url + "produtos/6"
        request = requests.delete(endpoint)
        self.assertTrue(request.json)
        self.assertEqual(200, request.status_code)


if __name__ == '__main__':
    unittest.main()
