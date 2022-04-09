import math
import func_auxiliares as fn


def mergeSort(vetor, p, r):
    inicio = fn.current_milli_time()
    if p < r:
        q = (p + r) // 2
        mergeSort(vetor, p, q)
        mergeSort(vetor, q + 1, r)
        merge(vetor, p, q, r)
    fim = fn.current_milli_time()
    tempo_exec = fim-inicio
    return [vetor, tempo_exec]

def merge(vetor, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = vetor[p + i]
    for j in range(0, n2):
        R[j] = vetor[q + 1 + j]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            vetor[k] = L[i]
            i += 1
        else:
            vetor[k] = R[j]
            j += 1