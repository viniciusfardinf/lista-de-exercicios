#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def analisa_faturamento(dados):    

  faturamento_diario = [dado['valor'] for dado in dados if dado['valor'] > 0]  # filtrando os dias que o valor foi maior que zero
  
  media_mensal = sum(faturamento_diario) / len(faturamento_diario) # calculando  a média do mês

  menor_valor = min(faturamento_diario) #localizando o menor valor
  maior_valor = max(faturamento_diario) # maior valor 
 
  dias_acima_media = sum(valor > media_mensal for valor in faturamento_diario) # dias que foram acima da média

  return menor_valor, maior_valor, dias_acima_media

 # carregando o json
with open('dados.json', 'r') as f:  
  dados = json.load(f)

menor, maior, dias_acima = analisa_faturamento(dados)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamento acima da média:", dias_acima)