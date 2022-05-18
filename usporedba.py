import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from scipy import stats



dataBTC = pd.read_csv("Data/coin_Bitcoin.csv")
dataADA = pd.read_csv("Data/coin_Cardano.csv")
dataIOTA = pd.read_csv("Data/coin_Iota.csv")
dataETH = pd.read_csv("Data/coin_Ethereum.csv")

#izbacit naslove stupca tablice

#print(dataBTC.columns)


#stupac cijena otvaranja

opBTCdf = dataBTC.Open
clBTCdf = dataBTC.Close
opADAdf = dataADA.Open
clADAdf = dataADA.Close
opIOTAdf = dataIOTA.Open
clIOTAdf = dataIOTA.Close
opETHdf = dataETH.Open
clETHdf = dataETH.Close

dateBTC = dataBTC.Date
dateADA = dataADA.Date
dateIOTA = dataIOTA.Date.to_numpy()[110:]


opBTC = opBTCdf.to_numpy()
clBTC = clBTCdf.to_numpy()
opADA = opADAdf.to_numpy()
clADA = clADAdf.to_numpy()
opIOTA = opIOTAdf.to_numpy()
clIOTA = clIOTAdf.to_numpy()
opETH = opETHdf.to_numpy()
clETH = clETHdf.to_numpy()


opBTC_n = opBTC[1617:]
opIOTA_n = opIOTA[110:]
opETH_n = opETH[786:]

data= {'BTC': opBTC_n,
       'ETH': opETH_n,
        'IOTA': opIOTA_n,
        'ADA': opADA,
        }




df = pd.DataFrame(data,columns=['BTC','ETH','IOTA','ADA'])

corrMatrix = df.corr()
print (corrMatrix)







datumi = []
for i in dateIOTA:
    datum_i_vrijeme=i.split(" ")
    datumi.append(datum_i_vrijeme[0])

x = np.arange(1245).reshape(-1, 1)

reg1 = LinearRegression().fit(x, opADA)
reg2 = LinearRegression().fit(x, opIOTA_n)
reg3 = LinearRegression().fit(x, opBTC_n)
reg4 = LinearRegression().fit(x, opETH_n)


y1 = reg1.predict(x)
y2 = reg2.predict(x)
y3 = reg3.predict(x)
y4 = reg4.predict(x)

#print(x)
fig, ax = plt.subplots()
ax.plot(dateIOTA,opADA,"r")
ax.plot(opBTC_n,"b")
ax.plot(opIOTA_n,"orange")
ax.plot(opETH_n,"g")



ax.set_yscale('log')
ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(datumi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])

plt.title("Usporedni graf (Logaritamska skala)")
plt.legend(["ADA","BTC","IOTA","ETH"])
plt.ylabel("USD")

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.plot(y1,"r")
ax.plot(y2,"orange")
ax.plot(y3,"b")
ax.plot(y4,"g")
plt.legend(["ADA","IOTA","BTC","ETH"])
plt.title("Usporedni graf linearne regresije")

plt.show()
