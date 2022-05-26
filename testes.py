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


class ProdutoTestes(unittest.TestCase):
    def test_getProduto(self):
        produtoTeste = {
            "id": 1,
            "nome": "X-Salada",
            "descricao": "Pão, maionese, alface, tomate, queijo e hambúrguer artesanal.",
            "valor": 11.0,
            "imagem": "https://static.deliverymuch.com.br/images/products/602ff217d5554.png"
        }

        endpoint = "produtos/1"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(produtoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_getListaProdutos(self):
        produtoTeste1 = {
            "id": 2,
            "nome": 'X-Calabresa',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e calabresa.',
            "valor": 16,
            "imagem": 'https://static.deliverymuch.com.br/images/products/60217fc2316e8.png'
        }

        produtoTeste2 = {
            "id": 3,
            "nome": 'X-Bacon',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e bacon.',
            "valor": 17,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff18425507.png'
        }

        produtoTeste3 = {
            "id": 5,
            "nome": 'X-Coração',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e coração.',
            "valor": 18,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602180428eaf5.png'
        }

        endpoint = "produtos"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertIn(produtoTeste1, requestJSON)
        self.assertIn(produtoTeste2, requestJSON)
        self.assertIn(produtoTeste3, requestJSON)
        self.assertEqual(200, statusCode)

    def test_criarProduto(self):
        produtoTeste = {
            "nome": 'X-Contra Filé',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e contra filé.',
            "valor": 19.0,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff28c23895.png'
        }

        endpoint = "produtos"
        url = dominio + endpoint

        request = requests.post(url, json=produtoTeste)
        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(produtoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_atualizarProduto(self):
        produtoTeste = {
            "id": 4,
            "nome": 'X-Picanha',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e picanha.',
            "valor": 20,
            "imagem": 'https://static.deliverymuch.com.br/images/products/6021880d5b686.png'
        }

        endpoint = "produtos/4"
        url = dominio + endpoint

        request = requests.put(url, json=produtoTeste)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(produtoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_deletarProduto(self):
        endpoint = "produtos/6"
        url = dominio + endpoint

        request = requests.delete(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


class PedidoTestes(unittest.TestCase):
    def test_getPedido(self):
        pedidoTeste = {
            "id": 1,
            "usuario": 1,
            "produtos": [1, 2],
            "quantidades": [1, 1]
        }

        endpoint = "pedidos/1"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_getListaPedidos(self):
        pedidoTeste1 = {
            "id": 2,
            "usuario": 2,
            "produtos": [2, 3],
            "quantidades": [1, 1]
        }

        pedidoTeste2 = {
            "id": 3,
            "usuario": 3,
            "produtos": [3, 4],
            "quantidades": [1, 1]
        }

        pedidoTeste3 = {
            "id": 4,
            "usuario": 4,
            "produtos": [4, 5],
            "quantidades": [1, 1]
        }

        endpoint = "pedidos"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertIn(pedidoTeste1, requestJSON)
        self.assertIn(pedidoTeste2, requestJSON)
        self.assertIn(pedidoTeste3, requestJSON)
        self.assertEqual(200, statusCode)

    def test_criarPedido(self):
        pedidoTeste = {
            "usuario": 11,
            "produtos": [2, 4],
            "quantidades": [1, 2]
        }

        endpoint = "pedidos"
        url = dominio + endpoint

        request = requests.post(url, json=pedidoTeste)
        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_atualizarProdutoPedido_adicionar(self):
        produtoTeste = {
            "usuario": 4,
            "produtos": [2, 5],
            "quantidades": [1, 1]
        }

        pedidoTeste = {
            "id": 5,
            "usuario": 4,
            "produtos": [1, 2, 5],
            "quantidades": [1, 2, 2]
        }

        endpoint = "pedidos/5"
        url = dominio + endpoint

        request = requests.put(url, json=produtoTeste)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    # def test_atualizarProdutoPedido_remover(self):
    #     produtoTeste = {
    #         "usuario": 5,
    #         "produtos": [2, 3, 4],
    #         "quantidades": [-1, -1, -1]
    #     }

    #     pedidoTeste = {
    #         "id": 7,
    #         "usuario": 5,
    #         "produtos": [2, 3],
    #         "quantidades": [0, 0]
    #     }

    #     endpoint = "pedidos/7"
    #     url = dominio + endpoint

    #     request = requests.put(url, json=produtoTeste)
    #     statusCode = request.status_code
    #     requestJSON = request.json()

    #     self.assertEqual(pedidoTeste, requestJSON)
    #     self.assertEqual(200, statusCode)

    def test_excluirPedido(self):
        endpoint = "pedidos/6"
        url = dominio + endpoint

        request = requests.delete(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


if __name__ == '__main__':
    unittest.main()
