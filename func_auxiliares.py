import time

def VerificaModo(modo):
    
    if modo == 1:
        return 'crescente'
    elif modo == 2:
        return 'decrescente'
    elif modo == 3:
        return 'aleatorio'
    else:    
        return -1
    
def quantidade(qntd):
    
    if qntd == 1:
        return 100
    elif qntd == 2:
        return 1000
    elif qntd == 3:
        return 5000
    elif qntd == 4:
        return 30000
    elif qntd == 5:
        return 50000
    elif qntd == 6:
        return 100000
    elif qntd == 7:
        return 150000
    elif qntd == 8:
        return 200000
    else:
        return -1
    
def current_milli_time():
    return (time.time()*1000)


def ImprimeResultado(algoritmo, vetor_ordenado, tempo_exec):
    #print('Vetor ordenado: {}'.format(vetor_ordenado))
    print('------------------------------------')
    print('Algoritmo: {}'.format(algoritmo))
    #print('Contagem de comparações: {}'.format(count_comparacoes))
    print('Tempo de execução: {}'.format(tempo_exec))
    print('------------------------------------')
    

menu = '1.BubbleSort\n2.InsertionSort\n3.MergeSort\n4.HeapSort\n5.QuickSort\n6.AOH\n7.Salvar dados\n0.Sair'
modo = 'Digite o modo:\n1.Crescente\n2.Decrescente\n3.Aleatorio\n'
qntd = 'Digite a quantidade:\n1.100\n2.1000\n3.5000\n4.30000\n5.50000\n6.100.000\n7.150.000\n8.200.000\n'