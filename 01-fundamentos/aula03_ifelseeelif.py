nome_cliente = input("Digite o nome do cliente: ")
valor_orcamento = float(input("Digite o valor do orçamento: "))
if valor_orcamento <= 1000: 
    print(f"{nome_cliente} o orçamento é baixo.")
elif valor_orcamento >= 1001 and valor_orcamento <= 5000:
    print(f"{nome_cliente} o orçamento é médio.")
else:
    print(f"{nome_cliente} o orçamento é alto.")
