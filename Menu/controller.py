def cadastroProduto(produto):

    with open('Menu/produtos.txt', 'a') as arquivo:
        arquivo.write(str(produto)+"\n")
