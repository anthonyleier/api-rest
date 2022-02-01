
from flask_restful import Resource
from config import baseBlog
from funcoes import gerarJson


class UsuarioById(Resource):
    def get(self, id):
        query = f"SELECT * FROM usuario WHERE id = {id};"
        dados = baseBlog.selecionar(query)
        json = gerarJson(dados)
        return json

    def delete(self, id):
        query = f"DELETE FROM usuario WHERE id = {id};"
        baseBlog.executar(query)
        return 0
