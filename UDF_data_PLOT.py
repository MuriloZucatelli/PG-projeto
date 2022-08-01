# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:49:40 2022

@author: Murilo
"""


# PACOTES
from os import listdir, path
import pandas as pd
import re
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import ScalarFormatter as SF
from matplotlib.ticker import MultipleLocator as ML
from sys import platform

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=12)  # fontsize of the axes title
plt.rc("axes", labelsize=11)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=10)  # fontsize of the tick labels
plt.rc("ytick", labelsize=10)  # fontsize of the tick labels
plt.rc("legend", fontsize=6.5)  # legend fontsize
plt.rc("font", size=11)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("deep", 11) 







entrada = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 4 DPM e UDF\Dados"
names = ['Anular externo',
         'Anular fim',
         'Anular interno',
         'Coluna fundo',
         'Coluna',
         'Slot faces laterais',
         'Slot circular externo',
         'Slot circular interno',
         'Trim entrada',
         'Slot2coluna',
         'Trim2slot',
         't']
f = open(path.join(entrada, 'Caso 5',"media-da-taxa-de-adesao-rfile.out"), mode="r")
ta_caso5 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ta_caso5.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 6',"taxa-media-de-adesao-rfile.out"), mode="r")
ta_caso6 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ta_caso6.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 7',"taxa-media-de-adesao-rfile.out"), mode="r")
ta_caso7 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ta_caso7.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 8',"taxa-media-de-adesao-rfile.out"), mode="r")
ta_caso8 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ta_caso8.drop(columns='t')).plot()

#constrained_layout=True
marc = ['.',',','o','v','p','d','x','+','*','s','h']
fig,ax = plt.subplots(2,2, sharex=True)
for i,col in zip(range(0,11),names[0:-1]):
    ax[0][0].plot(ta_caso5['t']-ta_caso5['t'].min(), ta_caso5[col],
                  marker = marc[i], markevery = 0.15,
                  color = cor[i])
    

for i,col in zip(range(0,11),names[0:-1]):
    ax[0][1].plot(ta_caso6['t']-ta_caso6['t'].min(), ta_caso6[col],
                  marker = marc[i], markevery = 0.15,
                  color = cor[i])

for i,col in zip(range(0,11),names[0:-1]):
    ax[1][0].plot(ta_caso7['t']-ta_caso7['t'].min(), ta_caso7[col],
                  marker = marc[i], markevery = 0.15,
                  color = cor[i])

for i,col in zip(range(0,11),names[0:-1]):
    ax[1][1].plot(ta_caso8['t']-ta_caso8['t'].min(), ta_caso8[col],
                  marker = marc[i], markevery = 0.15,
                  color = cor[i])


ax[0][0].set_title('(a)')
ax[0][1].set_title('(b)')
ax[1][0].set_title('(c)')
ax[1][1].set_title('(d)')

ax[0][0].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[0][0].tick_params(axis="x", which="both", direction="inout")
ax[0][1].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[0][1].tick_params(axis="x", which="both", direction="inout")
ax[1][0].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[1][0].tick_params(axis="x", which="both", direction="inout")
ax[1][1].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[1][1].tick_params(axis="x", which="both", direction="inout")

fig.supylabel(r'Taxa de adesão [g/s]')
fig.supxlabel(r't [s]')
fig.legend(names[0:-1],
    loc="upper center", fancybox=False, shadow=True, ncol=6, bbox_to_anchor=(0.5, 1.005),framealpha=0.9)
plt.show()


# top=0.88,
# bottom=0.1,
# left=0.09,
# right=0.95,
# hspace=0.2,
# wspace=0.15





"Gráficos 2"
names = ['adesao media',
         't']

f = open(path.join(entrada, 'Caso 5',"taxa-media-de-adesao-total-rfile.out"), mode="r")
tat_caso5 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(tat_caso5.drop(columns='t')).plot()
tat_caso5['adesao media'] = 1000*tat_caso5['adesao media']/0.005

f = open(path.join(entrada, 'Caso 6',"taxa-media-de-adesao-total-rfile.out"), mode="r")
tat_caso6 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(tat_caso6.drop(columns='t')).plot()
tat_caso6['adesao media'] = 1000*tat_caso6['adesao media']/0.005

f = open(path.join(entrada, 'Caso 7',"taxa-media-de-adesao-total-rfile.out"), mode="r")
tat_caso7 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(tat_caso7.drop(columns='t')).plot()
tat_caso7['adesao media'] = 1000*tat_caso7['adesao media']/0.005

f = open(path.join(entrada, 'Caso 8',"taxa-media-de-adesao-total-rfile.out"), mode="r")
tat_caso8 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(tat_caso8.drop(columns='t')).plot()
tat_caso8['adesao media'] = 1000*tat_caso8['adesao media']/0.005


"GRAFICO 1"
def tat_0():
    return np.array([5.4877049e-05, #caso 1
                     0.00019057345, #caso 2
                     5.6306014e-05, #caso 3
                     0.0002081372, #caso 4
                     tat_caso5['adesao media'].tail(1),
                     tat_caso6['adesao media'].tail(1),
                     tat_caso7['adesao media'].tail(1),
                     tat_caso8['adesao media'].tail(1)])
# def tat_0():
#     return np.array([5.4877049e-05, #caso 1
#                      0.00019057345, #caso 2
#                      5.6306014e-05, #caso 3
#                      0.0002081372, #caso 4
#                      2.4595172e-05,
#                      0.0001282724,
#                      3.509525e-05,
#                      0.00015081901])

plt.rc("legend", fontsize=7)  # legend fontsize
def names():
    return [r'Caso 1, Q = 600 L/h, $\mu$=5 cP',
            r'Caso 2, Q=1000 L/h, $\mu$=5 cP',
            r'Caso 3, Q = 600 L/h, $\mu$=7 cP',
            r'Caso 4, Q=1000 L/h, $\mu$=7 cP',
            r'Caso 5, Q = 600 L/h, $\mu$=5 cP',
            r'Caso 6, Q=1000 L/h, $\mu$=5 cP',
            r'Caso 7, Q = 600 L/h, $\mu$=7 cP',
            r'Caso 8, Q=1000 L/h, $\mu$=7 cP']
    
# Re = np.array([5153.59, 8589.31, 3681.13, 6135.22])
# 
# mu = np.array([0.005,0.005,0.007,0.007])
# X = Q*mu
# Re, tat_c = zip(*sorted(zip(Re, tat_0())))
# plt.plot(Re,tat_c)
# plt.figure()
# X, tat_c  = zip(*sorted(zip(X, tat_0())))

# tdr = np.array([12.395431,58.73251,12.582794,57.86338])        #Medio no volume

"Mais indicado:"
ws = np.array([301.08372,
               551.55939,
               357.79758,
               583.34967,
               199.67,
               521.65373,
               208.5284,
               547.83449])    #Max wall shear na parede

ws = np.array([57.84919, #65.044647
               84.964035, #14.374611
               42.178776, #83.373192
               107.06046, #102.76
               26.432726, #5.0670857
               47.574211, #11.033544
               28.975037, #5.7298336
               62.922264]) #12    #Max wall shear no anular


# ws, tat_c, names  = zip(*sorted(zip(ws, tat_0(), names())))

fig, ax = plt.subplots(dpi=100,constrained_layout=True,figsize=(6, 5))
marc = ['P',',','o','v','p','d','x','+','*','s','h']
for i,it in zip(range(0,8),range(0,8)):
    ax.scatter(ws[i],tat_0()[i], marker = marc[i],s=50)
    
    
# d30  = ws[0:4]
# d120 = ws[4:]    
ws30, tat_30 = zip(*sorted(zip(ws[0:4], tat_0()[0:4])))
ws120, tat_120 = zip(*sorted(zip(ws[4:],  tat_0()[4:])))
plt.plot(ws30,tat_30,'-.',label=r'D50 = 30 $\mu$m',lw=1.2,alpha=0.5)
plt.plot(ws120, tat_120,'--',label=r'D50 = 120 $\mu$m',lw=1.2,alpha=0.5)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(names() + [r'D50=30 $\mu$m',r'D50=120 $\mu$m'],
          loc="center left", fancybox=True, shadow=False,bbox_to_anchor=(0.02, 0.77),framealpha=0.6)
ax.set_xlim([10,115])
ax.set(ylabel=r"Taxa de adesão [g/s] ", xlabel=r"$\tau_w$ [Pa]")




# tdr, tat_c  = zip(*sorted(zip(tdr, tat_0())))
# plt.plot(tdr,tat_c)

# tdr_max = np.array([3269.0262,15531.882,2940.0324,14399.164])
# tdr_max, tat_c  = zip(*sorted(zip(tdr_max, tat_0())))
# plt.plot(tdr_max,tat_c)




"Gráfico 2"
plt.rc("axes", titlesize=12)  # fontsize of the axes title
plt.rc("axes", labelsize=13)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=11)  # fontsize of the tick labels
plt.rc("ytick", labelsize=11)  # fontsize of the tick labels
plt.rc("legend", fontsize=8)  # legend fontsize
plt.rc("font", size=11)  # controls default text sizes
def names2():
    return [r'Caso 1, $\mu$=5 cP, D50 = 30 $\mu$m',
            r'Caso 2, $\mu$=5 cP, D50 = 30 $\mu$m',
            r'Caso 3, $\mu$=7 cP, D50 = 30 $\mu$m',
            r'Caso 4, $\mu$=7 cP, D50 = 30 $\mu$m',
            r'Caso 5, $\mu$=5 cP, D50 = 120 $\mu$m',
            r'Caso 6, $\mu$=5 cP, D50 = 120 $\mu$m',
            r'Caso 7, $\mu$=7 cP, D50 = 120 $\mu$m',
            r'Caso 8, $\mu$=7 cP, D50 = 120 $\mu$m']
cor = sns.color_palette("deep", 8) 
Q = np.array([600,1000,600,1000,600,1000,600,1000])
# Q, tat_c, nome  = zip(*sorted(zip(Q, tat_0(), names())))

fig, ax = plt.subplots(dpi=100,constrained_layout=True,figsize=(5, 4))
for i,it in zip(range(0,8),range(0,8)):
    ax.scatter(Q[i],tat_0()[i], marker = marc[i],color = cor[i])
    
# ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(names2(), loc="center left", fancybox=True, shadow=False,bbox_to_anchor=(0.08, 0.75),framealpha=0.6)
ax.set_xticks([600,1000])
ax.set(ylabel=r"Taxa de adesão [g/s] ", xlabel=r"Vazão fase primária [L/h]")














"Gráfico 3: IGNORA"
plt.rc("axes", titlesize=12)  # fontsize of the axes title
plt.rc("axes", labelsize=13)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=11)  # fontsize of the tick labels
plt.rc("ytick", labelsize=11)  # fontsize of the tick labels
plt.rc("legend", fontsize=8)  # legend fontsize
plt.rc("font", size=11)  # controls default text sizes
def names3():
    return [r'Caso 1, Q= 600 L/h, D50 = 30 $\mu$m',
            r'Caso 2, Q=1000 L/h, D50 = 30 $\mu$m',
            r'Caso 3, Q= 600 L/h, D50 = 30 $\mu$m',
            r'Caso 4, Q=1000 L/h, D50 = 30 $\mu$m',
            r'Caso 5, Q= 600 L/h, D50 = 120 $\mu$m',
            r'Caso 6, Q=1000 L/h, D50 = 120 $\mu$m',
            r'Caso 7, Q= 600 L/h, D50 = 120 $\mu$m',
            r'Caso 8, Q=1000 L/h, D50 = 120 $\mu$m']

cor = sns.color_palette("deep", 8) 
mu = np.array([5,5,7,7,5,5,7,7])
# Q, tat_c, nome  = zip(*sorted(zip(Q, tat_0(), names())))

fig, ax = plt.subplots(dpi=100,constrained_layout=True,figsize=(5, 4))
for i,it in zip(range(0,8),range(0,8)):
    ax.scatter(mu[i],tat_0()[i], marker = marc[i],color = cor[i])
    
# ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(names3(), loc="center left", fancybox=True, shadow=False,bbox_to_anchor=(0.08, 0.75),framealpha=0.6)
# ax.set_xticks([600,1000])
ax.set(ylabel=r"Taxa de adesão [g/s] ", xlabel=r"Viscosidade da fase primária, $\mu$ [cP]")
























"Gráficos 3"
names = ['Anular externo',
         'Anular fim',
         'Anular interno',
         'Coluna fundo',
         'Coluna',
         'Slot faces laterais',
         'Slot circular externo',
         'Slot circular interno',
         'Trim entrada',
         'Slot2coluna',
         'Trim2slot',
         't']
f = open(path.join(entrada, 'Caso 5',"massa-aderida-rfile.out"), mode="r")
ma_caso5 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ma_caso5.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 6',"massa-aderida-rfile.out"), mode="r")
ma_caso6 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ma_caso6.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 7',"massa-aderida-rfile.out"), mode="r")
ma_caso7 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ma_caso7.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 8',"massa-aderida-rfile.out"), mode="r")
ma_caso8 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,13), engine='python')
(ma_caso8.drop(columns='t')).plot()





"Gráficos 4"
names = ['massa aderida',
         't']

f = open(path.join(entrada, 'Caso 5',"massa-aderida-total-rfile.out"), mode="r")
mat_caso5 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(mat_caso5.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 6',"massa-aderida-total-rfile.out"), mode="r")
mat_caso6 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(mat_caso6.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 7',"massa-aderida-total-rfile.out"), mode="r")
mat_caso7 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(mat_caso7.drop(columns='t')).plot()

f = open(path.join(entrada, 'Caso 8',"massa-aderida-total-rfile.out"), mode="r")
mat_caso8 = pd.read_csv(f, delim_whitespace=True,skiprows=3,names=names,usecols=range(1,3), engine='python')
(mat_caso8.drop(columns='t')).plot()



