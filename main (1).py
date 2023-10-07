# x = [1,3,6,9,845]
# print(x[4]
# frutas = ['macã', 'banana', 'uva', 'cereja', 'true']
# print(frutas[4])


# frutas = ['macã', 'banana', 'uva', 'cereja', True]
# frutas.append('melão')
# print(frutas)

#remove 
# frutas = ['maça', 'banana', 'uva', 'cereja', True]
# frutas.remove('uva')
# print(frutas)

#del - remove pelo indice
# frutas = ['maça', 'banana', 'uva', 'cereja', True]
# frutas.del([3])
# print(frutas)

##Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 5 e imprima-a na tela.

numeros =[1,2,3,4,5]
print(numeros)

##Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
print(numeros[2])

##Exercício 3: Adicione o número 6 à lista numeros e imprima a lista atualizada.
numeros.append(6)
print(numeros)

##Exercício 4: Remova o número 3 da lista numeros e imprima a lista resultante.
numeros.remove(3)
print(numeros)

##Exercício 5: Crie uma lista chamada frutas contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
frutas = ['maça', 'banana', 'uva']
print(frutas + numeros)

##Exercício 6: Use um loop for para percorrer e imprimir todos os elementos da lista frutas.
for fruta in frutas:
  print(frutas)

##Exercício 7:** Verifique se o número 5 está presente na lista `numeros` e imprima uma mensagem informando se ele está na lista ou não.
n = 5
if 5 in numeros:
  print(f'O numéro solicitado esta na lista: {n}')
else:
 print("Não esta na lista: ",)