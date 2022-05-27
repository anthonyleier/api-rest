from flask import request, jsonify, make_response, Response
from flask_restful import Resource
from funcoes.pedidos import getListaPedidos, criarPedido
from funcoes.pedidos import getPedido, atualizarProdutoPedido, deletarPedido


class Pedidos(Resource):
    def get(self):
        listaPedidos = getListaPedidos()
        json = jsonify(listaPedidos)
        resposta = make_response(json, 200)
        return resposta

    def post(self):
        usuario = request.json['usuario']
        produtos = request.json['produtos']
        quantidades = request.json['quantidades']
        pedido = criarPedido(usuario, produtos, quantidades)

        if isinstance(pedido, dict):
            json = jsonify(pedido)
            resposta = make_response(json, 201)
        elif isinstance(pedido, Response):
            resposta = pedido
        else:
            mensagem = "Ocorreu um erro ao processar este pedido"
            statusCode = 500
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta


class PedidoPorID(Resource):
    def get(self, id):
        pedido = getPedido(id)

        if pedido:
            json = jsonify(pedido)
            resposta = make_response(json, 200)
        else:
            mensagem = "Pedido não encontrado"
            statusCode = 404
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta

    def put(self, id):
        usuario = request.json['usuario']
        produtos = request.json['produtos']
        quantidades = request.json['quantidades']
        pedido = atualizarProdutoPedido(usuario, produtos, quantidades, id)

        if isinstance(pedido, dict):
            json = jsonify(pedido)
            resposta = make_response(json, 200)
        elif isinstance(pedido, Response):
            resposta = pedido
        else:
            mensagem = "Ocorreu um erro ao processar este pedido"
            statusCode = 500
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta

    def delete(self, id):
        pedido = deletarPedido(id)

        if pedido:
            json = jsonify(pedido)
            resposta = make_response(json, 200)
        else:
            mensagem = "Pedido não encontrado"
            statusCode = 404
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta
