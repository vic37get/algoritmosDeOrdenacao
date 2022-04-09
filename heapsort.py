import func_auxiliares as fn

def Right(i):
    return 2 * i + 1


def Left(i):
    return 2 * i


def MaxHeapify(vetor, n, i):
    l = Left(i)
    r = Right(i)
    if l < n and vetor[l] > vetor[i]:
        maior = l
    else:
        maior = i
    if r < n and vetor[r] > vetor[maior]:
        maior = r
    if maior != i:
        aux = vetor[i]
        vetor[i] = vetor[maior]
        vetor[maior] = aux
        MaxHeapify(vetor, n, maior)


def BuildMaxHeap(vetor):
    n = len(vetor)
    for i in range((n//2) - 1, -1, -1):
        MaxHeapify(vetor, n, i)
        

def HeapSort(vetor):
    inicio = fn.current_milli_time()
    BuildMaxHeap(vetor)
    n = len(vetor)
    for i in range(n-1, 0, -1):
        aux = vetor[i]
        vetor[i] = vetor[0]
        vetor[0] = aux
        MaxHeapify(vetor, i, 0)
    fim = fn.current_milli_time()
    tempo_exec = fim - inicio
    return [vetor, tempo_exec]
