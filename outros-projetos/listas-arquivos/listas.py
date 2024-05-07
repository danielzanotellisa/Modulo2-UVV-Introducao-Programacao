# Listas são como tuplas, porém possui algumas diferenças
# Usamos colchetes para abrir e fechar uma lista
# Diferentemente das tuplas, listas são mutáveis
from time import sleep


lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

print(lanche)

lanche[3] = 'Picolé' #Mudando o índice 3 que era Pudim para Picolé

print(lanche)

#Podemos adicionar itens na nossa lista de duas formas
    # .append() - Adiciona ao final da lista
    # .insert(index,objeto) - Adiciona o objeto no index selecionado

lanche.append('Biscoito')

print(lanche)

lanche.insert(0,'Cachorro Quente')

print(lanche)

#Podemos eliminar elementos de duas formas
    # com o comando del lista[i]
    # com o método .pop(i) se não informamos o índice, ele eliminará o último item
    # com o método .remove(valor do item a ser eliminado)

del lanche[3] #Removemos o índice 3 que era Pizza

print(lanche) 

lanche.pop(0) #Removemos o Cachorro Quente

print(lanche)

lanche.remove('Suco') #Removendo um item baseado no seu valor

print(lanche)

#Podemos criar uma lista com o comando range

valores = list(range(0,10)) #Lembrando que o comando range irá excluir o valor final

print(valores)

#O método .sort() serve para organizar nossa lista, podemos usar também o sort(reverse=True) para ordezar de tras pra frente

#Podemos usar a função interna len() para saber o tamanho da nossa lista

print(len(valores))


#O remove elimina somente o primeiro valor correspondente na lista 

valores.append(2)

print(valores)

valores.remove(2) #Removeu o primeiro número 2 que ele encontrou

print(valores) 

valores.insert(2, 2)

print(valores)

#Aqui percorremos a lista inteira para achar todos os valores 2 e removê-los
for n in valores:
    if 2 in valores:
        valores.remove(2)
    print(n)
    sleep(0.5)

print(valores)


outros_valores = []
print(outros_valores)
for n in range(0,5+1):
    outros_valores.append(n)
    print(outros_valores)
    sleep(0.5)

for n in range(len(outros_valores)):
    print(outros_valores)
    outros_valores.pop()
    sleep(0.5)

print(outros_valores)


#Quando igualamos duas listas estamos fazendo uma ligação entre elas, logo tudo oque alterarmos em uma será alterado em outra

a = [2,4,5,6]
b = a

print(a)
print(b)

b[2] = 3

print(a)
print(b)

#Para copiarmos uma lista para a outra, usamos o seguinte método

b = a[:]
b[2] = 8
print(a)
print(b) #Aqui percebemos a diferença