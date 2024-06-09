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
            SELECT 
                url_group, 
                url_playoffs, 
                CASE 
                    WHEN url_finals IS NOT NULL THEN url_finals
                END AS url_finals
            FROM championships
            WHERE url_group IS NOT NULL;
        '''
        self.cursor.execute(sql)
        for region in self.cursor.fetchall():
            for url in region:
                list_urls.append(url)

        return list_urls
    
    def prepare_start_urls(self):
        start_urls = []
        urls = self.get_start_urls()
        for url in urls:
            if url:
                start_urls.append(url)
        return start_urls