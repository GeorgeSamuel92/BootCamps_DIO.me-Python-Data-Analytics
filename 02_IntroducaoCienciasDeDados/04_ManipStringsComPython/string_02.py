nome = 'Guilherme'
idade = 28
profissão = "programador"
linguagem = "Python"
saldo = 45.34542252

dados = {'nome': 'Guilherme', 'idade': 28, 'profissão': 'programador', 'linguagem': 'Python',}

print("Nome: %s, Idade: %d, Profissão: %s, Linguagem: %s" % (nome, idade, profissão, linguagem))

print("Nome: {}, Idade: {}, Profissão: {}, Linguagem: {}".format(nome, idade, profissão, linguagem))

print("Nome: {0}, Idade: {1}, Profissão: {2}, Linguagem: {3}, Nome: {0} {0} ".format(nome, idade, profissão, linguagem))

print("Nome: {nome}, Idade: {idade}, Profissão: {profissão}, Linguagem: {linguagem}".format(nome=nome, idade=idade, profissão=profissão, linguagem=linguagem))

print("Nome: {nome}, Idade: {idade}, Profissão: {profissão}, Linguagem: {linguagem}".format(**dados))

print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissão}, Linguagem: {linguagem}")

print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissão}, Linguagem: {linguagem}, Saldo: {saldo:10.2f}")
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissão}, Linguagem: {linguagem}, Saldo: {saldo:.2f}")