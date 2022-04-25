from flask import request, jsonify
from flask_restful import Resource
from config import baseBlog


class Pedidos(Resource):
    def get(self):
        query = 'SELECT * FROM pedidos;'
        dadosPedidoss = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosPedidoss)
        return jsonResposta

    def post(self):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        INSERT INTO pedidos (titulo, texto, usuario)
        VALUES ('{titulo}', '{texto}', {usuario});
        """
        baseBlog.executar(query)

        query = f"""
        SELECT * FROM Pedidos
        WHERE usuario = '{usuario}';
        """
        dadosPedidoss = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosPedidoss)
        return jsonResposta


class PedidoPorID(Resource):
    def get(self, id):
        query = f"SELECT * FROM pedidos WHERE id = {id};"
        dadosPedidos = baseBlog.selecionar(query)
        jsonResposta = jsonify(dadosPedidos)
        return jsonResposta

    def put(self, id):
        titulo = request.json['titulo']
        texto = request.json['texto']
        usuario = request.json['usuario']

        query = f"""
        UPDATE pedidos SET
        titulo = '{titulo}',
        texto = '{texto}',
        usuario = '{usuario}'
        WHERE id = {id};
        """
        baseBlog.executar(query)

        query = f"SELECT * FROM pedidos WHERE id = {id};"
        dadosPedidos = baseBlog.selecionar(query)

        jsonResposta = jsonify(dadosPedidos)
        return jsonResposta

    def delete(self, id):
        query = f"DELETE FROM Pedidos WHERE id = {id};"
        status = baseBlog.executar(query)

        jsonResposta = jsonify({'status': status})
        return jsonResposta
