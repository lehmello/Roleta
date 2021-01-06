import random
def aleatorio ():
    n = int (random.randint(0, 36))
    if n == 36 :
        n = 0        
    return n
jogador = 1000
banca= 5000
aposta = int
while jogador > 0 and banca > 0 :
    print("------------------------------------------------------------------")
    print("Seu valor na carteira: ", jogador)
    print("Valor da banca: ", banca)
    print("------------------------------------------------------------------")
    print("Apostar em numero par, digite PAR.")
    print("Apostar em numero impar, digite IMPAR.")
    print("Apostar em qualquer numero especifico, digite NUMERO.")
    print("Digite o tipo de aposta: ")
    tipo = str (input (""))
    print("------------------------------------------------------------------")
    valor = int (input("Digite o valor da sua aposta "))
    while valor > jogador:
    	valor = int (input("Digite um valor que tenha na sua carteira "))
    if tipo == "PAR" or tipo == "par":
        num = int(aleatorio())
        print ("O numero sorteado foi: ", num)
        if num % 2 == 0:
            print("Parabens! voce acertou!")
            jogador= jogador + valor
            banca= banca - valor
        if num % 2 != 0:
            print("Que pena, voce perdeu!")
            jogador= jogador - valor
            banca= banca + valor
    if tipo == "IMPAR" or tipo == "impar":
        num = int(aleatorio())
        print ("O numero sorteado foi: ", num)
        if num % 2 != 0:
            print("Parabens! voce acertou!")
            jogador= jogador + valor
            banca= banca - valor
        if num % 2 == 0:
            print("Que pena, voce perdeu!")
            jogador= jogador - valor
            banca= banca + valor
    if tipo == "NUMERO" or tipo == "numero":
        n= int (input("Digite seu numero entre 1 à 36: "))
        while n < 1 or n> 36:
            n= input("Digite um numero entre 1 à 36: ")
        num = int(aleatorio())
        print ("O numero sorteado foi: ", num)
        if num == n:
            print ("Voce acertou o numero! Parabens!")
            jogador = jogador + (valor*30)
            banca = banca - (valor*30)
        if num != n or num == 0:
            print ("Voce errou o numero!")
            jogador = jogador - valor
            banca = banca + valor
        
if jogador <= 0:
    print("Voce perdeu tudo! O jogo acabou.")
if banca <=0:
    print("Voce ganhou todo o dinheiro da banca! Parabens!")
            
    
        
    
