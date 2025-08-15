import pandas as pd

entradas = []
saidas = []

print("\nOlá, que tal fazermos um panorama das suas entradas e saídas financeiras?")

ganhos = int(input("Quantas fontes de renda mensal você possui? "))

for i in range(ganhos):
    while True:
        try:
            fonte_renda = input(f"Qual é a fonte de renda {i + 1}? ")
            if fonte_renda == "":
                print("Preencha o nome da fonte de renda.")
                continue
            break
        except ValueError:
            print("Por favor, insira um nome válido.")

    valor_fonte = float(input(f"Qual é o valor da fonte {fonte_renda}?: "))
    entradas.append(valor_fonte)

contas = int(input("\nQuantas contas você possui nesse mês?"))

for i in range(contas):
    while True:
        try:
            conta_mes = input(f"Qual é o nome da conta {i + 1}: ")
            if conta_mes == "":
                print("Preencha o nome da conta.")
                continue
            break
        except ValueError:
            print("Por favor, insira um nome válido.")
    valor_conta = float(input(f"Qual é o valor da conta {conta_mes}: "))
    saidas.append(valor_conta)

total_entradas = sum(entradas)
total_saidas = sum(saidas)
situacao = total_entradas - total_saidas
if situacao > 500:
    print(f"\nVocê está com um bom saudo de {situacao:.2f} reais.")
elif situacao > 0 & situacao <= 500:
    print(f"\nVocê até que está no azul, com um saldo de {situacao:.2f}, mas cuide bem.")
else:
    print(f"\nVocê está no vermelho, com um saldo de {situacao:.2f} reais, comece a planejar melhor os seus gastos.")

print("\nResumo das suas finanças:")
print(f"\nTotal de entradas : {total_entradas:.2f} reais.")
print(f"\nTotal de saidas : {total_saidas:.2f} reais.")
print(f"\nSaldo final : {situacao:.2f} reais.")


