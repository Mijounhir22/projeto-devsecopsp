import sqlite3
def verificar_login(usuario, senha):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    # Usando query parametrizada para evitar SQL Injection
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    return cursor.fetchone()
# CHAVE DE ACESSO AWS PARA TESTE DE SEGURANÇA
AWS_SECRET_KEY = "AKIAIMNO7CQD6EXAMPLE"