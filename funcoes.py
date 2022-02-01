from flask import jsonify


def gerarJson(dados):
    dictDados = dict(dados)
    json = jsonify(dictDados)
    return json
