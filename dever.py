#questão 1
print("\n--/ Quem é maior? /--\n")
valor=[]
save=[]
valor.append(float(input("Diga um número: ")))
valor.append(float(input("Diga outro: ")))
if (valor[0]>valor[1]):
    print(f'O maior é {valor[0]} e o menor é {valor[1]}')
elif(valor[0]<valor[1]):
    print(f'O maior é {valor[1]} e o menor é {valor[0]}')
else:
    print(f"O número {valor[0]} e o número {valor[1]} são iguais")
print(valor)
save.append(valor.copy())
print(save)
valor.clear()
#questão 2
print("\n--/ Par ou Ímpar? /--\n")
valor.append(int(input("Diga um número inteiro: ")))
if(valor[0]%2==0):
    print(f"{valor[0]} é par")
else:
    print(f"{valor[0]} é ímpar")
save.append(valor.copy())
valor.clear()
#questão 3
print("\n-- / Calculo de Peso Ideal /--\n")
valor.append(float(input("Diga sua altura: ")))
valor.append(input("(M/F)Diga seu sexo: "))
if(valor[1].upper()=='M'):
    valor.append((72.7*valor[0])-58)
elif(valor[1].upper()=='F'):
    valor.append((62.1*valor[0])-58)
print(f"Seu peso ideal é {valor[2]}")
save.append(valor.copy())
valor.clear()
#questão 4
print("\n--/ Bhaskara (sei la pra que) /--\n")
valor.append(float(input("Diga o coeficiente (a): ")))
valor.append(float(input("Diga o coeficiente (b): ")))
valor.append(float(input("Diga o coeficiente (c): ")))
valor.append((valor[1]**2)-4*valor[0]*valor[2])
if(valor[3]>0):
    valor.append((-valor[1]+valor[3]**(1/2))/2*valor[0])
    valor.append((-valor[1]-valor[3]**(1/2))/2*valor[0])
    print(f"As raízes são {valor[4]} e {valor[5]}")
elif(valor[3==0]):
    valor.append((-valor[1]+valor[3]**(1/2))/2*valor[0])
    print(f"A raiz é {valor[4]}")
else:
    print("Nenhuma raís real")
save.append(valor.copy())
valor.clear()

print("\n--/ Todos os valores do exercício /--\n")

atual=1
for i in save:
    print(f"Questão {atual}:\n{i}")
    atual+=1