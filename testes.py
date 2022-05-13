import unittest
import requests
from config import baseDelivery


url = "http://localhost:5000/"


def formatarTexto(texto):
    texto = texto.replace("\n", "")
    texto = texto.replace(" ", "")
    return texto


class UsuarioTestes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('estrutura.sql', 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            baseDelivery.executar(dados)

    def test_getUsuario(self):
        pass

    def test_getListaUsuarios(self):
        endpoint = url + "usuarios"
        request = requests.get(endpoint)
        texto = formatarTexto(request.text)
        exemplo = '{"email":"lucas.carvalho@gmail.com","id":3,"nome":"LucasCarvalho","senha":"lucas123"}'
        self.assertIn(exemplo, texto)

    def test_criarUsuario(self):
        pass

    def test_atualizarUsuario(self):
        pass

    def test_deletarUsuario(self):
        pass


if __name__ == '__main__':
    unittest.main()
