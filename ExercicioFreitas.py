import matplotlib.pyplot as plt
import numpy as np

receitas = np.array([100,120,105,85,90,98,150,140,130,112,108,95])
plt.plot(receitas,ls="--", color="red", marker="o",ms=6,label="Receitas")


despesas = np.array([90,100,86,110,100,97,150,100,88,99,107,150])
plt.plot(despesas,ls="--", color="blue", marker="o",ms=6,label="Despesas")


resultado = receitas - despesas 
plt.plot(resultado,ls="--", color="green", marker="o",ms=6,label="Resultado")


#plt.legend(loc="upper right") colocar a legenda no lugar desejado
plt.legend()


#importando arquivo CSV
data = np.genfromtxt("D:/Downloads/iris.data",delimiter=",",usecols=(0,1,2,3))
#print(data)

setTS = data[0:50,0]
print(setTS)

setLS = data[0:50,1]
print(setLS)

grafico = plt.figure()

grTS = grafico.add_subplot(1,2,1)
plt.plot(setTS,"r-o")

grLS = grafico.add_subplot(1,2,2)
plt.plot(setLS,"b-o")