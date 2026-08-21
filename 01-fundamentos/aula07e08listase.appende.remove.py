clientes = []
idades = []
contador = 1

while contador <= 3:  
    nome_cliente = input("Digite o nome do cliente:")
    idade_cliente = int(input("Digite a idade do cliente:"))

    clientes.append(nome_cliente)
    idades.append(idade_cliente)

    contador += 1

print("===== CLIENTES CADASTRADOS =====" )

for cliente, idade in zip(clientes, idades):
    print(f"Cliente: {cliente} - Idade: {idade}")
