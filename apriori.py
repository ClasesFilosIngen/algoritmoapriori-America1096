##Función que permite crear C1, obteniendo una lista de conjuntos unitarios
def init_pass(T):
    C1 = []
    for conjunto in T:
        for elemento in conjunto:
            if not [elemento] in C1:
                C1.append([elemento])
                
    C1.sort()
    return list(map(frozenset, C1))#Permite crear conjuntos

##Permite crear el conjunto F, que da como resultado los conjuntos de elementos frecuentes
##Para que un conjuntos sea frecuente sus subconjuntos deben ser frecuentes 
def obtenerF(T, Ck, minSup):
    repeticiones = {}
    for conjunto in T:
        for elemento in Ck:
            if elemento.issubset(conjunto):
                if not elemento in repeticiones:
                    repeticiones.setdefault(elemento, 1)
                else:
                    repeticiones.update({elemento : repeticiones.get(elemento)+1})

    Fk = []
    for key in repeticiones:
        if repeticiones[key]/len(T) >= minSup:
            Fk.append(key)

    return Fk

#Funcion que crea Ck, conjuntos candidatos
def cand_gen(Fk, k): 
    C = []
    for i in range(len(Fk)):
        for j in range(i+1, len(Fk)): 
            L1 = list(Fk[i])[:k-2]
            L2 = list(Fk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1==L2: #Si el pirmer elemento de k-2 es igual
                C.append(Fk[i] | Fk[j]) #Se hace una union de los conjuntos
    return C


def apriori(T, minsup):
	C = []
	F = []
	C.append(init_pass(T))
	F.append(obtenerF(T, C[0], minsup))
	k = 2
	while (len(F[k-2]) > 0):
	 	C.append(cand_gen(F[k-2], k))
	 	F.append(obtenerF(T, C[k-1], minsup))
	 	k += 1


T = [['car', 'pol', 'lec'], ['car', 'que'], ['que', 'bot'], 
['car', 'pol', 'que'], ['car', 'pol', 'rop', 'que', 'lec'], 
['pol', 'rop', 'lec'], ['pol', 'lec', 'rop']]

apriori(T, 0.30)
