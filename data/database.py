from data.config import DIR
import sqlite3


class Hooks:
    def __init__(self, path_to_db=f"{DIR}/data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=None, fetchall=None, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_hooks(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Hooks(
        id INT NOT NULL UNIQUE,
        link TEXT
        );
        """

        self.execute(sql, commit=True)

    def add_hook(self, id: int, link: str):
        sql = "INSERT INTO Hooks(id, link) values(?, ?)"
        parameters = (id, link)
        self.execute(sql, parameters, commit=True)

    def delete_hook(self, id: int):
        sql = "DELETE FROM Hooks WHERE id=?"
        self.execute(sql, parameters=(id,), commit=True)

    def all_hooks(self):
        sql = "SELECT link FROM Hooks"
        data = self.execute(sql, fetchall=True)
        return data

    def count_hooks(self):
        return self.execute("SELECT COUNT(*) FROM Hooks;", fetchone=True)
