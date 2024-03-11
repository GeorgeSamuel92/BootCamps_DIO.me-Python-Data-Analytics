maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade: "))

#exemplo 03
if idade >= maior_idade:
    print('maior de idade, pode tirare a CNH')
    
if idade < maior_idade:
    print('não pode tira a CNH')
    
#exemplo 02
if idade >= maior_idade:
    print('maior de idade, pode tirare a CNH')
    
else: 
    print('não pode tira a CNH')
    
# exemplo 03
if idade >= maior_idade:
    print('maior de idade, pode tirare a CNH')
    
elif idade >= idade_especial:
    print('menor de idade mas com permissão especial para fazer aulas teoricas')
else: 
    print('não pode tira a CNH')
    
    