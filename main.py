from flask import Flask
from flask_restful import Api
from usuarios import UsuariosGeral, UsuarioPorID
from publicacoes import PublicacoesGeral, PublicacaoPorID

app = Flask(__name__)
api = Api(app)

api.add_resource(UsuariosGeral, '/usuarios')
api.add_resource(UsuarioPorID, '/usuarios/<id>')

api.add_resource(PublicacoesGeral, '/publicacoes')
api.add_resource(PublicacaoPorID, '/publicacoes/<id>')

if __name__ == '__main__':
    app.run()
