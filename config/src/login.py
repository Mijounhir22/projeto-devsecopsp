import sqlite3
def verificar_login(usuario, senha):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    # Usando query parametrizada para evitar SQL Injection
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    return cursor.fetchone()
# TESTE DE SEGURANÇA: ESTA LINHA DEVE SER BLOQUEADA PELA ESTEIRA
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYp