conta_normal = False
conta_universitaria = False
conta_especial = True


saldo = 1000
saque = 2500
cheque_especial = 450


if conta_normal :
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado utilizando o cheque especial!")
    else:
        print("não é possivel fazer o saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente, saque não realizado")
elif conta_especial:
    print("selecionada")
else:
    print("Sistema não reconheceu esse tipo de conta, entrem em contado com seu gerente!")