import unittest
import requests


dominio = "http://localhost:5000/"


class PedidoTestes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pedidoTeste1 = {
            "usuario": 13,
            "produtos": [2, 4, 5],
            "quantidades": [4, 8, 12]
        }

        pedidoTeste2 = {
            "usuario": 15,
            "produtos": [2, 4, 5],
            "quantidades": [4, 8, 12]
        }

        endpoint = "pedidos"
        url = dominio + endpoint

        request = requests.post(url, json=pedidoTeste1)
        requestJSON = request.json()
        cls.pedidoExemplo1 = requestJSON['id']

        request = requests.post(url, json=pedidoTeste2)
        requestJSON = request.json()
        cls.pedidoExemplo2 = requestJSON['id']

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
        self.assertEqual(201, statusCode)

    def test_atualizarProdutoPedido_adicionar(self):
        produtoTeste = {
            "usuario": 15,
            "produtos": [1, 2, 4],
            "quantidades": [1, 2, 3]
        }

        pedidoTeste = {
            "usuario": 15,
            "produtos": [1, 2, 4, 5],
            "quantidades": [1, 6, 11, 12]
        }

        endpoint = f"pedidos/{self.pedidoExemplo1}"
        url = dominio + endpoint

        request = requests.put(url, json=produtoTeste)
        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_atualizarProdutoPedido_remover(self):
        produtoTeste = {
            "usuario": 5,
            "produtos": [2, 4, 5],
            "quantidades": [-2, -2, -2]
        }

        pedidoTeste = {
            "usuario": 5,
            "produtos": [2, 4, 5],
            "quantidades": [2, 6, 10]
        }

        endpoint = f"pedidos/{self.pedidoExemplo2}"
        url = dominio + endpoint

        request = requests.put(url, json=produtoTeste)
        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

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
