from log import Log

config['LOG_URI'] = 'path/to/log'

# criando o Objeto LOG
log = Log()

# Simulando uma exception
try:
    num = 0/0
except:
    # Testando a escrita de uma exception
    log.log()

try:
    # Testando a Leitura de uma excetion
    # variavel 'i' recebe a linha do arquivo
    for i in log.ler():
        print(i)
except Exception as detalhe:
    log.log(detalhe)
