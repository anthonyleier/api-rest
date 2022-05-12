from config import baseDelivery
from flask import request, jsonify
from flask_restful import Resource
from funcoes.pedidos import getListaPedidos, criarPedido, getPedido


class Pedidos(Resource):
    def get(self):
        listaPedidos = getListaPedidos()
        json = jsonify(listaPedidos)
        return json

    def post(self):
        usuario = request.json['usuario']
        produtos = request.json['produtos']
        pedido = criarPedido(usuario, produtos)
        json = jsonify(pedido)
        return json


class PedidoPorID(Resource):
    def get(self, id):
        pedido = getPedido(id)
        json = jsonify(pedido)
        return json

    def put(self, id):
        usuario = request.json['usuario']
        produtos = request.json['produtos']
        pedido = atualizarPedido(usuario, produtos)

        return jsonResposta

    def delete(self, id):
        query = "DELETE FROM pedido_produto WHERE pedido = %s;"
        parametros = [id]
        status = baseDelivery.executar(query, parametros)

        query = "DELETE FROM pedido WHERE id = %s;"
        parametros = [id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta
