nome_cliente = input("Digite o nome do cliente: ")
telefone_cliente = input("Digite o telefone do cliente: ")
email_cliente = input("Digite o email do cliente: ")

if telefone_cliente != "" or email_cliente != "":
    print(f"{nome_cliente} seu cadastro foi aprovado.")
else:
    print(f"{nome_cliente} seu cadastro não foi aprovado.")