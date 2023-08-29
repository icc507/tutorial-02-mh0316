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

valor1 = t1[0]
valor2 = int(t1[1])
valor3 = t1[2]
valor4 = t2[0]
valor5 = int(t2[1])

tupla = (f"('{valor4}', {valor5}, {valor1}, {valor2}, '{valor3}', '{valor4}', {valor5})")

print(tupla)
