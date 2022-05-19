from config import baseDelivery


def getProduto(id):
    query = "SELECT * FROM produto WHERE id = %s;"
    parametros = [id]
    dadosProduto = baseDelivery.selecionarUm(query, parametros)
    return dadosProduto


def getListaProdutos():
    query = "SELECT * FROM produto;"
    listaProdutos = baseDelivery.selecionar(query)
    return listaProdutos


def criarProduto(nome, descricao, valor, imagem):
    query = "INSERT INTO produto (nome, descricao, valor, imagem) VALUES (%s, %s, %s, %s);"
    parametros = [nome, descricao, valor, imagem]
    baseDelivery.executar(query, parametros)

    query = "SELECT * FROM produto WHERE nome = %s AND descricao = %s AND valor = %s AND imagem = %s;"
    dadosProduto = baseDelivery.selecionarUm(query, parametros)
    return dadosProduto


def atualizarProduto(nome, descricao, valor, imagem, id):
    query = "UPDATE produto SET nome = %s, descricao = %s, valor = %s, imagem = %s WHERE id = %s;"
    parametros = [nome, descricao, valor, imagem, id]
    baseDelivery.executar(query, parametros)

    dadosProduto = getProduto(id)
    return dadosProduto


def deletarProduto():
    query = "DELETE FROM produto WHERE id = %s ;"
    parametros = [id]
    baseDelivery.executar(query, parametros)

    dadosProduto = getProduto(id)
    foiDeletado = not dadosProduto
    return foiDeletado
