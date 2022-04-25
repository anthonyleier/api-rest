from flask import request, jsonify
from flask_restful import Resource
from config import baseBlog


class PublicacoesGeral(Resource):
    def get(self):
        query = 'SELECT * FROM publicacao;'
        dadosPublicacoes = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosPublicacoes)
        return jsonResposta

    def post(self):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        INSERT INTO publicacao (titulo, texto, usuario)
        VALUES ('{titulo}', '{texto}', {usuario});
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM publicacao
        WHERE usuario = '{usuario}';
        """
        dadosPublicacoes = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosPublicacoes)
        return jsonResposta


class PublicacaoPorID(Resource):
    def get(self, id):
        query = f"SELECT * FROM publicacao WHERE id = {id};"
        dadosPublicacao = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosPublicacao)
        return jsonResposta

    def put(self, id):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        UPDATE publicacao SET 
        titulo = '{titulo}', 
        texto = '{texto}',
        usuario = '{usuario}'
        WHERE id = {id};
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM publicacao
        WHERE id = {id};
        """
        dadosPublicacao = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosPublicacao)
        return jsonResposta

    def delete(self, id):
        query = f"DELETE FROM publicacao WHERE id = {id};"
        baseBlog.executar(query)

        jsonResposta = jsonify({'status': 'success'})
        return jsonResposta
