import sqlite3
def verificar_login(usuario, senha):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    # Usando query parametrizada para evitar SQL Injection
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    return cursor.fetchone()
# Configuração de teste
ADMIN_PASSWORD = "minha_senha_super_secreta_123"