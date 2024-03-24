opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Opção de saque selecionada")
    elif opcao == 2:
        print("Exibindo o extrato")
else:
    print("obrigado por usar nosso sistema")