import func_auxiliares as fn


def InsertionSort(vetor):
    inicio = fn.current_milli_time()
    for j in range(1,len(vetor)):
        chave = vetor[j]
        i = j - 1
        while i >= 0 and vetor[i]>chave:
            vetor[i+1] = vetor[i]
            i = i - 1
        vetor[i+1] = chave
    fim = fn.current_milli_time()
    tempo_exec = fim-inicio
    return [vetor, tempo_exec]

            
    