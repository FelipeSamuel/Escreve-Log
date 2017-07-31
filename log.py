from seumodulo import app
from datetime import datetime
import sys
import traceback

class Log(object):
    
    def __init__(self):
        self.__caminho = app.config['LOG_URI']
        self.__exibe = app.config['DEBUG']

    def logging(self):
        try:
            exc_type, exc_value, exc_traceback =  sys.exc_info()
            erro = traceback.format_exception(exc_type, exc_value,exc_traceback)

            with open(self.__caminho, "a") as arquivo:
               conteudo = str(datetime.now())+" => "+str(erro[1]+"\n\t"+str(erro[2]))+"\n"
               conteudo += "************************************************************************************************************************************************************\n"
               arquivo.write(conteudo)

            if self.__exibe:
                print(erro)
        except Exception as e:
            print(e)
