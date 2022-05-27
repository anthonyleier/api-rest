from flask import request, jsonify, make_response, Response
from flask_restful import Resource
from funcoes.produtos import getListaProdutos, criarProduto
from funcoes.produtos import getProduto, atualizarProduto, deletarProduto


class Produtos(Resource):
    def get(self):
        listaProdutos = getListaProdutos()
        json = jsonify(listaProdutos)
        resposta = make_response(json, 200)
        return resposta

    def post(self):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']
        produto = criarProduto(nome, descricao, valor, imagem)

        if isinstance(produto, dict):
            json = jsonify(produto)
            resposta = make_response(json, 201)
        elif isinstance(produto, Response):
            resposta = produto
        else:
            mensagem = "Ocorreu um erro ao processar este produto"
            statusCode = 500
            resposta = make_response({"mensagem": mensagem}, statusCode)
        return resposta


class ProdutoPorID(Resource):
    def get(self, id):
        produto = getProduto(id)

        if produto:
            json = jsonify(produto)
            resposta = make_response(json, 200)
        else:
            mensagem = "Produto não encontrado"
            statusCode = 404
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta

    def put(self, id):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']
        produto = atualizarProduto(nome, descricao, valor, imagem, id)

        if isinstance(produto, dict):
            json = jsonify(produto)
            resposta = make_response(json, 200)
        elif isinstance(produto, Response):
            resposta = produto
        else:
            mensagem = "Ocorreu um erro ao processar este produto"
            statusCode = 500
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta

    def delete(self, id):
        produto = deletarProduto(id)

        if produto:
            json = jsonify(produto)
            resposta = make_response(json, 200)
        else:
            mensagem = "Produto não encontrado"
            statusCode = 404
            resposta = make_response({"mensagem": mensagem}, statusCode)

        return resposta
