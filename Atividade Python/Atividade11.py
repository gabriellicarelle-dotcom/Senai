

estoque = {}

print ("Bem vindo ao sistema de gestão de estoque, desenvolvido por Gabrielli Carelle")

while True:
    operacao = input ("Deseja registrar a entrada e saída de produtos? (digite 'entrada' ou 'saída') ou 'sair' ").lower()
    
    if operacao not in ['entrada','saída', 'sair']:
        print ("Operação inválida.")
        continue
    
    if operacao == 'sair':
        break
    produto = input ("Nome do produto: ").strip()
    qtd = int(input("Quantidade: ")) 

    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd 
        else:
            print ("Erro: produto inexistente ou estoque insuficiente.")

print ("\n ---Estoque Final---")
for p, q in estoque.items():
        print (f"{p} : {q}")




# Inicia o programa







