import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing


dataETH = pd.read_csv("Data/coin_Ethereum.csv")
dataADA = pd.read_csv("Data/coin_Cardano.csv")


#izbacit naslove stupca tablice

#print(dataBTC.columns)


#stupac cijena otvaranja


opETHdf = dataETH.Open
clETHdf = dataETH.Close



dateETH = dataETH.Date.to_numpy()


opETH = opETHdf.to_numpy()
clETH = clETHdf.to_numpy()


#print (dataBTC.head(),dataADA.head(),dataETH.head())
#print (dateETH)


#for index, i in enumerate (dateETH):
#    print(index, i)




datumi = []
for i in dateETH:
    datum_i_vrijeme=i.split(" ")
    datumi.append(datum_i_vrijeme[0])






x = np.arange(2031).reshape(-1, 1)

reg = LinearRegression().fit(x,opETH)

y = reg.predict(x)

cor = np.corrcoef(opETH,y)
print(cor)

fig, ax = plt.subplots()
ax.plot(dateETH,opETH,"r")
ax.plot(y)
ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(datumi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])

plt.title("Linearna regresija ETH cijene")
plt.legend(["ETH cijena","Linearna regresija"])
plt.ylabel("USD")
plt.show()
