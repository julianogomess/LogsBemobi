# LogsBemobi
## Aplicação simples desenvolvida em python para leitura de um arquivo de log, analisar a mudança de status de clientes de 3 paises e assim calcular quais paises tem mais clientes ativos.
## A saida do programa é outro arquivo de texto com o nome do pais, a quantidade de usuários em cada pais e por ultimo a quantiadade de usuários ativos.

O arquivo de log é o ["arquivo.log"](arquivo.log) , e após o processamento o arquivo gerado é o ["relatorio.txt"](relatorio.txt) , para auxilio nos teste  foi criado um arquivo python que gera o arquivo de log com numeros aleátórios. O [arquivo](criarLogs.py) esta inicialmente gerando 100 logs, porém é possivel facilmente alterar este código.
O processamento ocorre no [main.py](main.py) na função principal, há um objeto criado chamado Dados para auxiliar na contagem dos usuário totais e ativos .
Para auxiliar no entendimento do código a classe main possui comentários.
