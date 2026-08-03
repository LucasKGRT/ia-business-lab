nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = input("Digite a idade do cliente: ")
idade_cliente = int(idade_cliente)
if idade_cliente >= 18:
    print(f"{nome_cliente} é maior de idade.")
else:
    print(f"{nome_cliente} não é maior de idade.")
