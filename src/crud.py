#python 3.10.12

# ---- COMEÇO DO CRUD ----

# Importando do arquivo database o objeto TransactionObject
from database import TransactionObject

# Função de criar o BD caso não exista
def initDB():
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

# Função responsável por inserir
def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

# Função de visualizar os dados
def view():
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Função de buscar dados
def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome = ? OR sobrenome = ? OR email = ? OR cpf = ?", (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Função de deletar dados
def delete(id):
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

# Função de atualizar dados
def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject("dados.db")
    trans.connect()
    trans.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?", (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.disconnect()
