frase = 'Manipulação de String'
print(frase)

#--Fatiamento--
print('Fatiamento: ')
print(frase[3], '\n')
#mostra a letra 'i'

#--Fatimento com intervalo--
print('Fatiamento com intervalo: ')
print(frase[3:5]) #vai de 3 até 5, sem o 5 no caso.
#mostra 'ip'
print(frase[0:3])
#ou
print(frase[:3]) #vai de 0 até 3, sem o 3.
#mostra 'Man' 
print(frase[:13:2]) #o numero depois do segundo ':' indica um salto de quanto em quanto
#mostra 'Mnplaçod'
print(frase[::-1],'\n') #mostra a frase de trá pra frente
#mostra 'gnirtS ed oãçalupinaM'



#--Texto Grandes--
print('Texto grande """: ', """Um dia descobrimos que beijar uma pessoa para esquecer outra é bobagem.
Você não só não esquece a outra pessoa como pensa muito mais nela...
Um dia nós percebemos que as mulheres têm instinto "caçador" e fazem qualquer homem sofrer...\n""")
#usando """ pode-se colocar textos grandes.

#--Contagem de caracteres--
#frase.count(elemento, intervalo) -> não é necessario colocar o intervalo
print('.count(): ' , frase.count('a'))
#mostra quantas vezes aparece o elemento na string.


#--Procurar elemento--
#frase.find(elemtento, intervalo) -> não é necessario colocar o intervalo
print('.find(): ' , frase.find('a')) #mostra a posição onde está a primeira aparição do elemento

#--Substituir elemento--
#frase.replace(elemento, novoElemento)
print('.replace(): ' , frase.replace('String' , 'Inteiros'))#mostra 'Manipulação de Inteiros'

#--Tamanho--
print('len(): ', len(frase)) #mostra o tamanho da frase
#mostra 21

#METODOS PARA STRING:
print('\nMetodos para string: \n')
#.strip()
print('.strip(): ', frase.strip()) #remove todos os espaços inuteis da string

#.upper()
print( '.Upper(): ',frase.upper()) #transforma toda a string em letras maiusculas

#.lower()
print('.lower(): ' , frase.lower()) #transforma toda a string em letras minusculas

#.captalize()
print('.captalize(): ' , frase.capitalize()) #transforma todas as letras da string em minusculas e a primeira letra em maiuscula

#.title()
print('.title(): ' , frase.title()) #coloca só as primeiras letras de cada frase maiusculas, usando a posição dos espaços

#.split()
print('.split(): ' , frase.split()) #cria uma lista com partes da frase

#.join()
print('.join(): ' , ' '.join(frase)) #junta usando  