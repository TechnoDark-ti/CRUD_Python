"""
--------- Começo do arquivo para as ações do banco de dados ---------
"""
# Bibliotecas do sistema
import sqlite3 as sql

# Criando as funções de connect, execute e fetch com o banco de dados SQLite
class TransactionObject:
    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cur = None
        self.connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False

    def execute(self, query, parms=None):
        if self.connected:
            if parms is None:
                self.cur.execute(query)
            else:
                self.cur.execute(query, parms)
            return True
        else:
            return False

    def fetchall(self):
        if self.connected:
            return self.cur.fetchall()
        else:
            return None

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False
