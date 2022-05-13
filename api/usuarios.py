from flask import request, jsonify
from flask_restful import Resource
from funcoes.usuarios import getListaUsuarios, criarUsuario
from funcoes.usuarios import getUsuario, atualizarUsuario, deletarUsuario


class Usuarios(Resource):
    def get(self):
        listaUsuarios = getListaUsuarios()
        json = jsonify(listaUsuarios)
        print(listaUsuarios)
        return json

    def post(self):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        usuario = criarUsuario(nome, email, senha)
        json = jsonify(usuario)
        return json


class UsuarioPorID(Resource):
    def get(self, id):
        usuario = getUsuario(id)
        json = jsonify(usuario)
        return json

    def put(self, id):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        usuario = atualizarUsuario(nome, email, senha, id)
        json = jsonify(usuario)
        return json

    def delete(self, id):
        usuario = deletarUsuario(id)
        json = jsonify(usuario)
        return json
