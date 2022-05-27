import os
from banco import Banco
from flask import jsonify, Response
from flask import request, make_response


database_host = os.getenv('DATABASE_HOST', 'database')
database_nome = os.getenv('DATABASE_NOME', 'delivery')
baseDelivery = Banco(database_host, database_nome)


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
