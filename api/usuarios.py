from flask import request
from utils import montarResposta
from flask_restful import Resource
from funcoes.usuarios import getListaUsuarios, criarUsuario
from funcoes.usuarios import getUsuario, atualizarUsuario, deletarUsuario


class Usuarios(Resource):
    def get(self):
        listaUsuarios = getListaUsuarios()
        resposta = montarResposta(listaUsuarios)
        return resposta

    def post(self):
        try:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            usuario = criarUsuario(nome, email, senha)
            resposta = montarResposta(usuario)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500


class UsuarioPorID(Resource):
    def get(self, id):
        usuario = getUsuario(id)
        resposta = montarResposta(usuario)
        return resposta

    def put(self, id):
        try:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            usuario = atualizarUsuario(nome, email, senha, id)
            resposta = montarResposta(usuario)
            return resposta
        except:
            return {'mensagem': 'Erro na aplicação: campos faltantes'}, 500

    def delete(self, id):
        usuario = deletarUsuario(id)
        resposta = montarResposta(usuario)
        return resposta
