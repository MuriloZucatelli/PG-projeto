# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:37:14 2022

@author: Murilo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter as SF
from matplotlib.ticker import MultipleLocator as ML
import seaborn as sns
import pandas as pd

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=18)  # fontsize of the axes title
plt.rc("axes", labelsize=14)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=13)  # fontsize of the tick labels
plt.rc("ytick", labelsize=13)  # fontsize of the tick labels
plt.rc("legend", fontsize=10)  # legend fontsize
plt.rc("font", size=13)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("husl", 7)


def P(d, stdev, dm):
    frac = 1 / (d*(stdev**2 * 2 * np.pi) ** 0.5)
    expnum = np.log(d/dm) ** 2 / (2 * stdev ** 2)
    dist = frac * np.exp(-expnum)
    return dist



# d = np.linspace(2, 120, 20)
n = 30
d_log = np.logspace(np.log(50), np.log(250), n,base=np.exp(1))
diam = 120
sigm = 0.23

f = 100*P(d_log, sigm, diam)

fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(d_log, f,'-o', color = cor[0])
ax.semilogx()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.tick_params(axis="x", which="both", direction="inout")
ax.xaxis.set_major_formatter(SF())
ax.xaxis.set_minor_formatter(SF())
ax.tick_params(axis ='x', which = 'minor', labelsize = 8, pad = 2,length = 4)
ax.tick_params(axis ='x', which = 'major', labelsize = 12, pad = 6, length = 7)

ax.yaxis.set_major_locator(ML(0.3))

ax.set(
    xlabel=r"Diâmetro das gotículas [$\mu m$]",
    ylabel=r"Fração mássica $Y_g$",
)
ax.grid()

#
#
#


P_int = P(d_log, sigm, diam)
fig, ax = plt.subplots(dpi=100, tight_layout=True)
sz = np.size(P_int)
x = d_log[0:sz-1]+0.5*np.diff(d_log)
x_centro = np.diff(d_log)
y = P_int[0:sz-1] + 0.5*np.diff(P_int)

integral = np.sum(x_centro*y)  #Deve retornar 1
soma = x_centro*y

ax.scatter(d_log[0:29],soma)

# Acumulado
for i in range(1,sz):
    P_int[i] = sum(soma[0:i])
    print()
    
plt.plot(x,y)
#
#
#

fig,ax = plt.subplots(tight_layout=True)
plt.plot(d_log,P_int,'-o', color = cor[0])

ax.semilogx()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.tick_params(axis="x", which="both", direction="inout")
ax.xaxis.set_major_formatter(SF())
ax.xaxis.set_minor_formatter(SF())
ax.tick_params(axis ='x', which = 'minor', labelsize = 8, pad = 2,length = 4)
ax.tick_params(axis ='x', which = 'major', labelsize = 12, pad = 6, length = 7)

ax.yaxis.set_major_locator(ML(0.1))

ax.set(
    xlabel=r"Diâmetro das gotículas [$\mu m$]",
    ylabel=r"Frequência acumulada [-]",
)
ax.grid()







# Distribuição discreta

P_int = P(d_log, sigm, diam)

d_discr = d_log[0:n-1]+0.5*np.diff(d_log)
d_discr = d_log

x_centro = np.diff(d_log,append=2*d_log[-1]-d_log[-2])
y_mean = P_int

integral = np.sum(x_centro*y_mean)  #Deve retornar 1
P_discrete = x_centro*P_int
# plt.scatter(d_discr,P_discrete,color=cor[1])

fig,ax = plt.subplots(tight_layout=True)
ax.hist(d_discr,bins=d_discr,weights=P_discrete,align='mid')
ax.semilogx()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.tick_params(axis="x", which="both", direction="inout")
ax.xaxis.set_major_formatter(SF())
ax.xaxis.set_minor_formatter(SF())
ax.tick_params(axis ='x', which = 'minor', labelsize = 8, pad = 2,length = 4)
ax.tick_params(axis ='x', which = 'major', labelsize = 12, pad = 6, length = 7)
ax.set(
    xlabel=r"Diâmetro das gotículas [$\mu m$]",
    ylabel=r"Fração mássica $Y_d$",
)



alpha_d = 0.05      # concentração fase dispersa 5%
rho = 850           # massa específica oleo
vazao = np.array([600, 1000]) # vazao fase primária L/h
vazao_total = rho*vazao/3.6e6   #kg/s

injecoes = pd.DataFrame(np.zeros([n,4]),columns = ["D","Y_g",f"Vazao {vazao[0]}",f"Vazao {vazao[1]}"])
injecoes["D"] = d_discr/1000      # diametro em mm
# injecoes["Y_g"] = P(d_log, sigm, diam)
injecoes["Y_g"] = P_discrete
injecoes[f"Vazao {vazao[0]}"] = (1/integral)*injecoes["Y_g"]*alpha_d*vazao_total[0]
injecoes[f"Vazao {vazao[1]}"] = (1/integral)*injecoes["Y_g"]*alpha_d*vazao_total[1]

100*np.sum(injecoes[f"Vazao {vazao[0]}"])/vazao_total[0]
100*np.sum(injecoes[f"Vazao {vazao[1]}"])/vazao_total[1]

# plt.scatter(1000*injecoes["D"],injecoes["Y_g"])



#
#
#

# rosin hammler
# d_log = np.logspace(np.log(4), np.log(150), 50,base=np.exp(1))
# diam = 40
# # n = np.flip(np.log(-np.log(P_int)))/np.log(d_log/diam)
# # n = np.where(n > 0, n, 0)
# # n = np.mean(n)
# Yd = 1 - np.exp(-(d_log/diam)**2.1)


# plt.plot(d_log,Yd)
# plt.semilogx()


# DETERMINANDO O PARCEL METODO

# Constant MASS
# Valores para cada diâmetro
# Para o scale flow rate by face area
t_dpm = 1e-4
faces_inlet = 1582
diametro_max_alvo = 0.25e-3 #mm
rho_got = 1000
max_m_parcel = rho_got*np.pi/6*diametro_max_alvo**3
const_mass_parcel = (injecoes["Vazao 600"]*t_dpm)/0.9215  #massa de parcel injetada por time-step
injecoes["Parcel Mass 600"] = np.where(const_mass_parcel<max_m_parcel,const_mass_parcel,max_m_parcel)

diametro_max_alvo = 0.25e-3 #mm
rho_got = 1000
max_m_parcel = rho_got*np.pi/6*diametro_max_alvo**3
const_mass_parcel = (injecoes["Vazao 1000"]*t_dpm)/0.9215
injecoes["Parcel Mass 1000"] = np.where(const_mass_parcel<max_m_parcel,const_mass_parcel,max_m_parcel)




# rho_got*np.pi/6*d**3    #M_particula
# rho_got*np.pi/6*d**3/(2.30392e-5/faces_inlet)










