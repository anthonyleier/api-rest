from flask import request
from utils import montarResposta
from flask_restful import Resource
from funcoes.pedidos import getListaPedidos, criarPedido
from funcoes.pedidos import getPedido, atualizarProdutoPedido, deletarPedido


class Pedidos(Resource):
    def get(self):
        listaPedidos = getListaPedidos()
        resposta = montarResposta(listaPedidos)
        return resposta

    def post(self):
        try:
            usuario = request.json['usuario']
            produtos = request.json['produtos']
            quantidades = request.json['quantidades']
            pedido = criarPedido(usuario, produtos, quantidades)
            resposta = montarResposta(pedido)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500


class PedidoPorID(Resource):
    def get(self, id):
        pedido = getPedido(id)
        resposta = montarResposta(pedido)
        return resposta

    def put(self, id):
        try:
            usuario = request.json['usuario']
            produtos = request.json['produtos']
            quantidades = request.json['quantidades']
            pedido = atualizarProdutoPedido(usuario, produtos, quantidades, id)
            resposta = montarResposta(pedido)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500

    def delete(self, id):
        pedido = deletarPedido(id)
        resposta = montarResposta(pedido)
        return resposta
