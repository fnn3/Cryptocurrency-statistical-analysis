import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing


dataBTC = pd.read_csv("Data/coin_Bitcoin.csv")
dataADA = pd.read_csv("Data/coin_Cardano.csv")
dataIOTA = pd.read_csv("Data/coin_Iota.csv")

#izbacit naslove stupca tablice

#print(dataBTC.columns)


#stupac cijena otvaranja

opBTCdf = dataBTC.Open
clBTCdf = dataBTC.Close
opADAdf = dataADA.Open
clADAdf = dataADA.Close
opIOTAdf = dataIOTA.Open
clIOTAdf = dataIOTA.Close


dateBTC = dataBTC.Date
dateADA = dataADA.Date
date1 = dataIOTA.Date.to_numpy()[110:]


opBTC = opBTCdf.to_numpy()
clBTC = clBTCdf.to_numpy()
opADA = opADAdf.to_numpy()
clADA = clADAdf.to_numpy()
opIOTA = opIOTAdf.to_numpy()
clIOTA = clIOTAdf.to_numpy()

#print (dataBTC.head(),dataADA.head(),dataIOTA.head())
#print (date1)


#for index, i in enumerate (date1):
#    print(index, i)

opBTC_n = opBTC[1617:]
opIOTA_n = opIOTA[110:]

datumi = []
for i in date1:
    datum_i_vrijeme=i.split(" ")
    datumi.append(datum_i_vrijeme[0])

#print(datumi)


#print(len(opBTC_n),len(opIOTA_n),len(opADA))

x = np.arange(1245).reshape(-1, 1)

reg = LinearRegression().fit(x, opADA)

y = reg.predict(x)

cor = np.corrcoef(opADA,y)
print(cor)

fig, ax = plt.subplots()
ax.plot(date1,opADA,"r")
ax.plot(y)
ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(datumi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])

plt.title("Linearna regresija ADA cijene")
plt.legend(["ADA open cijena","Linearna regresija"])
plt.ylabel("USD")
plt.show()
