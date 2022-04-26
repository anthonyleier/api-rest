from flask import request, jsonify
from flask_restful import Resource
from config import baseDelivery


class Produtos(Resource):
    def get(self):
        query = "SELECT * FROM produto;"
        dadosProdutos = baseDelivery.selecionar(query)

        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta

    def post(self):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']

        query = """
        INSERT INTO produto (nome, descricao, valor, imagem)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        parametros = [nome, descricao, valor, imagem]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta


class ProdutoPorID(Resource):
    def get(self, id):
        query = "SELECT * FROM produto WHERE id = %s;"
        parametros = [id]
        dadosProduto = baseDelivery.selecionarUm(query, parametros)

        jsonResposta = jsonify(dadosProduto)
        return jsonResposta

    def put(self, id):
        nome = request.json['nome']
        descricao = request.json['descricao']
        valor = request.json['valor']
        imagem = request.json['imagem']

        query = """
        UPDATE produto SET nome = %s, descricao = %s, valor = %s, imagem = %s
        WHERE id = %s RETURNING id;
        """
        parametros = [nome, descricao, valor, imagem, id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta

    def delete(self, id):
        query = "DELETE FROM produto WHERE id = %s RETURNING id;"
        parametros = [id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta
