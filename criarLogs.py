import random

def criarLogs():
    #aqui pode se alterar a quantidades de logs que estarão presentes
    numLogs = 100

    #variaveis auxiliadoras
    cod_area = [55,56,52]
    tipo = ["assinado","cancelado"]
    file = ""

    #criação de cada log
    for x in range(0,numLogs):
        msg = str(random.choice(cod_area)) + str(random.randint(100000,999999)) + str(random.randint(100000,999999)) + " "+ str(random.choice(tipo))+"\n"
        file += msg
    #criando o arquivo
    f = open("arquivo.log","w")
    f.write(file)
    f.close


criarLogs()
