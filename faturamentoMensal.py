import json


def main():
    with open('./dados.json') as file:
        dados = json.load(file)

    valores = [float(d['valor']) for d in dados]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(dados)
    quantidade = sum(v > media for v in valores)

    print(f"• O menor valor de faturamento ocorrido em um dia do mês: {menor}")
    print(f"• O maior valor de faturamento ocorrido em um dia do mês: {maior}")
    print(f"• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {quantidade}")


if __name__ == "__main__":
    main()