import requests, json
from loguru import logger
class request:
    base_url = 'https://www.ubisoft.com/_next/data/ATLPrP2MS97bw41nY3b4g/pt-br/esports/rainbow-six/siege/match/5850.json?id=5850'
    # base_url = 'https://www.ubisoft.com/_next/data/lOhuklQA0gv47daW1G-Uc/pt-br/esports/rainbow-six/siege/match/5850.json?id=5850'
    def request_info(self, id=0):
        prepared_url = f'{self.base_url}{id}.json?id={id}'
        response = requests.get(prepared_url)

        json_response = json.loads(response.text)
        matches_info = json_response['pageProps']['pageData']
        return matches_info
