from utils import baseDelivery, chaveNecessaria


def getUsuario(id):
    query = "SELECT * FROM usuario WHERE id = %s;"
    parametros = [id]
    dadosUsuario = baseDelivery.selecionarUm(query, parametros)
    return dadosUsuario


def getListaUsuarios():
    query = "SELECT * FROM usuario;"
    listaUsuarios = baseDelivery.selecionar(query)
    return listaUsuarios


@chaveNecessaria
def criarUsuario(nome, email, senha):
    if nome and email and senha:
        query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s) RETURNING id;"
        parametros = [nome, email, senha]
        dados = baseDelivery.executar(query, parametros)
        id = dados['id']

        dadosUsuario = getUsuario(id)
        return dadosUsuario


@chaveNecessaria
def atualizarUsuario(nome, email, senha, id):
    if getUsuario(id):
        query = "UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id = %s;"
        parametros = [nome, email, senha, id]
        baseDelivery.executar(query, parametros)

        dadosUsuario = getUsuario(id)
        return dadosUsuario


@chaveNecessaria
def deletarUsuario(id):
    if getUsuario(id):
        query = "SELECT id FROM pedido WHERE usuario = %s;"
        parametros = [id]
        pedidos = baseDelivery.selecionar(query, parametros)

        for pedido in pedidos:
            query = "DELETE FROM pedido_produto WHERE pedido = %s;"
            parametros = [pedido['id']]
            baseDelivery.executar(query, parametros)

            query = "DELETE FROM pedido where id = %s;"
            parametros = [pedido['id']]
            baseDelivery.executar(query, parametros)

        query = "DELETE FROM usuario WHERE id = %s;"
        parametros = [id]
        baseDelivery.executar(query, parametros)

        dadosUsuario = getUsuario(id)
        foiDeletado = not dadosUsuario
        return foiDeletado
