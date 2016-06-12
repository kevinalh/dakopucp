# -*- coding: utf-8 -*-

import pprint

from googleapiclient.discovery import build

from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Guarda las busquedas de Google en la base de datos"
    service = build("customsearch", "v1", developerKey=settings.CODIGO_GOOGLE)
    def buscar():
      res = service.cse().list(
          q='lectures',
          cx='017576662512468239146:omuauf_lfve',
        ).execute()
      pprint.pprint(res)
