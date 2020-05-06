from django.db import connection

class Relatorio:
    
    @staticmethod
    def relatAniversarioCliente():
        cursor = connection.cursor()
        cursor.execute("""SELECT nomeCliente, strftime('%m',dataNascimento) as mes FROM cliente_cliente order by mes""")#COnsulta esta errada.
        resultados = cursor.fetchall()
        return resultados
        