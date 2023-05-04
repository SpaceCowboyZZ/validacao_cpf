lista_resultados = [] #lista final que vai receber o cpf multiplicado
lista_resultados2 = []
multiplicador1 = 10 #o nome já diz o q é, vai receber -1 até ser igual a 2 
i = 0 #indice q vai receber +1 toda vez q multiplicar
while True:
    cpf_digitado = input(' digite o seu cpf: ')
    if len(cpf_digitado) != 11:
        print(' digite somente os 11 numeros do cpf ')
    else:
        try:
            cpf =[int(numeros) for numeros in cpf_digitado] #transforma de string para int e separa todos os numeros
            entrada_sequencial = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)
            if entrada_sequencial:
                print(' você digitou dados em sequencia ')
                continue
            while multiplicador1 >= 2 and i < 10:
                resultado_parcial = multiplicador1 * cpf[i]
                lista_resultados.append(resultado_parcial)
                multiplicador1 -= 1
                i += 1
                continue
        except ValueError:
            print('lerro: digite somente numeros! ')
        primeiro_digito = ((sum(lista_resultados) * 10) % 11)
        if primeiro_digito > 9:
            primeiro_digito = 0
            continue
        elif primeiro_digito == cpf[9]:
            multiplicador1 = 11
        else:
            print(' cpf invalido ')
            break
        while multiplicador1 >= 2 and i < 11:
            resultado_parcial2 = multiplicador1 * cpf[i]
            lista_resultados2.append(resultado_parcial2)
            multiplicador1 -= 1
            i += 1
            continue
        segundo_digito = (sum(lista_resultados2) * 10) % 11
        if segundo_digito > 9:
            segundo_digito = 0
            continue
        elif segundo_digito == cpf[10] and primeiro_digito == cpf[9]:
            print(' valido ')
        else:
            print(' cpf invalido ')
            break
            
        
        