import pyodbc
from loguru import logger

class connection():
    server= 'datasiege.database.windows.net'
    database = 'dataSiege'
    username = 'admin2024'
    password = 'DataSiege2024'
    driver = '{ODBC Driver 17 for SQL Server}'
    _instance = None

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

    def database_cursor(self):
        try:
            with pyodbc.connect(f'DRIVER={self.driver};SERVER={self.server};PORT=1433;DATABASE={self.database};UID={self.username};PWD={self.password}') as conn:
                with conn.cursor() as cursor:
                    return cursor
        except Exception as e:
            logger.error('ERROR')
            logger.error(e)