#vetor

estoque = []

escolha = -1

while escolha != 6:
    print("=== ESTOQUE DA CANTINA ===")
    print("1 - Adicionar produto")
    print("2 - Visualizar produtos disponiveis")
    print("3 - Ver quantidade de produtos")
    print("4 - Verificar se um produto está no estoque")
    print("5 - Remover produto")
    print("6 - Sair") 
 
    escolha = int(input("Informe a operação desejada (1 - 6): "))

    #inicio do match case
    match escolha:
        case 1:
            produto = (input("Informe o produto que deseja adicionar: "))
            if produto not in estoque:
                estoque.append(produto)
                print("Produto adicionado")
            else:
                print ("produto ja existe")
            
        case 2:
            if estoque:
                print("Estoque atual", estoque)
            else:
                print("Não há produtos cadastrados")
        
        case 3:
             print(f"Quantidade de itens cadastrados: {len(estoque)}")
        
        case 4:
            encontrou = False
            produto = (input(f"Informe o produto que deseja procurar: "))
            for item in estoque:
                if(item == produto):
                 encontrou = True

            if(encontrou == True):
                print("Produto cadastrado")
            else:
                print("Produto não cadastrado")
        
        case 5:
            remover = (input("Qual produto deseja remover do estoque? "))
            if remover in estoque:
                estoque.remove(remover)
                print("Produto removido")
            else:
                print("Produto não encontrado")
        
        case 6:
            print("Programa encerrado")
        case _:
            print("Opção inválida, tente novamente")
# fim do coigo
