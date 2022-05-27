from utils import baseDelivery, chaveNecessaria


def getProduto(id):
    query = "SELECT * FROM produto WHERE id = %s;"
    parametros = [id]
    dadosProduto = baseDelivery.selecionarUm(query, parametros)
    return dadosProduto


def getListaProdutos():
    query = "SELECT * FROM produto;"
    listaProdutos = baseDelivery.selecionar(query)
    return listaProdutos


@chaveNecessaria
def criarProduto(nome, descricao, valor, imagem):
    if nome and descricao and imagem and valor > 0:
        query = "INSERT INTO produto (nome, descricao, valor, imagem) VALUES (%s, %s, %s, %s) RETURNING id;"
        parametros = [nome, descricao, valor, imagem]
        dados = baseDelivery.executar(query, parametros)
        id = dados['id']

        dadosProduto = getProduto(id)
        return dadosProduto


@chaveNecessaria
def atualizarProduto(nome, descricao, valor, imagem, id):
    if nome and descricao and imagem and id and valor > 0:
        query = "UPDATE produto SET nome = %s, descricao = %s, valor = %s, imagem = %s WHERE id = %s;"
        parametros = [nome, descricao, valor, imagem, id]
        baseDelivery.executar(query, parametros)

        dadosProduto = getProduto(id)
        return dadosProduto


@chaveNecessaria
def deletarProduto(id):
    if getProduto(id):
        query = "DELETE FROM produto WHERE id = %s;"
        parametros = [id]
        baseDelivery.executar(query, parametros)

        dadosProduto = getProduto(id)
        foiDeletado = not dadosProduto
        return foiDeletado
