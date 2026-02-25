contador=0
soma=0
while contador < 4:
    contador += 1
    nota = float(input(f"Insira o {contador} nota: "))
    soma+=nota

media = soma/contador
print ("A sua média é :",media)
if  media >= 7:
    print ("Você foi Aprovado")
else:
    print ("Você foi Reprovado")