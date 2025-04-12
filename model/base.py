import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("simulacoes.db", check_same_thread=False)
cursor = conn.cursor()

def inicializar_banco():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        moeda TEXT NOT NULL,
        valor_brl REAL NOT NULL,
        valor_convertido REAL NOT NULL,
        cotacao REAL NOT NULL
    )
    """)
    conn.commit()

# Executa a inicialização ao carregar o módulo
inicializar_banco()
