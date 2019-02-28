def init_pass(T):
    C1 = []
    for x in range(len(T)):
    	for y in range(len(T[x])):
    		if not T[x][y] in C1:
    			C1.append(T[x][y])
    C1.sort()
    return C1

def obtenerF(T, C, minsup):
	dic = {}
	for conjunto in T:
		for elemento in conjunto:
			dic.setdefault(elemento, 0)
			keys = dic.keys()
			if elemento in keys:
				dic.update({elemento : dic.get(elemento)+1})
	
	for key in dic:
		if dic[key]/len(C) < minsup:
			C.remove(key)			
	return C

def cand_gen(F, T):
	C, aux = [], []
	i = 0
	for f1 in range(len(F)-1):
		for f2 in range(len(F)-1):
			c  = []
			if F[f1] != F[f2+1] and F[f2+1] not in aux:
				c.append(F[f1])
				c.append(F[f2+1])
				C.append(c)

		for s in F:
			pass	
		
		aux.append(F[f1])
			
	return C
			

def apriori(T, minsup):
	C = []
	F = []
	C.append(init_pass(T))
	F.append(obtenerF(T, C[0], minsup))
	k=1
	#for x in F[k-1]:
	#	print(F[0])
	C.append(cand_gen(F[k-1], T))
	#F.append(obtenerF(T, C[1], minsup))
	#	k=k+1
	print(C)
s = [['rop', 'pol', 'lec'], ['car', 'que'], ['que', 'bot'], 
['car', 'pol', 'que'], ['car', 'pol', 'rop', 'que', 'lec'], 
['pol', 'rop', 'lec'], ['pol', 'lec', 'rop']]

apriori(s, 0.30)