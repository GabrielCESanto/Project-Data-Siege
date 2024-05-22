import requests, json
from loguru import logger
class request:
    base = 'https://www.ubisoft.com/_next/data/'
    complement = '/pt-br/esports/rainbow-six/siege/match/'

    def request_info(self, id_game=0, id_json = ''):
        prepared_url = f'{self.base}{id_json}{self.complement}{id_game}.json?id={id_game}'
        response = requests.get(prepared_url)

        json_response = json.loads(response.text)
        matches_info = json_response['pageProps']['pageData']
        return matches_info
