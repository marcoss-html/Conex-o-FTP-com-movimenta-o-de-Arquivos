def diaDaSemana(argument):
    switcher = {
        0: "segunda",
        1: "terca",
        2: "quarta",
        3: "quinta",
        4: "sexta",
        5: "sabado",
        6: "domingo"
    }
 
    return switcher.get(argument, "nothing")

def renomearArquivoData(dataDeOntem):
    ano = dataDeOntem.year
    mes = dataDeOntem.month
    dia = dataDeOntem.day

    #verificar se o mes tem 1 digito, se sim adicionar 0 na frente
    
    if len(str(mes)) == 1:
        mes = f'0{mes}'

    #verificar se o dia tem 1 digito, se sim adicionar 0 na frente
    if len(str(dia)) == 1:
        dia = f'0{dia}'
  
    dataFormatada = f'{ano}{mes}{dia}'
    nomeArquivo = f'{dataFormatada}.rar'
    return nomeArquivo

#from datetime import date
#print(renomearArquivoData(date.today()))