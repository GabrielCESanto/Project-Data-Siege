from loguru import logger
import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
from database.databaseConnection import connection

class getData:
    connector = connection.getInstance()
    cursor = connector.database_cursor()

    def get_start_urls (self):
        list_urls = []
        sql = '''
            SELECT url_group, url_playoffs
            FROM championships
            WHERE url_group IS NOT NULL
        '''
        self.cursor.execute(sql)
        for region in self.cursor.fetchall():
            for url in region:
                list_urls.append(url)

        return list_urls
