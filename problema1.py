#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()

for i in range(1, len(t2)):
    t2[i] = int(t2[i])

tupla = tuple([f"'{item}'" if isinstance(item, str) else item for item in t2 + t1 + t2])

print('(' + ', '.join(map(str, tupla)) + ')')
