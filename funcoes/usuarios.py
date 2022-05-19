from config import baseDelivery


def getUsuario(id):
    query = "SELECT * FROM usuario WHERE id = %s;"
    parametros = [id]
    dadosUsuario = baseDelivery.selecionarUm(query, parametros)
    return dadosUsuario


def getListaUsuarios():
    query = "SELECT * FROM usuario;"
    listaUsuarios = baseDelivery.selecionar(query)
    return listaUsuarios


def criarUsuario(nome, email, senha):
    query = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s);"
    parametros = [nome, email, senha]
    baseDelivery.executar(query, parametros)

    query = "SELECT * FROM usuario WHERE nome = %s AND email = %s AND senha = %s;"
    dadosUsuario = baseDelivery.selecionarUm(query, parametros)
    return dadosUsuario


def atualizarUsuario(nome, email, senha, id):
    query = "UPDATE usuario SET nome = %s, email = %s, senha = %s WHERE id = %s;"
    parametros = [nome, email, senha, id]
    baseDelivery.executar(query, parametros)

    dadosUsuario = getUsuario(id)
    return dadosUsuario


def deletarUsuario(id):
    query = "DELETE FROM usuario WHERE id = %s;"
    parametros = [id]
    baseDelivery.executar(query, parametros)

    dadosUsuario = getUsuario(id)
    foiDeletado = not dadosUsuario
    return foiDeletado
