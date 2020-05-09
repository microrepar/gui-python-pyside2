# -*- coding: utf-8 -*-
"""Exemplo de CRUD com SQLite3."""
from PySide2.QtSql import QSqlDatabase, QSqlQuery


class ConnectSQLite:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('DataBaseName.sqlite3')
        # self.db.setDatabaseName(':memory:')
        self.db.open()

        self.query = QSqlQuery()

        # Criando a tabela.
        self.create_table()

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS table_name (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT
        )'''
        self.query.exec_(sql)

    def insert_row(self, data):
        sql = 'INSERT INTO table_name (name, age, gender) VALUES (?, ?, ?)'
        self.query.prepare(sql)
        for index, value in enumerate(data):
            self.query.addBindValue(data[index])
        self.query.exec_()

    def insert_rows(self, data):
        for row in data:
            self.insert_row(data=row)

    def find_by_id(self, rowid):
        sql = 'SELECT * FROM table_name WHERE id = ?'
        self.query.prepare(sql)
        self.query.addBindValue(rowid)
        self.query.exec_()
        if self.query.first():
            return self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3)
        return False

    def find(self, limit=10):
        sql = 'SELECT * FROM table_name LIMIT ?'
        self.query.prepare(sql)
        self.query.addBindValue(limit)
        self.query.exec_()

        result = []
        while self.query.next():
            data = (self.query.value(0), self.query.value(1),
                    self.query.value(2), self.query.value(3))
            result.append(data)
        return result

    def update_row(self, rowid, name, age, gender):
        sql = 'UPDATE table_name SET name=?, age=?, gender=? WHERE id=?'
        self.query.prepare(sql)
        self.query.addBindValue(name)
        self.query.addBindValue(age)
        self.query.addBindValue(gender)
        self.query.addBindValue(rowid)

        if self.query.exec_():
            return True

        self.db.rollback()
        print(self.query.lastError())
        return False

    def remove_row(self, rowid):
        sql = 'DELETE FROM table_name WHERE id=?'
        self.query.prepare(sql)
        self.query.addBindValue(rowid)

        if self.query.exec_():
            return True

        self.db.rollback()
        print(self.query.lastError())
        return False


if __name__ == '__main__':
    print('Drivers disponíveis:', QSqlDatabase.drivers())

    # user = ('Felipe', 35, 'Masculino')
    # users = [
    #     ('Maria', 20, 'Feminino'),
    #     ('João', 50, 'Masculino'),
    # ]

    # database = ConnectSQLite()

    # Inserindo os dados.
    # database.insert_row(data=user)
    # database.insert_rows(data=users)

    # Consultando com filtro.
    # print(database.find_by_id(rowid=1))

    # Consultando todos (limit=10).
    # print(database.find())

    # Alterando registro da tabela.
    # print('ANTES da alteração:')
    # print(database.find_by_id(rowid=2))
    # database.update_row(rowid=2, name='Rafaela', age=50, gender='Feminino')
    # print('DEPOIS da alteração:')
    # print(database.find_by_id(rowid=2))

    # Removendo registro da tabela.
    # print('ANTES da remoção:')
    # print(database.find())
    # database.remove_row(rowid=2)
    # print('DEPOIS da remoção:')
    # print(database.find())

    # Fechando conexão com o banco.
    # database.db.close()
