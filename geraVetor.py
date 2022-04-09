import random
import json


def GeraVetor(tamanho):
    vetor = list(range(0,tamanho))
    random.shuffle(vetor)
    
    return vetor



vetor1  = GeraVetor(200000)
vetor2 = list(range(0,200000))
vetor3 = list(range(200000,0,-1))


with open('aleatorio.json','w') as f:
    json.dump(vetor1,f)
    
with open('crescente.json','w') as g:
    json.dump(vetor2,g)

with open('decrescente.json','w') as h:
    json.dump(vetor3,h)