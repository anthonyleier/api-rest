from flask import request, jsonify
from flask_restful import Resource
from funcoes.produtos import getListaProdutos, criarProduto
from funcoes.produtos import getProduto, atualizarProduto, deletarProduto


class Produtos(Resource):
    def get(self):
        listaProdutos = getListaProdutos()
        json = jsonify(listaProdutos)
        return json

    def post(self):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']
        produto = criarProduto(nome, descricao, valor, imagem)
        json = jsonify(produto)
        return json


class ProdutoPorID(Resource):
    def get(self, id):
        produto = getProduto(id)
        json = jsonify(produto)
        return json

    def put(self, id):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']
        produto = atualizarProduto(nome, descricao, valor, imagem, id)
        json = jsonify(produto)
        return json

    def delete(self, id):
        produto = deletarProduto(id)
        json = jsonify(produto)
        return json
