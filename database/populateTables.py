import sqlite3
import os
import databaseConnection

class populateTables:
    def __init__(self):
        connector = databaseConnection.connection.getInstance()
        self.conn = connector.database_connection()
        self.cursor = self.conn.cursor()

    def populate_unmutable_tables(self):
        pass

    def populate_mutables_tables(self):
        pass