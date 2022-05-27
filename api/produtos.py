from flask import request
from utils import montarResposta
from flask_restful import Resource
from funcoes.produtos import getListaProdutos, criarProduto
from funcoes.produtos import getProduto, atualizarProduto, deletarProduto


class Produtos(Resource):
    def get(self):
        listaProdutos = getListaProdutos()
        resposta = montarResposta(listaProdutos)
        return resposta

    def post(self):
        try:
            nome = request.json['nome']
            descricao = request.json['descricao']
            valor = request.json['valor']
            imagem = request.json['imagem']
            produto = criarProduto(nome, descricao, valor, imagem)
            resposta = montarResposta(produto)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500


class ProdutoPorID(Resource):
    def get(self, id):
        produto = getProduto(id)
        resposta = montarResposta(produto)
        return resposta

    def put(self, id):
        try:
            nome = request.json['nome']
            descricao = request.json['descricao']
            valor = request.json['valor']
            imagem = request.json['imagem']
            produto = atualizarProduto(nome, descricao, valor, imagem, id)
            resposta = montarResposta(produto)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500

    def delete(self, id):
        produto = deletarProduto(id)
        resposta = montarResposta(produto)
        return resposta
