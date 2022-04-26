from flask import request, jsonify
from flask_restful import Resource
from config import baseDelivery


class Pedidos(Resource):
    def get(self):
        query = "SELECT * FROM pedido;"
        dadosPedidos = baseDelivery.selecionar(query)

        jsonResposta = jsonify(dadosPedidos)
        return jsonResposta

    def post(self):
        usuario = request.json['usuario']

        query = "INSERT INTO pedido (usuario) VALUES (%s) RETURNING id;"
        parametros = [usuario]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta


class PedidoPorID(Resource):
    def get(self, id):
        query = "SELECT * FROM pedido WHERE id = %s;"
        parametros = [id]
        dadosPedido = baseDelivery.selecionarUm(query, parametros)

        jsonResposta = jsonify(dadosPedido)
        return jsonResposta

    def put(self, id):
        usuario = request.json['usuario']

        query = "UPDATE pedido SET usuario = %s WHERE id = %s;"
        parametros = [usuario, id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta

    def delete(self, id):
        query = "DELETE FROM pedido WHERE id = %s;"
        parametros = [id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta
