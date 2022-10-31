def cadastroProduto(produto):                       #lista onde serão cadastrados os produtos

    with open('produtos.txt', 'a') as arquivo:       
        arquivo.write(str(produto)+"\n")            #Insere os produtos cadastrados dentro do arquivo txt


def procuraItem(nome):
    index=0
    flag=0
    arquivo = open("produtos.txt", "r")            #Le linha por linha no arquivo txt
    for line in arquivo:
        index +=1
        if nome == eval(line)['nome']:             #Procura o produto na lista  
            chave = index                   
            flag =1
    if flag == 0:
        arquivo.close()
        return 0                                   #Caso nao ache o produto ele retorna 0
    else:
        arquivo.close()
        return chave                               #Se achou o produto retorna a chave dele


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

def venda(nome):
    chave=procuraItem(nome)             # Utiliza a função para procurar o item
    temp={}
    if chave != False:
        quant=int(input("digite a quantidade vendida: "))
        
        try:
            with open('produtos.txt', 'r') as fr:               
                lines = fr.readlines()                      # Le linha por linha
                
                ptr = 1                                     # Ponteiro para posição
                
                with open('produtos.txt', 'w') as fw:       # Abrindo no modo de escrita
                    for line in lines:
                        
                        if ptr != chave:
                            fw.write(line)
                        else:
                            dif = eval(line)['quantidade'] -quant       # Subtrai a quantidade que foi vendida do item

                            temp=eval(line)
                            
                            
                            temp['quantidade'] = dif
                            
                            
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")           
        with open('produtos.txt', 'a') as fd:
            fd.write(str(temp)+'\n')                    # Escreve a diferença que foi vendida no arquivo txt
    else:
        print("NAO ENCONTRADO")

def relatorio():
    with open('produtos.txt','r') as arquivo:  
        for line in arquivo:
            dif = eval(line)['quantidadeInicial']-eval(line)['quantidade']              
            print("{} vendid@s: {}\n".format(eval(line)['nome'],dif))                   # Mostra a quantidade que foi vendida
            lucro=dif*eval(line)['preco']
            print("lucro na venda de {}: {}\n".format(eval(line)['nome'],lucro))        # Mostra o lucro bruto que foi obtido
