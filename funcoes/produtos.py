from config import baseDelivery


def getProduto():
    query = "SELECT * FROM produto WHERE id = %s;"
    parametros = [id]
    dadosProduto = baseDelivery.selecionarUm(query, parametros)


def getListaProdutos():
    query = "SELECT * FROM produto;"
    dadosProdutos = baseDelivery.selecionar(query)


def criarProduto():

    query = """
        INSERT INTO produto (nome, descricao, valor, imagem)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
    parametros = [nome, descricao, valor, imagem]
    status = baseDelivery.executar(query, parametros)


def atualizarProduto(): query = """
        UPDATE produto SET nome = %s, descricao = %s, valor = %s, imagem = %s
        WHERE id = %s RETURNING id;
        """


parametros = [nome, descricao, valor, imagem, id]
status = baseDelivery.executar(query, parametros)


def deletarProduto():
    query = "DELETE FROM produto WHERE id = %s RETURNING id;"
    parametros = [id]
    status = baseDelivery.executar(query, parametros)
