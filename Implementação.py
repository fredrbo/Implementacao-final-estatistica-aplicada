from random import randint      #Números aleatórios
from math import sqrt           #Raiz quadrada
import matplotlib.pyplot as plt #Gráficos
from time import sleep


def printMenu():
    opt = 100
    while opt != 0:
        opt = int(input('''\n######## Menu ########
1- Análisar dados. (Tendência Central e medidas de dispersão)
2- Gerar gráficos
0- Sair
           
Escolha uma opção: '''))      
        
        if opt == 1:
            analisar()
        elif opt == 2:
            graf()
        elif opt == 0:
            print('\nAté mais!')
            break

# Tendência central
def sort(array):

    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break
        
    return array

def media(array):
   return sum(array)/len(array)

def mediana(array):
    
     if len(array) % 2 == 0:
        mid = (len(array)/2) 
        return (array[int(mid)] + array[int(mid)-1])/2
     else:
        mid = (len(array)/2) -0.5
        return array[int(mid)]

def moda(array):
    max = (0,0)
    for n in array:
        m = array.count(n)
        if m > max[0]:
            max = (m, n)
    return max[1]

#Dispersão
def desvio(array,index):
    desvio = []
    media = sum(array)/len(array)
    for x in range(len(array)):
        desvio.append(array[x] - media)
        
    return desvio[index]

def desvioM(array):
    desvio = []
    media = sum(array)/len(array)
    for x in range(len(array)):
        desvio.append(array[x] - media)
        if desvio[x] < 0:
            desvio[x] = desvio[x] * (-1)
        
    return sum(desvio)/len(array)

def analisar():
    opt = 100
    while open != 9:
        opt = int(input('''\nDeseja digitar os dados ou gerar automaticamente?
1- Digitar dados
2- Gerar automaticamente
0- Voltar

Escolha uma opção: '''))
        # Array digitado
        if opt == 1:
            quantidade = int(input("Quantos dados quer colocar? "))
            dados =[]
            
            for x in range(quantidade):
                n = int(input(f'Dado {x + 1}: '))
                dados.append(n)
            print(f'Dados organizados {sort(dados)}\n') 
            print(f'\nMedidas centrais dos dados.\n Media - {"%.2f"% media(dados)}\n Moda - {moda(dados)}\n Mediana - {mediana(dados)}')
            print("\nDispersão")
            for x in range(len(dados)): 
                print(f' Desvio do {x+1}º elemento: {"%.2f"% desvio(dados, x)}')
    
            print(f' Desvio médio: {desvioM(dados)}')
            var = [] # quadrados dos desvios
            for x in range(len(dados)): 
                var.append(desvio(dados, x) *desvio(dados, x) )
            print(f' Variância: { sum(var)/len(dados)}')
            print(f' Desvio padrão: {"%.2f"% sqrt((sum(var)/len(dados)))}')
            
            
        ##Creating random array
        elif opt == 2:         
            dados = [] 
            quantidade = int(input("Quantidade de dados: "))
            min = int(input("Valor minimo: "))
            max = int(input("Valor máximo: "))
                    
            for n in range(quantidade):
                aleat = randint(min, max)
                dados.append(aleat)
            dados = sort(dados)
            print(f'Dados sortidos e organizados {dados}\n')           
            print(f'\nMedidas centrais dos dados.\n Media - {"%.2f"% media(dados)}\n Moda - {moda(dados)}\n Mediana - {mediana(dados)}')
            
            print("\nDispersão")
            for x in range(len(dados)): 
                print(f' Desvio do {x+1}º elemento: {"%.2f"% desvio(dados, x)}')
            print(f' Desvio médio: {desvioM(dados)}')
            
            var = [] # quadrados dos desvios
            for x in range(len(dados)): 
                var.append(desvio(dados, x) *desvio(dados, x) )
            print(f' Variância: {sum(var)/len(dados)}')
            print(f' Desvio padrão: {"%.2f"% sqrt((sum(var)/len(dados)))}')
        elif opt == 0:
            break
            
# graficos
def delay():
    print('Carregando gráfico...')
    sleep(1.2)

def graf():
    x = []
    y = []
    nome = input("Nome do gráfico: ")
    plt.title(nome)
   
    quantX = int(input("\nQuantidade de variaveis : "))
    for n in range(quantX):
        varX = input(f'Nome da {n+1}ª variavel: ')
        x.append(varX)
    for n in range(quantX):
        varY = int(input(f'Valor da variavel {x[n]}: '))
        y.append(varY)

    cores= ["y","r","b","g"]
    cor= randint(0,3)

    tipo = 10
    while tipo != 0:
        tipo = int(input('''\n1 - Linha
2 - Barra
3 - Pizza
0 - Voltar menu
Escolha o tipo do gráfico: '''))

        if tipo == 1 :
            plt.plot(x,y, color = cores[cor])
            delay()
            plt.show()
            
            
        elif tipo ==2:
            plt.bar(x,y, color = cores[cor])
            delay()
            plt.show()
            

        elif tipo == 3:
             plt.pie(y, labels = x, startangle = 90, shadow = True)
             delay()
             plt.show()
             

        elif tipo == 0:
           break       
            

### inicio
print('''Implementação Tópicos Estatistica Aplicada
FATEC São José dos Campos
Desenvolvido por: Frederico Rabelo 4ºADS-B
Professor: Dawilmar''')

printMenu()


