# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:23:54 2022

@author: Murilo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:53:30 2022

@author: Murilo
"""

import matplotlib as mpl
import matplotlib.ticker as tic
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os.path as path

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
pasta = (
    r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Codigos python e processamentos"
)

Re10 = pd.read_csv(path.join(pasta, "velo-for-yplusRe10.csv"))
Re13 = pd.read_csv(path.join(pasta, "velo-for-yplusRe13.csv"))
Re15 = pd.read_csv(path.join(pasta, "velo-for-yplusRe15.csv"))
Re18 = pd.read_csv(path.join(pasta, "velo-for-yplusRe18.csv"))
Re18liso = pd.read_csv(path.join(pasta, "velo-for-yplusRe18liso.csv"))

Re10["TKE"] = pd.read_csv(path.join(pasta, "tke-for-yplusRe10.csv"), usecols=["TKE"])
Re13["TKE"] = pd.read_csv(path.join(pasta, "tke-for-yplusRe13.csv"), usecols=["TKE"])
Re15["TKE"] = pd.read_csv(path.join(pasta, "tke-for-yplusRe15.csv"), usecols=["TKE"])
Re18["TKE"] = pd.read_csv(path.join(pasta, "tke-for-yplusRe18.csv"), usecols=["TKE"])

Y_wall = 10.75
Re10["Dw"] = Y_wall - Re10["Y"]
Re13["Dw"] = Y_wall - Re13["Y"]
Re15["Dw"] = Y_wall - Re15["Y"]
Re18["Dw"] = Y_wall - Re18["Y"]
Re18liso["Dw"] = Y_wall - Re18liso["Y"]

rho = 1000
mu = 0.001
tau10 = 1.256  # 1.275 #1.25
tau13 = 2.3682  # 2.4
tau15 = 3.204  # 3.25
tau18 = 4.7926  # 4.89
tau18liso = 3.68446  # 3.82

Cmu = 0.09
uast10 = (Re10["TKE"].iloc[-1] ** 0.5) * (Cmu ** (1 / 4))  # TKE = 3.68e-3
uast13 = (Re13["TKE"].iloc[-1] ** 0.5) * (Cmu ** (1 / 4))
uast15 = (Re15["TKE"].iloc[-1] ** 0.5) * (Cmu ** (1 / 4))
uast18 = (Re18["TKE"].iloc[-1] ** 0.5) * (Cmu ** (1 / 4))
uast18liso = (0.0115027 ** 0.5) * (Cmu ** (1 / 4))

Re10["Uast"] = Re10["Velo"] * uast10 / (tau10 / rho)
Re10["yast"] = rho * uast10 * (Re10["Dw"] / 1000) / mu

Re13["Uast"] = Re13["Velo"] * uast13 / (tau13 / rho)
Re13["yast"] = rho * uast13 * (Re13["Dw"] / 1000) / mu

Re15["Uast"] = Re15["Velo"] * uast15 / (tau15 / rho)
Re15["yast"] = rho * uast15 * (Re15["Dw"] / 1000) / mu

Re18["Uast"] = Re18["Velo"] * uast18 / (tau18 / rho)
Ks = 0.1e-3
Cs = 1
Ksplus_18 = rho * Ks * uast18 / mu
Re18["yast"] = rho * uast18 * (Re18["Dw"] / 1000) / mu

Re18liso["Uast"] = Re18liso["Velo"] * uast18liso / (tau18liso / rho)
Re18liso["yast"] = rho * uast18liso * (Re18liso["Dw"] / 1000) / mu

fig, ax = plt.subplots(dpi=100, tight_layout=True)

# ax.plot(Re10["Velo"],Re10["Y"],lw=1,alpha=0.9, ls='--', ms=5, label='Q = 0,34 [m$^3$/h]', marker= 's',mfc='none')
# ax.plot(Re13["Velo"],Re13["Y"],lw=1,alpha=0.9, ls=':', ms=5, label='Q = 0,455 [m$^3$/h]', marker= 'o',mfc='none')
# ax.plot(Re15["Velo"],Re15["Y"],lw=1,alpha=0.9, ls='-.', ms=5, label='Q = 0,523 [m$^3$/h]', marker= '*',mfc='none')
# ax.plot(Re18["Velo"],Re18["Y"],lw=1,alpha=0.9, ls='-', ms=5, label='Q = 0,629 [m$^3$/h]', marker= 'x',mfc='none')

# =============================================================================
# ax.plot(Re10["y+"],Re10["U/ut"],lw=1, ls='', ms=6, label='Q = 0,34 [m$^3$/h]', marker= 's',mfc='none',c=cor[0],markevery = 0.018)
# ax.plot(Re13["y+"],Re13["U/ut"],lw=1, ls='', ms=6, label='Q = 0,455 [m$^3$/h]', marker= 'o',mfc='none',c=cor[1], markevery = 0.018)
# ax.plot(Re15["y+"],Re15["U/ut"],lw=1, ls='', ms=6, label='Q = 0,523 [m$^3$/h]', marker= '*',mfc='none',c=cor[2],markevery = 0.018)
# ax.plot(Re18["y+"],Re18["U/ut"],lw=1, ls='', ms=6, label='Q = 0,629 [m$^3$/h]', marker= 'x',mfc='none',c=cor[3],markevery = 0.018)
# ax.plot(Re18liso["y+"],Re18liso["U/ut"],lw=1,alpha=0.9, ls='', ms=6, label=r'Q = 0,629 [m$^3$/h] $K_s = 0$',c=cor[4],marker= '^',mfc='none', markevery = 0.018)
# =============================================================================

ax.plot(
    Re10["yast"],
    Re10["Uast"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,340 [m$^3$/h]",
    marker="s",
    c=cor[0],
    markevery=0.018,
)
ax.plot(
    Re13["yast"],
    Re13["Uast"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    c=cor[1],
    markevery=0.018,
)
ax.plot(
    Re15["yast"],
    Re15["Uast"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    c=cor[2],
    markevery=0.018,
)
ax.plot(
    Re18["yast"],
    Re18["Uast"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    c=cor[3],
    markevery=0.018,
)
ax.plot(
    Re18liso["yast"],
    Re18liso["Uast"],
    lw=1,
    alpha=0.9,
    ls="",
    ms=6,
    label=r"Q = 0,629 [m$^3$/h] $K_s = 0$",
    c=cor[4],
    marker="^",
    markevery=0.018,
)

ax.set(xlim=[1, 110])
ax.semilogx()

ax.plot(
    np.linspace(0, 15, 30),
    np.linspace(0, 15, 30),
    lw=2,
    ls="--",
    label=r"$U^*=y^*$",
    c="k",
)
k = 0.4187  # von Kármán constant (= 0.4187)
E = 9.793  # empirical constant (= 9.793)
ax.plot(
    np.linspace(7, 90, 30),
    1 / k * np.log(E * np.linspace(7, 90, 30)),
    lw=2,
    ls="dotted",
    label=r"Lei Log parede lisa",
    c="darkblue",
)


ax.xaxis.set_ticks([1, 5, 11.225, 30, 100], labels=["1", "5", "11.225", "30", "100"])
ax.grid()
# ax.plot(Re18_malha6["Velocity Magnitude"],Re18_malha6["Position"])
# ax.plot(experimental['x'],experimental['Curve1'], label = r"Experimental Re ~ 11900 $\alpha$ = 0,8", ms =5, marker = '^',mfc='none')
ax.set(xlabel=r"$y^*$ [-]", ylabel=r"Velocidade adimensional $U^*$ [-]")

ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)


Ks = 0.1e-3
Cs = 1
Ksplus_18 = rho * Ks * uast18 / mu
Ksplus_10 = rho * Ks * uast10 / mu
DB = (
    1
    / k
    * np.log((Ksplus_18 - 2.25) / 87.75 + Cs * Ksplus_18)
    * np.sin(0.4258 * (np.log(Ksplus_18) - 0.811))
)

# ax.plot(np.linspace(10,90,30),1/k*np.log(E*np.linspace(10,90,30))-DB,lw=2,ls='dotted', label = r'Lei Log parede rugosa', c='darkblue')
ax.legend()
