#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = input().split()

elementos = []
for elemento in t:
    if elemento.isdigit() or (elemento[0] == '-' and elemento[1:].isdigit()):
        elementos.append(int(elemento))
    elif elemento.replace('.', '', 1).isdigit():
        elementos.append(float(elemento))
    else:
        elementos.append(elemento)

elementos_invertidos = elementos[::-1]

print(tuple(elementos_invertidos))
