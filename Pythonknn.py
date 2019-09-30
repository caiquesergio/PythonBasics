#kNN - K Nearest Neighbors

dados = []
classes = []
with open('C:/knnPython/haberman.data','r') as arq:
    for linha in arq.readlines():
        #print(linha)
        campos = linha.replace('\n', '').split(',')
        #print(campos)
        dados.append([int(campos[0]), 
                       int(campos[1]),
                       int(campos[2]),
                       int(campos[3])]) 
        classes.append(int(campos[3]))
        
        #print(dados)
        #print(classes)
        
porcTreina = 0.8
total = len(dados)
qtTreina = int(total * porcTreina)
qtTeste = total - qtTreina
print(total, qtTreina, qtTeste)
treina,teste = [],[]
qt = 0
for qt in range(total):
    if qt < qtTreina:
        treina.append(dados[qt])
    else:
        teste.append(dados[qt])
    qt += 1
    
print(len(dados), len(treina), len(teste))
        