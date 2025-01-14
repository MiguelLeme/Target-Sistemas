import json

with open('dados.json', 'r') as f:
    faturamento = json.load(f)

faturamento_valido = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_faturamento)

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
