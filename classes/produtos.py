from flask import request, jsonify
from flask_restful import Resource
from config import baseBlog


class Produtos(Resource):
    def get(self):
        query = 'SELECT * FROM produtos;'
        dadosProdutos = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta

    def post(self):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        INSERT INTO produtos (titulo, texto, usuario)
        VALUES ('{titulo}', '{texto}', {usuario});
        """
        baseBlog.executar(query)

        query = f"SELECT * FROM produtos WHERE usuario = '{usuario}';"
        dadosProdutos = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta


class ProdutoPorID(Resource):
    def get(self, id):
        query = f"SELECT * FROM produtos WHERE id = {id};"
        dadosProdutos = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta

    def put(self, id):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        UPDATE produtos SET 
        titulo = '{titulo}', 
        texto = '{texto}',
        usuario = '{usuario}'
        WHERE id = {id};
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM produtos
        WHERE id = {id};
        """
        dadosProdutos = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosProdutos)
        return jsonResposta

    def delete(self, id):
        query = f"DELETE FROM produtos WHERE id = {id};"
        baseBlog.executar(query)

        jsonResposta = jsonify({'status': 'success'})
        return jsonResposta
