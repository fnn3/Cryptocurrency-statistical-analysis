import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import scipy.stats
import math
import statistics
from fitter import Fitter, get_common_distributions, get_distributions


dataBTC = pd.read_csv("Data/coin_Bitcoin.csv")
dataADA = pd.read_csv("Data/coin_Cardano.csv")
dataIOTA = pd.read_csv("Data/coin_Iota.csv")
dataETH = pd.read_csv("Data/coin_Ethereum.csv")

BTC = dataBTC.Open.to_numpy()
ETH = dataETH.Open.to_numpy()
IOTA = dataIOTA.Open.to_numpy()
ADA = dataADA.Open.to_numpy()

dateA = dataADA.Date.to_numpy()
dateB = dataBTC.Date.to_numpy()
dateE = dataETH.Date.to_numpy()
dateI = dataIOTA.Date.to_numpy()


#Računanje verižnih indeksa

# verizni ADA
#----------------------------------------------------------------------------------------------

num_bins=100

verADA = []

for index,i in enumerate(ADA):
    if index==0:
        rez=100
    else:
        rez = (ADA[index]/ADA[index-1])*100
    verADA.append(rez)

sdADA = np.std(verADA)
avADA = np.average(verADA)

print("prosjek verižnih indeksa=",avADA,"\nstandardna devijacija verižnih indeksa=",sdADA)

#histogram stvarnih frekvencija

n, bins, patches = plt.hist(verADA, num_bins)

# distribucija teorijskih frekvencija

hiADA = []

for index,i in enumerate(bins):
    if index == 0:
        rez = round(scipy.stats.norm(avADA, sdADA).cdf(i)* len(verADA))
    else:
        rez = round((scipy.stats.norm(avADA, sdADA).cdf(i) - scipy.stats.norm(avADA, sdADA).cdf(bins[index - 1])) * len(verADA))
    hiADA.append(rez)




verADA2 = []

for i in verADA :
    if i>(avADA-3*sdADA) and i<(avADA+3*sdADA):
        verADA2.append(i)



sdADA2 = np.std(verADA2)
avADA2 = np.average(verADA2)

print("Ulazni parametri nakon druge iteracije-ADA","\nprosjek verižnih indeksa=",avADA2,"\nstandardna devijacija verižnih indeksa=",sdADA2)


