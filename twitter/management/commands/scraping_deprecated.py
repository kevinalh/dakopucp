# -*- coding: utf-8 -*-

''' NO FUNCIONA - Ocurre un bug que sale como sin resolver en Github '''

import sys
from GoogleScraper import scrape_with_config, GoogleSearchError
from GoogleScraper.database import ScraperSearch, SERP, Link
from twitter.models import Tweet,  Keyword

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import OperationalError,  connection
import pdb
import time

class Command(BaseCommand):
    help = "Saca la data de Google a partir de la informacion que se provee"
    def handle(self, *args, **options):        
        def mineria():
            keyword_array = ['tia maria mina']
            for keyword in keyword_array:
                time.sleep(10)
                analizar_keyword(keyword)

        def analizar_keyword(keyword):
            # Configuracion de GoogleScrap
            pdb.set_trace()
            config = {
                'SCRAPING': {
                    'use_own_ip': 'True',
                    'keyword': keyword,
                    'search_engines': 'bing',
                    'num_pages_for_keyword': 3
                },
                'SELENIUM': {
                    'sel_browser': 'chrome',
                },
                'GLOBAL': {
                    'do_caching': 'False'
                }
            }

            try:
                pdb.set_trace()
                sqlalchemy_session = scrape_with_config(config)
            except GoogleSearchError as e:
                print(e)

            # Inspeccion
            pdb.set_trace()
            for search in sqlalchemy_session.query(ScraperSearch).all():
                for serp in search.serps:
                    print(serp)
                    for link in serp.links:
                        print(link)
        try:
            mineria()
        except KeyboardInterrupt:
            print("Cancelado por teclado")
