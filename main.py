
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
    file1 = open("arquivo.log", "r")
    #checa linha por linha do arquivo e aumenta a contagem
    for x in file1:
        if not x.isspace():
            cod_pais = x[0] + x[1]
            aux = x.find("assinado")
            if cod_pais=="55":
                i = 0;
            elif cod_pais=="56":
                i = 1;
            elif cod_pais=="52":
                i = 2;
            dados[i].user += 1;
            if aux!= -1:
                dados[i].ativos += 1

    #escreve o relatorio no outro arquivo
    file2 = open("relatorio.txt", "w")
    for x in dados:
        file2.write(x.pais + " , " + str(x.user) + " , " + str(x.ativos)+"\n")
            
    file2.close;


main()
