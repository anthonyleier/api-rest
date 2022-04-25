from flask import Flask
from flask_restful import Api
from classes.usuarios import Usuarios, UsuarioPorID
from classes.produtos import Produtos, ProdutoPorID
# from classes.pedidos import PedidosGeral, PedidoPorID
# from classes.promocoes import PromocoesGeral, PromocaoPorID

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioPorID, '/usuarios/<id>')

api.add_resource(Produtos, '/produtos')
api.add_resource(ProdutoPorID, '/produtos/<id>')

# api.add_resource(PedidosGeral, '/pedidos')
# api.add_resource(PedidoPorID, '/pedidos/<id>')


# api.add_resource(PromocoesGeral, '/promocoes')
# api.add_resource(PromocaoPorID, '/promocoes/<id>')

if __name__ == '__main__':
    app.run()
