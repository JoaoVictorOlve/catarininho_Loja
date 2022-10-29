#nome, tipo, quantidade, preço
from controller import cadastroProduto

def menu():


    menu = 1
    while (menu!=0):
            print('='*30, 'CATARININHO MEGA STORE', '='*30)

            print('\n O que podemos fazer para você hoje?\n')

            menu = int(input('1. -> Cadastro de Produto\n2. -> Relatorio de Vendas\n3. -> Venda\n4. -> Exclussao de produto\n0. -> Sair\n>: '))

            match menu:
                case 1:

                    produto = {} 

                    produto['nome']=str(input("Digite o nome do produto: "))   
                    produto['tipo']=str(input("Digite o tipo do produto: "))
                    produto['preco']=str(input("Insira o preço do seu produto: "))
                    produto['quantidade']=str(input("Digite a quantidade de itens: "))

                    cadastroProduto(produto)
        


menu()