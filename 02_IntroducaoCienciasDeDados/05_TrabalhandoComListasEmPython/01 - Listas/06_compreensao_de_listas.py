# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]

# Contando ocorrências de um
print(quadrado)


for numero in numeros:
    quadrado.append(numero ** 2)
  
print(quadrado)
