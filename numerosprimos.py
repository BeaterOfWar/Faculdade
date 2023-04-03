N = int(input('Quantidade de testes = '))
#N será a quantidade de testes a serem feitas
for repeticao in range (N):
    X = int(input('Número a ser testado = '))
    #X será o numero a ser testado 
    contador = 0
    #A Variável "contador" serve para o programa testar quantas vezes o numero foi dividido
    #Pois um numero primo só pode ser dividido por dois numeros diferentes;
    for divisor in range (1, X+1):
        #1 e ele mesmo
        if X % divisor == 0:
         contador = contador + 1
         #caso o resto da divisão dê zero o contador recebera mais um
    if contador == 2:
        #se o contador for igual a 2 o numero é primo pois ele foi dividido por dois numeros diferentes apenas
        print ('eh primo')
    else:
        #caso o contador seja diferente de 2 ele não é primo
        print ('nao eh primo')