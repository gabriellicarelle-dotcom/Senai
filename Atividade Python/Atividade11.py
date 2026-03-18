

estoque = {}

# Mensagem de bem vindo
print ("Bem vindo ao sistema de gestão de estoque, desenvolvido por Gabrielli Carelle")

# Repita
while True:
    operacao = input ("Deseja registrar a entrada e saída de produtos? (digite 'entrada' ou 'saída') ou 'sair' ").lower()
    
    # Se não for nnhuma das opções: repita
    if operacao not in ['entrada','saída', 'sair']:
        print ("Operação inválida.")
        continue
    
    # Se opção for sair acontece 
    if operacao == 'sair':
        break
    produto = input ("Nome do produto: ").strip()
    qtd = int(input("Quantidade: ")) 

# Se opçaõ for entrada  acontece
    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd 
        else:
            print ("Erro: produto inexistente ou estoque insuficiente.")

# Mensagem final
print ("\n ---Estoque Final---")
for p, q in estoque.items():
        print (f"{p} : {q}")




# Inicia o programa







