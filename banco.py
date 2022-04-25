import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host, db):
        try:
            self.conexao = psycopg2.connect(
                host=host, database=db, user='postgres', password='postgres')
        except:
            print("Não foi possivel conectar ao banco de dados. Verifique as informações da conexão e tente novamente")

    def selecionar(self, query, parametros=None):
        try:
            cursor = self.conexao.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query, parametros)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado

        except Exception as erro:
            print(f"Erro no banco: {erro}")

    def selecionarUm(self, query, parametros=None):
        try:
            cursor = self.conexao.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query, parametros)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado

        except Exception as erro:
            print(f"Erro no banco: {erro}")

    def executar(self, query, parametros=None):
        try:
            cursor = self.conexao.cursor()
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query, parametros)
            self.conexao.commit()
            id = cursor.fetchone()[0]
            cursor.close()
            return id

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro no banco: {erro}")
            print("Rollback aplicado")
            return str(erro)

    def fecharConexao(self):
        try:
            self.conexao.close
        except:
            print("Não foi possível fechar a conexão")
