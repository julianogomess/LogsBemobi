
#Objeto auxiliador para os dados
class Dados(object):
    def __init__(self,pais, user , ativos):
        self.pais = pais
        self.user = user
        self.ativos = ativos



#função principal
def main():

    #apenas os 3 paises
    dados = [Dados("Brasil",0,0),Dados("Chile",0,0),Dados("Mexico",0,0)]
    
    #lista dos usuarios com status de ativo
    listaAtivos = []

    #lista dos usuários com status de cancelados
    listaCancelados = []


    file1 = open("arquivo.log", "r")
    #checa linha por linha do arquivo e aumenta a contagem
    for x in file1:
        if not x.isspace():
            vazio = x.find(" ")
            cod_user = x[0:vazio]
            cod_pais = x[0:2]
            #checa o pais do usuário
            if cod_pais=="55":
                i = 0
            elif cod_pais=="56":
                i = 1
            elif cod_pais=="52":
                i = 2
            
            #checa se o usuário ja foi contabilizado anteriomente
            ativo = listaAtivos.count(cod_user)>0
            cancel = listaCancelados.count(cod_user)>0
            status = x[vazio+1]
            if ativo:
                #checa se o usuario ativo trocou para cancelado
                if status=="c":
                    dados[i].ativos -= 1
            elif cancel:
                #checa se o usuário assinou novamente
                if status=="a":
                    dados.ativos += 1
            else:
                #caso seja a primeira vez do usuário
                dados[i].user += 1
                if status=="a":
                    dados[i].ativos += 1
                    listaAtivos.append(cod_user)
                else:
                    listaCancelados.append(cod_user)

    #escreve o relatorio no outro arquivo
    file2 = open("relatorio.txt", "w")
    for x in dados:
        file2.write(x.pais + " , " + str(x.user) + " , " + str(x.ativos)+"\n")
            
    file2.close


main()
