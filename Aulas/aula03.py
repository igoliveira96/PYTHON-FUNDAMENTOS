#Operações aritméticas

'''
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

'''
numA = int(input('Primeiro valor: '))
numB = int(input('Segundo valor: '))
soma = numA + numB
subtracao = numA - numB
multiplicacao = numA * numB
divisao = numA / numB
divisaoInteira = numA // numB
potencia = numA ** numB
print('A soma é: {}'.format(soma))
print('A subtração é: {}'.format(subtracao))
print('A multiplicação é: {}'.format(multiplicacao))
print('A divisão é: {}'.format(divisao))
print('A divisão inteira é: {}'.format(divisaoInteira))
print('A potência é: {}'.format(potencia))
'''

#Desafio - 1:
'''
numero = int(input('Digite um número: '))
sucessor = numero + 1;
antecessor = numero - 1;
print('O sucessor do número {} é {}'.format(numero, sucessor))
print('O antecessor do número {} é {}'.format(numero, antecessor))
'''

#Desafio - 2:
'''
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)
print('O dobro do número {} é {}'.format(numero, dobro))
print('O triplo do número {} é {}'.format(numero, triplo))
print('A raiz quadrada do número {} é {}'.format(numero, raizQuadrada))
'''

#Desafio - 3:
'''
notaUm = float(input('Digite a primeira nota: '))
notaDois = float(input('Digite a segunda nota: '))
media = (notaUm + notaDois) / 2
print('A média das notas é: {}'.format(media))
'''

#Desafio - 4:
'''
metros = float(input('Digite um valor (metros): '))
centimetros = metros * 100;
milimetros = centimetros * 10;
print('{} metro(s) em centímetros é {}'.format(metros, centimetros))
print('{} metro(s) em milímetros é {}'.format(metros, milimetros))
'''

#Desafio - 5:
'''
numero = int(input('Tabuada do número? '))
print('{} * 1 = {}'.format(numero, numero*1))
print('{} * 2 = {}'.format(numero, numero*2))
print('{} * 3 = {}'.format(numero, numero*3))
print('{} * 4 = {}'.format(numero, numero*4))
print('{} * 5 = {}'.format(numero, numero*5))
'''

#Desafio - 6:
'''
dinheiro = float(input('Informe a quantia: '))
conversao = dinheiro * 3.27
print('O valor de R$ {} em dólar é: {}'.format(dinheiro, conversao))
'''

#Desafio - 7:
'''
largura = int(input('Informe a largura da parede: '))
altura = int(input('Informe a altura da parede: '))
area = largura * altura
qtdLitros = area / 2;
print('A área a ser pinta é de {} metros quadrados'.format(area))
print('A quantidade de litros de tinta necessário é {}'.format(qtdLitros))
'''

#Desafio - 8:
'''
precoProduto = float(input('Informe o preço do produto: '))
novoPreco = precoProduto - (precoProduto * 0.05)
print('O novo valor com o desconto de 5% é: {}'.format(novoPreco))
'''

#Desafio - 9:

salario = float(input('Informe o salário: '))
novoSalario = salario + (salario * 0.15)
print('O novo salário com aumento de 15% é {}'.format(novoSalario))
