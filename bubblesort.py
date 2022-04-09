import func_auxiliares as fn



def BubbleSort(vetor):
    inicio = fn.current_milli_time()
    for i in range(1,len(vetor)):
        for j in range(len(vetor)-1,0,-1):
            if vetor[j] < vetor[j-1]:
                vetor[j-1], vetor[j] = vetor[j], vetor[j-1]
    fim = fn.current_milli_time()
    tempo_exec = fim-inicio
    return [vetor, tempo_exec]