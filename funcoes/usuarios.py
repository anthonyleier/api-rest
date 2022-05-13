from config import baseDelivery


def getUsuario():
    query = "SELECT * FROM usuario WHERE id = %s;"
    parametros = [id]
    dadosUsuario = baseDelivery.selecionarUm(query, parametros)
    return dadosUsuario


def getListaUsuarios():
    query = "SELECT * FROM usuario;"
    listaUsuarios = baseDelivery.selecionar(query)
    return listaUsuarios


def criarUsuario():
    query = """
        INSERT INTO usuario (nome, email, senha)
        VALUES (%s, %s, %s) ;
        """
    parametros = [nome, email, senha]
    status = baseDelivery.executar(query, parametros)


def atualizarUsuario():
    query = """
        UPDATE usuario SET nome = %s, email = %s, senha = %s
        WHERE id = %s ;
        """
    parametros = [nome, email, senha, id]
    status = baseDelivery.executar(query, parametros)


def deletarUsuario():
    query = "DELETE FROM usuario WHERE id = %s ;"
    parametros = [id]
    status = baseDelivery.executar(query, parametros)
