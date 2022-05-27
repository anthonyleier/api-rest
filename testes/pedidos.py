import unittest
import requests


dominio = "http://localhost:5000/"
autenticacao = {'api_key': '974ff5366ebab83585cf8406e8548ca3', 'Content-Type': 'application/json'}


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

        pedidoTeste3 = {
            "usuario": 17,
            "produtos": [2, 4, 5],
            "quantidades": [4, 8, 12]
        }

        endpoint = "pedidos"
        url = dominio + endpoint

        json = {**pedidoTeste1, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo1 = requestJSON['id']

        json = {**pedidoTeste2, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo2 = requestJSON['id']

        json = {**pedidoTeste3, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo3 = requestJSON['id']

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

        json = {**pedidoTeste, **autenticacao}
        request = requests.post(url, json=json)

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

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

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

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(pedidoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_excluirPedido(self):
        endpoint = f"pedidos/{self.pedidoExemplo3}"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


class PedidoTestesFalhas(unittest.TestCase):
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

        json = {**pedidoTeste1, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo1 = requestJSON['id']

        json = {**pedidoTeste2, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo2 = requestJSON['id']

    def test_getPedido_inexistente(self):
        jsonEsperado = {"mensagem": "Pedido não encontrado"}

        endpoint = "pedidos/1258"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(404, statusCode)

    def test_criarPedido_quantidadeNegativa(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este pedido"}

        pedidoTeste = {
            "usuario": 1225,
            "produtos": [432, 545],
            "quantidades": [-1, -1]
        }

        endpoint = "pedidos"
        url = dominio + endpoint

        json = {**pedidoTeste, **autenticacao}
        request = requests.post(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarProdutoPedido_inexistente(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este pedido"}

        produtoTeste = {
            "usuario": 5,
            "produtos": [2, 4, 5],
            "quantidades": [-2, -2, -2]
        }

        endpoint = f"pedidos/7865"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarProdutoPedido_usuarioInexistente(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este pedido"}

        produtoTeste = {
            "usuario": 1545,
            "produtos": [1, 2, 4],
            "quantidades": [1, 2, 3]
        }

        endpoint = f"pedidos/{self.pedidoExemplo1}"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarProdutoPedido_chaveInvalida(self):
        jsonEsperado = {"mensagem": "API Key não reconhecida. Por favor, utilize uma API Key válida."}

        produtoTeste = {
            "usuario": 5,
            "produtos": [2, 4, 5],
            "quantidades": [-2, -2, -2]
        }

        endpoint = f"pedidos/{self.pedidoExemplo2}"
        url = dominio + endpoint

        autenticacao = {'api_key': '2fb74eed31df38eead96278c6349b8fe', 'Content-Type': 'application/json'}
        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(400, statusCode)

    def test_excluirPedido_inexistente(self):
        jsonEsperado = {"mensagem": "Pedido não encontrado"}

        endpoint = "pedidos/598"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(404, statusCode)


if __name__ == '__main__':
    unittest.main()
