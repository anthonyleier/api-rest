from flask import request
from flask_restful import Resource
from config import baseBlog
from funcoes import gerarJson


class Usuarios(Resource):
    def get(self):
        query = 'SELECT * FROM usuario;'
        dadosUsuarios = baseBlog.selecionar(query)
        jsonRetorno = gerarJson(dadosUsuarios)
        return jsonRetorno

    def post(self):
        nome = request.json['nome']
        email = request.json['email']

        query = f"""
        INSERT INTO usuario (nome, email)
        VALUES ('{nome}', '{email}');
        """

        baseBlog.executar(query)
        return 0

    def put(self):
        id = request.json['id']
        nome = request.json['nome']
        email = request.json['email']

        query = f"""
        UPDATE usuario SET 
        nome = '{nome}', email = '{email}'
        WHERE id = {id};
        """

        baseBlog.executar(query)
        return 0
