import random
dados = [0,0,0,0,0]

list = [0,1,2,3,4]



def tirada(lista):
    for i in lista:
        dados[i] = random.randrange(1,7)
        print (dados)
    return dados


#todos los dados iguales
def es_generala(lista):
    if lista[0] == lista[1] == lista[2] == lista[3] == lista[4]:
        return True
    else:
        return False

#4 dados iguales
def es_poker(lista):
    if lista[0] == lista[1] == lista[2] == lista[3]:
        return True
    else:
        return False

def es_escalera(lista):
    pass

def es_full(lista):
    pass

print(es_generala(tirada(list)))
print(es_poker(tirada(list)))
