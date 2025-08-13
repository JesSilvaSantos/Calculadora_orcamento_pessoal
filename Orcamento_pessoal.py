def calcular_orcamento(receita, despesas):
    saldo = receita - sum(despesas)
    return saldo

def main():
    receita = float(input("Digite sua receita mensal: R$ "))
    despesas = []

    while True:
        despesa = input("Digite uma despesa (ou 'fim' para terminar): ")
        if despesa.lower() == 'fim':
            break
        despesas.append(float(despesa))

    saldo = calcular_orcamento(receita, despesas)
    print(f"\nSeu saldo final é: R$ {saldo:.2f}")

if __name__ == "__main__":
    main()
