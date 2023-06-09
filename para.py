i = [0]
soma = 0
for i in range (5):
     nota = int(input("Digite nota: "))
     soma = soma + nota
     i = i + 1

media = soma/5
print("A média da sala é %0.1f" %media)