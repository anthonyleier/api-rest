from config import baseDelivery


def getPedido(id):
    query = """
    SELECT
        pedido.id, pedido.usuario,
        ARRAY_AGG(CONCAT(
            pedido_produto.produto, ',', pedido_produto.quantidade
        )) AS carrinho
    FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id
    WHERE pedido.id = %s
    GROUP BY pedido.id;
    """
    parametros = [id]
    dados = baseDelivery.selecionar(query, parametros)
    dadosPedido = dados[0]
    for item in dadosPedido['carrinho']:
        print(type(item))
        print(item)
        elementos = item.split(',')
        dadosPedido['carrinho'].append([elementos[0], elementos[1]])
    return dadosPedido


def getListaPedidos():
    query = """
    SELECT
        pedido.id, pedido.usuario,
        ARRAY_AGG(pedido_produto.produto) AS produtos,
        ARRAY_AGG(pedido_produto.quantidade) AS quantidades
    FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id
    GROUP BY pedido.id;
    """
    dadosPedidos = baseDelivery.selecionar(query)
    return dadosPedidos


def criarPedido(usuario, carrinho):
    query = "INSERT INTO pedido (usuario) VALUES (%s) RETURNING id;"
    parametros = [usuario]
    dados = baseDelivery.executar(query, parametros)
    id = dados['id']

    for produto, quantidade in carrinho:
        query = "INSERT INTO pedido_produto (pedido, produto, quantidade) VALUES (%s, %s, %s);"
        parametros = [id, produto, quantidade]
        baseDelivery.executar(query, parametros)

    dadosPedido = getPedido(id)
    return dadosPedido


def atualizarPedido(usuario, produtos, id):
    query = "UPDATE pedido SET usuario = %s WHERE id = %s;"
    parametros = [usuario, id]
    baseDelivery.executar(query, parametros)

    query = "DELETE FROM pedido_produto WHERE pedido = %s;"
    parametros = [id]
    baseDelivery.executar(query, parametros)

    for produto, quantidade in produtos:
        query = "INSERT INTO pedido_produto (pedido, produto, quantidade) VALUES (%s, %s, %s);"
        parametros = [id, produto, quantidade]
        baseDelivery.executar(query, parametros)

    dadosPedido = getPedido(id)
    return dadosPedido


def deletarPedido(id):
    query = "DELETE FROM pedido_produto WHERE pedido = %s;"
    parametros = [id]
    baseDelivery.executar(query, parametros)

    query = "DELETE FROM pedido WHERE id = %s;"
    parametros = [id]
    baseDelivery.executar(query, parametros)

    dadosPedido = getPedido(id)
    foiDeletado = not dadosPedido
    return foiDeletado
