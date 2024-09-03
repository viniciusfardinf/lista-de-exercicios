#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


def calcula_percentual_estados(faturamento_estados): 

  
  faturamento_total = sum(faturamento_estados.values()) # cálculo do faturamento total  
  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()} # calcula o percentual de cada estado

  return percentuais

# dados 
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula os percentuais
percentuais_estados = calcula_percentual_estados(faturamento)

# Imprime
for estado, percentual in percentuais_estados.items():
  print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")