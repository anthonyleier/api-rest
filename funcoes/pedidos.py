from config import baseDelivery


def getPedido(id):
    query = """
    SELECT pedido.id, pedido.usuario, pedido_produto.produto, pedido_produto.quantidade FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id WHERE pedido.id = %s;
    """
    parametros = [id]
    dadosPedido = baseDelivery.selecionarUm(query, parametros)
    return dadosPedido


def getListaPedidos():
    query = """
    SELECT pedido.id, pedido.usuario, ARRAY_AGG(pedido_produto.produto) AS produtos FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id GROUP BY pedido.id;
    """
    dadosPedidos = baseDelivery.selecionar(query)
    return dadosPedidos


def criarPedido(usuario, produtos):
    query = "INSERT INTO pedido (usuario) VALUES (%s);"
    parametros = [usuario]
    pedido = baseDelivery.executar(query, parametros)

    for produto in produtos:
        query = "INSERT INTO pedido_produto (pedido, produto) VALUES (%s, %s);"
        parametros = [pedido, produto]
        baseDelivery.executar(query, parametros)

    resposta = {'pedido': pedido, 'produtos': produtos}
    return resposta


def atualizarPedido(id, usuario):
    query = "UPDATE pedido SET usuario = %s WHERE id = %s;"
    parametros = [usuario, id]
    status = baseDelivery.executar(query, parametros)


def deletarPedido(id):
    query = "DELETE FROM pedido_produto WHERE pedido = %s;"
    parametros = [id]
    status = baseDelivery.executar(query, parametros)

    query = "DELETE FROM pedido WHERE id = %s;"
    parametros = [id]
    status = baseDelivery.executar(query, parametros)
