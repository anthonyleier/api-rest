from config import baseDelivery


def getPedidos():
    query = """
    SELECT pedido.id, pedido.usuario,
    ARRAY_AGG(pedido_produto.produto) AS produtos
    FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id
    GROUP BY pedido.id;
    """
    dadosPedidos = baseDelivery.selecionar(query)

    return dadosPedidos


def criarPedido(usuario, produtos):
    query = "INSERT INTO pedido (usuario) VALUES (%s) RETURNING id;"
    parametros = [usuario]
    pedido = baseDelivery.executar(query, parametros)

    for produto in produtos:
        query = "INSERT INTO pedido_produto (pedido, produto) VALUES (%s, %s) RETURNING id;"
        parametros = [pedido, produto]
        baseDelivery.executar(query, parametros)

    resposta = {'pedido': pedido, 'produtos': produtos}
    return resposta

def getPedidoID(id):
    query = """
        SELECT pedido.id, pedido.usuario, pedido_produto.produto, pedido_produto.quantidade FROM pedido
        LEFT JOIN pedido_produto
        ON pedido_produto.pedido = pedido.id
        WHERE pedido.id = %s;
        """
        parametros = [id]
        dadosPedido = baseDelivery.selecionarUm(query, parametros)
    
    return dadosPedido

def atualizarPedido(id):
    query = "UPDATE pedido SET usuario = %s WHERE id = %s;"
        parametros = [usuario, id]
        status = baseDelivery.executar(query, parametros)

        jsonResposta = jsonify(status)
    
