from flask import request, jsonify
from flask_restful import Resource
from config import baseDelivery


class Produtos(Resource):
    def get(self):
        query = f"SELECT * FROM produto;"
        dadosProdutos = baseDelivery.selecionar(query)

        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta

    def post(self):
        pass


class ProdutoPorID(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
