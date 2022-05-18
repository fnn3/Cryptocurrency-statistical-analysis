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


datumi = []
for i in dateIOTA:
    datum_i_vrijeme=i.split(" ")
    datumi.append(datum_i_vrijeme[0])


x = np.arange(1245).reshape(-1, 1)

avADA = np.average(opADA)
avIOTA = np.average(opIOTA_n)
avETH = np.average(opETH_n)
avBTC = np.average(opBTC_n)

AdaN = []
for i in opADA:
    ada = i / avADA
    AdaN.append(ada)

IotaN = []
for i in opIOTA_n:
    iota = i / avIOTA
    IotaN.append(iota)

EthN = []
for i in opETH_n:
    eth = i / avETH
    EthN.append(eth)

BtcN = []
for i in opBTC_n:
    btc = i / avBTC
    BtcN.append(btc)

fig, ax = plt.subplots()
ax.plot(dateIOTA,AdaN,"r")
ax.plot(IotaN,"orange")
ax.plot(EthN,"g")
ax.plot(BtcN,"b")


ax.set_xticks([0,len(datumi)/4, len(datumi)/2, 3*len(datumi)/4, len(datumi)-1])
ax.set_xticklabels([datumi[0],datumi[int(len(datumi)/4)],datumi[int(len(datumi)/2)],datumi[3*int(len(datumi)/4)],datumi[len(datumi)-1]])

plt.title("Usporedno kretanje cijene u omjeru")
plt.legend(["ADA","ETH","BTC"])
plt.ylabel("USD")



plt.show()
