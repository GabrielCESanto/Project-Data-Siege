import sqlite3
from loguru import logger

class connection():
    _instance = None
    database_path = 'database/dataSiege.db'

    def __init__(self):
        if connection._instance is not None:
            raise Exception("Call getInstance")
        else:
            connection._instance = self

    @staticmethod
    def getInstance():
        if connection._instance is None:
            connection()

        return connection._instance

    def database_connection(self):
        try:
            return sqlite3.connect(self.database_path)
        except Exception as e:
            logger.error("ERROR")
            logger.error(e)