from config import baseDelivery


def getProduto():
    query = "SELECT * FROM produto WHERE id = %s;"
    parametros = [id]
    dadosProduto = baseDelivery.selecionarUm(query, parametros)


def getListaProdutos():
    query = "SELECT * FROM produto;"
    dadosProdutos = baseDelivery.selecionar(query)


def criarProduto(nome, descricao, valor, imagem, id):

    query = """
        INSERT INTO produto (nome, descricao, valor, imagem)
        VALUES (%s, %s, %s, %s);
        """
    parametros = [nome, descricao, valor, imagem]
    status = baseDelivery.executar(query, parametros)


def atualizarProduto(nome, descricao, valor, imagem, id):
    query = """
    UPDATE produto SET nome = %s, descricao = %s, valor = %s, imagem = %s
    WHERE id = %s ;
    """
    parametros = [nome, descricao, valor, imagem, id]
    status = baseDelivery.executar(query, parametros)


def deletarProduto():
    query = "DELETE FROM produto WHERE id = %s ;"
    parametros = [id]
    status = baseDelivery.executar(query, parametros)
