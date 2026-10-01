cont = 0
soma = 0
avg = 0
num = float(input("Digite uma nota: "))
while num != -1:
    
    cont +=1
    soma += num
    avg = soma / cont
    num = float(input("Digite uma nota: "))

if num != 0:
    print(f"A média dos números digitados foi: {avg:.2f}")
else:
    print("Nenhuma nota foi inserida. ")