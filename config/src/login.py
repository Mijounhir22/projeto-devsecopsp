import sqlite3

# Remediação: Implementação de Queries Parametrizadas
def verificar_login(usuario, senha):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()

    # O uso do '?' impede que o input do usuário execute comandos SQL indesejados
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    
    if resultado:
        print("Autenticação bem-sucedida!")
        return True
    else:
        print("Credenciais inválidas.")
        return False
    
    conn.close()

# Exemplo de execução segura
if __name__ == "__main__":
    verificar_login("admin", "senha_segura_123")