import unittest
import requests


dominio = "http://localhost:5000/"
autenticacao = {'api_key': '974ff5366ebab83585cf8406e8548ca3', 'Content-Type': 'application/json'}


class ProdutoTestes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        produtoTeste = {
            "nome": 'X-Contra Filé',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e contra filé.',
            "valor": 19.0,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff28c23895.png'
        }

        endpoint = "produtos"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.post(url, json=json)

        requestJSON = request.json()
        cls.pedidoExemplo = requestJSON['id']

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

        json = {**produtoTeste, **autenticacao}
        request = requests.post(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()
        requestJSON.pop('id', None)

        self.assertEqual(produtoTeste, requestJSON)
        self.assertEqual(201, statusCode)

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

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(produtoTeste, requestJSON)
        self.assertEqual(200, statusCode)

    def test_deletarProduto(self):
        endpoint = f"produtos/{self.pedidoExemplo}"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertTrue(requestJSON)
        self.assertEqual(200, statusCode)


class ProdutoTestesFalhas(unittest.TestCase):
    def test_getProduto_inexistente(self):
        jsonEsperado = {"mensagem": "Produto não encontrado"}

        endpoint = "produtos/456"
        url = dominio + endpoint

        request = requests.get(url)
        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(404, statusCode)

    def test_criarProduto_valorNegativo(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este produto"}

        produtoTeste = {
            "nome": 'X-Contra Filé',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e contra filé.',
            "valor": -50,
            "imagem": 'https://static.deliverymuch.com.br/images/products/602ff28c23895.png'
        }

        endpoint = "produtos"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.post(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarProduto_inexistente(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este produto"}

        produtoTeste = {
            "nome": 'X-Picanha',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e picanha.',
            "valor": 20,
            "imagem": 'https://static.deliverymuch.com.br/images/products/6021880d5b686.png'
        }

        endpoint = "produtos/478"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_atualizarProduto_valorNegativo(self):
        jsonEsperado = {"mensagem": "Ocorreu um erro ao processar este produto"}

        produtoTeste = {
            "nome": 'X-Picanha',
            "descricao": 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e picanha.',
            "valor": -20,
            "imagem": 'https://static.deliverymuch.com.br/images/products/6021880d5b686.png'
        }

        endpoint = "produtos/4"
        url = dominio + endpoint

        json = {**produtoTeste, **autenticacao}
        request = requests.put(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(500, statusCode)

    def test_deletarProduto_inexistente(self):
        jsonEsperado = {"mensagem": "Produto não encontrado"}

        endpoint = "produtos/45678"
        url = dominio + endpoint

        json = {**autenticacao}
        request = requests.delete(url, json=json)

        statusCode = request.status_code
        requestJSON = request.json()

        self.assertEqual(jsonEsperado, requestJSON)
        self.assertEqual(404, statusCode)


if __name__ == '__main__':
    unittest.main()
