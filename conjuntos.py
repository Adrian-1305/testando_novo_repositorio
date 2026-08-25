conj1= {1,2,3,4}
conj2 = {3,4,5,6}
print("Primeiro conjunto: ", conj1)
print("Segundo conjunto: ", conj2)
uniao = conj1.union(conj2)
print ("união dos conjuntos 1 e 2: ", uniao)
intersec = conj1.intersection(conj2)
print("Interseção do conjunto 1 e 2:",intersec)
difer1 = conj1.difference(conj2)
difer2 = conj2.difference(conj1)
print("diferença entre do conjunto 1 e 2:",difer1,'e',difer2)

