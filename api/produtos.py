from flask import request, jsonify, make_response
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
        json = jsonify(produto)
        resposta = make_response(json, 201)
        return resposta


class ProdutoPorID(Resource):
    def get(self, id):
        produto = getProduto(id)
        json = jsonify(produto)
        resposta = make_response(json, 200)
        return resposta

    def put(self, id):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']
        produto = atualizarProduto(nome, descricao, valor, imagem, id)
        json = jsonify(produto)
        resposta = make_response(json, 200)
        return resposta

    def delete(self, id):
        produto = deletarProduto(id)
        json = jsonify(produto)
        resposta = make_response(json, 200)
        return resposta
