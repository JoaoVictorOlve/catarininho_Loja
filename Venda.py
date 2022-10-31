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
    temp={}
    if chave != False:
        quant=int(input("digite a quantidade vendida"))
        
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
                        else:
                            dif = eval(line)['quantidade'] -quant
                            
                            temp=eval(line)
                            
                            
                            temp['quantidade'] = dif
                            print(temp)
                            
                            lucro = dif*eval(line)['preco']
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")
        with open('produtos.txt', 'a') as arquivo:
            arquivo.write("\n"+str(temp))
    else:
        print("NAO ENCONTRADO")

nome=str(input("digite o nome do item vendido"))
venda(nome)
