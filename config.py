from banco import Banco
from flask import request, make_response

ipAcesso = 'database'
nomeBanco = 'delivery'

baseDelivery = Banco(ipAcesso, nomeBanco)


def validarChave(apiKey):
    query = "SELECT chave FROM chave_acesso;"
    chaves = baseDelivery.selecionar(query)
    chave = {'chave': apiKey}
    return chave in chaves


def chaveNecessaria(funcao):
    def verificarChave(*args, **kwargs):
        if request.json:
            apiKey = request.json.get("api_key")

            if validarChave(apiKey):
                return funcao(*args, **kwargs)
        else:
            mensagem = "API Key não reconhecida. Por favor, utilize uma API Key válida."
            statusCode = 400
            resposta = make_response({"mensagem": mensagem}, statusCode)
            return resposta

    return verificarChave
