import time
import mergesort as ms
import func_auxiliares as fn

def InsertionSort(vetor):
    count_comparacoes = 0
    for j in range(1,len(vetor)):
        chave = vetor[j]
        i = j - 1
        count_comparacoes+=1
        while i >= 0 and vetor[i]>chave:
            count_comparacoes+=1
            vetor[i+1] = vetor[i]
            i = i - 1
        vetor[i+1] = chave
        if count_comparacoes > (len(vetor)-1):
              return 0
    return 1


def AOH(vetor):
  inicio = fn.current_milli_time()
  resposta = InsertionSort(vetor)
  if resposta != 1:
    vetor, tmp = ms.mergeSort(vetor,0,(len(vetor)-1))
  fim = fn.current_milli_time()
  tempo_exec = fim-inicio
  return vetor, tempo_exec 