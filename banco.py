import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host, database, user, password):
        self.conexao = psycopg2.connect(host=host, database=database, user=user, password=password)
        self.cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def selecionar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchall()
            return resultado

        except Exception as erro:
            print(f"Erro no selecionar: {erro}")

    def selecionarUm(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchone()
            return resultado

        except Exception as erro:
            print(f"Erro no selecionarUm: {erro}")

    def executar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            self.conexao.commit()
            retorno = "RETURNING"

            if retorno in query:
                return self.cursor.fetchone()

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro no executar: {erro}")

    def fecharConexao(self):
        try:
            self.cursor.close()
            self.conexao.close()
        except:
            print("Não foi possível fechar a conexão")
