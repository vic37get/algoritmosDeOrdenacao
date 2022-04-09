import bubblesort
import json
import insertionsort
import q
import heapsort
import mergesort
import func_auxiliares as fn
import AOH
import pandas as pd


def ExecutaAlgoritmo(nome,algoritmo, modo, quantidade):
    if quantidade == -1:
        print('Opção inválida!\n')
        return
    
    with open('{}.json'.format(modo), 'r') as f:
        dados = json.load(f)
    vetor = dados[0:quantidade]
    if nome != 'QuickSort' and nome!= 'MergeSort':
        vetor_ordenado, tempo_exec = algoritmo(vetor)
        fn.ImprimeResultado(nome, vetor_ordenado, tempo_exec)
    else:
        vetor_ordenado, tempo_exec = algoritmo(vetor,0,len(vetor)-1)
        fn.ImprimeResultado(nome,vetor_ordenado, tempo_exec)
    return [nome, tempo_exec]
    
    
        
def main():
    dados = pd.DataFrame()
    op = -1
    while(op != 0):
        print(fn.menu)
        op = int(input('Digite uma opção: \n'))
        if op == 1:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('BubbleSort',bubblesort.BubbleSort, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
                
        elif op == 2:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('InsertionSort',insertionsort.InsertionSort, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
             
        elif op == 3:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('MergeSort',mergesort.mergeSort, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
             
        elif op == 4:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('HeapSort',heapsort.HeapSort, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
             
        elif op == 5:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('QuickSort',q.QuickSort, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
             
        elif op == 6:
            modo =  int(input(fn.modo))
            modo = fn.VerificaModo(modo)
            qntd = int(input(fn.qntd))
            qntd = fn.quantidade(qntd)
            print('Aguarde...\n')
            nome, tempo_exec = ExecutaAlgoritmo('AOH',AOH.AOH, modo, qntd)
            dados = dados.append({'Algoritmo': nome, 'Modo': modo, 'Quantidade': qntd, 'Tempo de Execução': tempo_exec}, ignore_index=True)
             
        elif op == 7:
            dados.to_csv('dados.csv', encoding='utf-8')
            print('Dados salvos com sucesso!\n')
            
        elif op == 0:
            print('Fim do programa.\n')
            return

main()
        


