# Mensagem de boas-vindas
print("Bem-vindo ao sistema de controle de acesso!")
print("Desenvolvido por Gabrielli\n")

# Pergunta o dia da semana.
# lower quer dizer que se o usúario digitar com letra maiúscula ou minúscula  o programa vai entender igual
dia = input("Digite o dia da semana: ").lower()

# Tipo de usuário
tipo = input("Você é membro ou visitante? ").lower()

# Se for visitante, pede o tempo de permanência
# == é um operador de comparação
if tipo == "visitante":
    horas = int(input("Quantas horas deseja permanecer? "))
else:
    horas = 0  # membro não precisa informar as horas


# Verifica se é fim de semana
if dia == "sabado" or dia == "domingo":
    
    if tipo == "membro":
        print("Acesso permitido: membros podem entrar no fim de semana.")
    else:
        print("Acesso negado: visitantes não podem entrar no fim de semana.")

# Caso seja dia útil (segunda a sexta)
else:
    
    if tipo == "membro":
        print("Acesso permitido: membros têm acesso ilimitado em horário comercial.")
    
    elif tipo == "visitante":
        # Verifica limite de horas
        if horas <= 4:
            print("Acesso permitido: tempo dentro do limite de 4 horas.")
        else:
            print("Acesso negado: visitantes só podem ficar até 4 horas.")
    
    else:
        print("Tipo de usuário inválido.")

