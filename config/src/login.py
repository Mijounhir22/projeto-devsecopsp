import sqlite3

def verificar_login(usuario, senha):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()

    # MODO SEGURO: O '?' atua como um placeholder. 
    # O SQL entende que o que vier dali é apenas TEXTO, não um COMANDO.
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    
    if resultado:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")
    
    conn.close()