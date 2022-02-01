from flask import Flask
from flask_restful import Api
from usuarios import Usuarios
from usuarioID import UsuarioById

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuarios, '/users')
api.add_resource(UsuarioById, '/users/<id>')

if __name__ == '__main__':
    app.run()
