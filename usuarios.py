from flask import request, jsonify
from flask_restful import Resource
from config import baseBlog


class UsuariosGeral(Resource):
    def get(self):
        query = 'SELECT * FROM usuario;'
        dadosUsuarios = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosUsuarios)
        return jsonResposta

    def post(self):
        nome = request.json['nome']
        email = request.json['email']

        query = f"""
        INSERT INTO usuario (nome, email)
        VALUES ('{nome}', '{email}');
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM usuario
        WHERE nome = '{nome}'
        AND email = '{email}';"""
        dadosUsuario = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosUsuario)
        return jsonResposta


class UsuarioPorID(Resource):
    def get(self, id):
        query = f"SELECT * FROM usuario WHERE id = {id};"
        dadosUsuario = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosUsuario)
        return jsonResposta

    def put(self, id):
        nome = request.json['nome']
        email = request.json['email']

        query = f"""
        UPDATE usuario SET 
        nome = '{nome}', email = '{email}'
        WHERE id = {id};
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM usuario
        WHERE id = {id};"""
        dadosUsuario = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosUsuario)
        return jsonResposta

    def delete(self, id):
        query = f"DELETE FROM usuario WHERE id = {id};"
        baseBlog.executar(query)

        jsonResposta = "{'status': 'success'}"
        return jsonResposta
