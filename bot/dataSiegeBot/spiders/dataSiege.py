# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
import scrapy
from loguru import logger
import re
from utils.request import request
from main.app import app
from database.getData import getData

class DatasiegeSpider(scrapy.Spider):
    name = 'dataSiege'
    allowed_domains = ['ubisoft.com']
    start_urls = getData().get_start_urls()
    id_json = ''

    def parse(self, response):
        try:
            requeridor = request()
            info_insertion = app()
            cache = self.read_matches_cache()

            all_matches_link  = response.css('.matches-list_match__G2PUt > a::attr(href)').getall()
            if not all_matches_link : 
                all_matches_link  = response.css('.brackets_matchup__F8vxe::attr(href)').getall()

            id = re.search('"buildId":"(\w+)"', response.text)
            self.id_json = re.split('"', id.group()) [-2]

            for match in all_matches_link:
                if match in cache:
                    logger.debug(f'{match} já foi varrida')
                    continue

                id_match = re.split('/', match)[-1]
                match_info = requeridor.request_info(id_match, self.id_json)
                info_insertion.get_matches_info(match_info, match)
        except Exception as e:
            logger.debug('ERROR')
            logger.debug(e)


    def read_matches_cache(self):
        cache_list = []
        try:
            with open('/home/thiago/Projetos/dataSiege/Project-Data-Siege/main/cache_matches.txt', 'r') as file:
                lines = file.readlines()
                stripped_lines = [line.strip() for line in lines]
                cache_list = stripped_lines
            return cache_list
        except Exception as e:
            return cache_list