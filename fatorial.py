n = int(input("Digite o valor de n: "))
fatorial = 1
count = 2
while (count <= n):
    fatorial *= count
    count += 1

print(fatorial)