from flask import request, jsonify, make_response
from flask_restful import Resource
from funcoes.usuarios import getListaUsuarios, criarUsuario
from funcoes.usuarios import getUsuario, atualizarUsuario, deletarUsuario


class Usuarios(Resource):
    def get(self):
        listaUsuarios = getListaUsuarios()
        json = jsonify(listaUsuarios)
        resposta = make_response(json, 200)
        return resposta

    def post(self):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        usuario = criarUsuario(nome, email, senha)
        json = jsonify(usuario)
        resposta = make_response(json, 201)
        return resposta


class UsuarioPorID(Resource):
    def get(self, id):
        usuario = getUsuario(id)
        json = jsonify(usuario)
        resposta = make_response(json, 200)
        return resposta

    def put(self, id):
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        usuario = atualizarUsuario(nome, email, senha, id)
        json = jsonify(usuario)
        resposta = make_response(json, 200)
        return resposta

    def delete(self, id):
        usuario = deletarUsuario(id)
        json = jsonify(usuario)
        resposta = make_response(json, 200)
        return resposta
