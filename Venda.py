def procuraItem(nome):
    index=0
    flag=0
    arquivo = open("produtos.txt", "r") 
    for line in arquivo:
        index +=1
        if nome == eval(line)['nome']:
            chave = index
            flag =1
    if flag == 0:
        arquivo.close()
        return 0
    else:
        arquivo.close()
        return chave
def venda(nome):
    chave=procuraItem(nome)
    if chave != False:
        quant=int(input("digite a quantidade vendida"))
        arquivo = open("produtos.txt", "w") 
        index=0
        try:
            with open('produtos.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
      
                # opening in writing mode
                with open('produtos.txt', 'w') as fw:
                    for line in lines:
                        
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        dif=eval(line)['quantidade']-quant
                        eval(line)['quantidade'] = dif
                        lucro=dif*eval(line)['preco']
                        line=dif
        except:
            print("Oops! someting error")
               
    else:
        print("NAO ENCONTRADO")

nome=str(input("digite o nome do item vendido"))
venda(nome)