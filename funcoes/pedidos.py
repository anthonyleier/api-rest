from config import baseDelivery


def getPedido(id):
    query = """
    SELECT
        pedido.id, pedido.usuario,
        ARRAY_AGG(pedido_produto.produto ORDER BY pedido_produto.produto) AS produtos,
        ARRAY_AGG(pedido_produto.quantidade ORDER BY pedido_produto.produto) AS quantidades
    FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id
    WHERE pedido.id = %s
    GROUP BY pedido.id;
    """
    parametros = [id]
    dados = baseDelivery.selecionar(query, parametros)

    if dados:
        return dados[0]


def getListaPedidos():
    query = """
    SELECT
        pedido.id, pedido.usuario,
        ARRAY_AGG(pedido_produto.produto ORDER BY pedido_produto.produto) AS produtos,
        ARRAY_AGG(pedido_produto.quantidade ORDER BY pedido_produto.produto) AS quantidades
    FROM pedido
    LEFT JOIN pedido_produto ON pedido_produto.pedido = pedido.id
    GROUP BY pedido.id;
    """
    dadosPedidos = baseDelivery.selecionar(query)
    return dadosPedidos


def criarPedido(usuario, produtos, quantidades):
    query = "INSERT INTO pedido (usuario) VALUES (%s) RETURNING id;"
    parametros = [usuario]
    dados = baseDelivery.executar(query, parametros)
    id = dados['id']

    itens = list(zip(produtos, quantidades))
    itensOrdenados = sorted(itens, key=lambda x: x[1])

    for produto, quantidade in itensOrdenados:
        query = "INSERT INTO pedido_produto (pedido, produto, quantidade) VALUES (%s, %s, %s);"
        parametros = [id, produto, quantidade]
        baseDelivery.executar(query, parametros)

    dadosPedido = getPedido(id)
    return dadosPedido


def atualizarProdutoPedido(usuario, produtos, quantidades, id):
    query = "UPDATE pedido SET usuario = %s WHERE id = %s;"
    parametros = [usuario, id]
    baseDelivery.executar(query, parametros)

    itens = list(zip(produtos, quantidades))
    itensOrdenados = sorted(itens, key=lambda x: x[1])

    for produto, quantidade in itensOrdenados:
        query = "SELECT * FROM pedido_produto WHERE pedido = %s AND produto = %s;"
        parametros = [id, produto]
        dados = baseDelivery.selecionarUm(query, parametros)

        if dados:
            quantidadeAtual = dados['quantidade']
            quantidadeAtual += quantidade
            quantidadeAtual = quantidadeAtual if quantidadeAtual > 0 else 0

            query = "UPDATE pedido_produto SET quantidade = %s WHERE pedido = %s AND produto = %s;"
            parametros = [quantidadeAtual, id, produto]
            baseDelivery.executar(query, parametros)

        elif quantidade > 0:
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
