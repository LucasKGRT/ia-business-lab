opcao = 1

while opcao != 4:

    print("\=============================")
    print("      BUSINESS ASSISTANT      ")
    print("\=============================")
    print("1 - Cadastrar cliente")
    print("2 - Consultar cliente")
    print("3 - Excluir cliente")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Cadastrar cliente em desenvolvimento...")
    elif opcao == 2:
        print("Consultar cliente em desenvolvimento...")
    elif opcao == 3:
        print("Excluir cliente em desenvolvimento...")
    elif opcao == 4:
        print("Saindo do sistema...")
    else:
        print("Opção inválida. Tente novamente.")