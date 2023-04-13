import os
from flask import Flask
from flask_restful import Api
from utils import baseDelivery
from api.pedidos import Pedidos, PedidoPorID
from api.usuarios import Usuarios, UsuarioPorID
from api.produtos import Produtos, ProdutoPorID

app = Flask(__name__)
api = Api(app)


api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioPorID, '/usuarios/<id>')


api.add_resource(Produtos, '/produtos')
api.add_resource(ProdutoPorID, '/produtos/<id>')


api.add_resource(Pedidos, '/pedidos')
api.add_resource(PedidoPorID, '/pedidos/<id>')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    baseDelivery.fecharConexao()
