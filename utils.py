import os
from banco import Banco
from flask import jsonify, Response
from flask import request, make_response
from dotenv import load_dotenv


load_dotenv()
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
baseDelivery = Banco(host=DATABASE_HOST, database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, port=DATABASE_PORT)


def acessoBloqueado():
    mensagem = "API Key não reconhecida. Por favor, utilize uma API Key válida."
    statusCode = 400
    resposta = make_response({"mensagem": mensagem}, statusCode)
    return resposta


def validarChave(apiKey):
    query = "SELECT chave FROM chave_acesso;"
    chaves = baseDelivery.selecionar(query)
    chave = {'chave': apiKey}
    return chave in chaves


def chaveNecessaria(funcao):
    def verificarChave(*args, **kwargs):
        if request.json and validarChave(request.json.get("api_key")):
            return funcao(*args, **kwargs)
        else:
            return acessoBloqueado()
    return verificarChave


def montarResposta(recurso):
    if isinstance(recurso, dict) or isinstance(recurso, list) or isinstance(recurso, bool):
        json = jsonify(recurso)
        resposta = make_response(json, 200)

    elif isinstance(recurso, Response):
        resposta = recurso

    else:
        mensagem = "Ocorreu um erro ao processar este recurso"
        statusCode = 500
        resposta = make_response({"mensagem": mensagem}, statusCode)

    return resposta
