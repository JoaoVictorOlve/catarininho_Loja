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

produto = input('Informe o produto: ')
apagarProduto(produto)