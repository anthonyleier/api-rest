from flask import Flask
from flask_restful import Api
from usuarios import Usuarios, UsuarioPorID
# from pedidos import PedidosGeral, PedidoPorID
# from produtos import ProdutosGeral, ProdutoPorID
# from promocoes import PromocoesGeral, PromocaoPorID

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuarios, '/usuarios')
api.add_resource(UsuarioPorID, '/usuarios/<id>')

# api.add_resource(PedidosGeral, '/pedidos')
# api.add_resource(PedidoPorID, '/pedidos/<id>')

# api.add_resource(ProdutosGeral, '/produtos')
# api.add_resource(ProdutoPorID, '/produtos/<id>')

# api.add_resource(PromocoesGeral, '/promocoes')
# api.add_resource(PromocaoPorID, '/promocoes/<id>')

if __name__ == '__main__':
    app.run()
