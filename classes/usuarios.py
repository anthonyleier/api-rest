from flask import request, jsonify
from flask_restful import Resource
from config import baseDelivery


class Usuarios(Resource):
    def get(self):
        query = "SELECT * FROM usuario;"
        dadosUsuarios = baseDelivery.selecionar(query)

        jsonResposta = jsonify(dadosUsuarios)
        return jsonResposta

    def post(self):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']

        query = f"""
        INSERT INTO usuario (nome, email, senha)
        VALUES (%s, %s, %s)
        RETURNING ID;
        """
        parametros = (nome, email, senha)
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta


class UsuarioPorID(Resource):
    def get(self, id):
        query = f"SELECT * FROM usuario WHERE id = %s;"
        parametros = [id]
        dadosUsuario = baseDelivery.selecionarUm(query, parametros)

        jsonResposta = jsonify(dadosUsuario)
        return jsonResposta

    def put(self, id):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']

        query = f"""
        UPDATE usuario SET nome = %s, email = %s, senha = %s
        WHERE id = %s RETURNING ID;
        """
        parametros = [nome, email, senha, id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta

    def delete(self, id):
        query = f"DELETE FROM usuario WHERE id = %s RETURNING ID;"
        parametros = [id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
        return jsonResposta
