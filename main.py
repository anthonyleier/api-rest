from flask import Flask
from flask_restful import Api
from usuarios import UsuariosGeral, UsuarioPorID

app = Flask(__name__)
api = Api(app)

api.add_resource(UsuariosGeral, '/users')
api.add_resource(UsuarioPorID, '/users/<id>')

if __name__ == '__main__':
    app.run()
