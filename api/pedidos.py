from flask import request, jsonify
from flask_restful import Resource
from funcoes.pedidos import getListaPedidos, criarPedido
from funcoes.pedidos import getPedido, atualizarPedido, deletarPedido


class Pedidos(Resource):
    def get(self):
        listaPedidos = getListaPedidos()
        json = jsonify(listaPedidos)
        return json

    def post(self):
        usuario = request.json['usuario']
        produtos = request.json['produtos']
        quantidades = request.json['quantidades']
        pedido = criarPedido(usuario, produtos, quantidades)
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
        pedido = atualizarPedido(usuario, produtos, id)
        json = jsonify(pedido)
        return json

    def delete(self, id):
        pedido = deletarPedido(id)
        json = jsonify(pedido)
        return json
