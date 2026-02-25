
nome = input("Insira o seu nome: ")
idade = int(input("Insira sua idade: "))

#repete quandoa idade for valida
while idade < 120 or idade > 0:
    idade = int(input("Idade(anos completos - ate 120 anos)"))
    dias_vida = idade * 365
    print (f"{nome}, você viveu {dias_vida} dias")

