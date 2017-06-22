#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys, traceback


class Log:
    diretorio = os.getcwd()+ "\\log.log"

    def __init__(self, caminho = diretorio):
        self.caminho = caminho

    def log(self):
        try:
             exc_type, exc_value, exc_traceback =  sys.exc_info()
             erro = traceback.format_exception(exc_type, exc_value,exc_traceback)

             with open(self.caminho, "a") as arquivo:
                arquivo.write("\n"+str(datetime.now())+" => "+str(erro[1]+"\n\t"+str(erro[2])))
        except:
            print("Falha ao salvar o arquivo de log")

    def ler(self):
        try:
            return open(self.caminho, 'r')
        except:
            print("Falha ao ler o arquivo de log.")
        return []
