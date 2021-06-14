import sqlite3
from Service.DataFormat import Data
from Model.Produto import Product


class DataBase:
    def __init__(self, db_name: str):
        self.db = sqlite3.connect(f'{db_name}.db', isolation_level=None)
        #self.db.row_factory = lambda cursor, row: row[0]


class Cursor(DataBase):

    def __init__(self, db_name: str):
        super().__init__(db_name)
        self.cursor = self.db.cursor()


    def monta_lista(self, loja):
        self.cursor.execute("SELECT serial FROM Produtos WHERE loja LIKE (?)",('%'+loja+'%',))
        result = self.cursor.fetchall()
        print(result)
        return list(set(result))


    def criar_tabela(self, table_name):
        self.cursor.execute(f"CREATE TABLE {table_name} (loja text,serial text,name text, price text, date date)")
        '''
        Cria uma nova tabela no banco de dados para salvar os produtos, executar somente na primeira execução do banco.
        '''


    def salva_produto(self, loja, serial, name, price):
        self.cursor.execute("INSERT INTO Produtos VALUES (?,?,?,?,?)", (loja, serial, name, price, Data.get_data()))
        print('Produto salvo com sucesso!')


    def get_product(self, serial):
        self.cursor.execute("SELECT * FROM Produtos WHERE serial LIKE (?) ORDER BY DATE DESC",('%'+serial+'%',))
        item = self.cursor.fetchall()
        print(item)
