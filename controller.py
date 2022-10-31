def apagarProduto(findProduto):
        #Lista onde vão ser colocados os produtos dentro do arquivo
        #   V
        lista = []

        #Pega cada linha dentro do arquivo e joga dentro da lista
        #   V
        with open('produtos.txt', 'r') as arquivo:
            for numero, linha in enumerate(arquivo): #lê linha por linha o arquivo
                relatorio = eval(linha) #converte a linha do arquivo para dicionário
                lista.append(relatorio) #joga esse dicionário para dentro da lista

        #Deleta o produto dentro da lista
        #   V
        for x in range(0, len(lista)): #lê a lista de produtos indice por indice...
            if findProduto == lista[x]['nome']: #se o nome escrito do input for o mesmo do produto da lista, executa o comando

                del lista[x] #deleta o produto dentro da lista
                break #quebra o loop (evita o erro "index out of range")
        
        #Reescreve o arquivo com os produtos da lista
        #   V
        with open('produtos.txt', 'w') as arquivo: #Na hora de executar o comando, ele limpa o arquivo de texto para substituir os dados
            for x in range(0, len(lista)): #Lê a lista indice por indice
                arquivo.write(str(lista[x])+'\n') #Repõe os produtos da lista para dentro do arquivo de texto

def aumentarEstoque(findProduto):
    #Lista onde vão ser colocados os produtos dentro do arquivo
    #   V
    lista = []
    encontrado = False

    #Pega cada linha dentro do arquivo e joga dentro da lista
    #   V
    with open('produtos.txt', 'r') as arquivo: 
        for numero, linha in enumerate(arquivo): #lê linha por linha o arquivo
            relatorio = eval(linha) #converte a linha do arquivo para dicionário
            lista.append(relatorio) #joga esse dicionário para dentro da lista
    arquivo.close()
        
    #Altera a quantidade do produto dentro da lista e joga a lista de volta para o arquivo de texto
    #   V
    for x in range(0, len(lista)):
        if findProduto == lista[x]['nome']:
            encontrado = True
            print('='*85)
            print('|{:^20}|{:^20}|{:^20}|{:^20}'.format(' Nome', ' Tipo', ' Quantidade', ' Preço')) #Cabeçalho
            print('='*85)
            print('|{:^20}|{:^20}|{:^20}|{:^20}'.format(lista[x]['nome'],lista[x]['tipo'],lista[x]['quantidade'],lista[x]['preco']))
            print('='*85)
            while True:
                aumentar = int(input('Informe a quantidade que quer aumentar\n>'))
                lista[x]['quantidade'] = lista[x]['quantidade'] + aumentar
                    
                with open('produtos.txt', 'w') as arquivo:
                    for x in range(0, len(lista)):
                        arquivo.write(str(lista[x])+'\n')
                
                sair = input('Valor alterado!\nPressione enter para continuar')
                break
    if encontrado == False:
        sair = input('Produto não encontrado!\nPressione enter para continuar')


estoque = str(input('Informe o nome do produto que queira aumentar o estoque\n>'))
aumentarEstoque(estoque)