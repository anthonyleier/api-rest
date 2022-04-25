import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host, db):
        try:
            self.conexao = psycopg2.connect(
                host=host, database=db, user='postgres', password='postgres')
            self.conexao.set_client_encoding('LATIN1')
        except:
            print("Não foi possivel conectar ao banco de dados. Verifique as informações da conexão e tente novamente")

    def selecionar(self, query):
        try:
            cursor = self.conexao.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)

    def selecionarUm(self, query):
        try:
            cursor = self.conexao.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query)
            resultado = cursor.fetchone()
            cursor.close()
            return resultado

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)

    def executar(self, query):
        try:
            cursor = self.conexao.cursor()
        except:
            print("Não foi possível se conectar ao banco")

        try:
            cursor.execute(query)
            self.conexao.commit()
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            self.conexao.rollback()
            print("Error: %s" % error)
            print("Rollback aplicado")

    def fecharConexao(self):
        try:
            self.conexao.close
        except:
            print("Não foi possível fechar a conexão")
