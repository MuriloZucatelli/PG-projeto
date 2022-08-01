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

Y_wall = 10.75
pasta = (
    r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Codigos python e processamentos"
)
Re10 = pd.read_csv(path.join(pasta, "velo-for-yplusRe10.csv"))
Re10["Dw"] = Y_wall - Re10["Y"]
Re13 = pd.read_csv(path.join(pasta, "velo-for-yplusRe13.csv"))
Re13["Dw"] = Re13["Y"].iloc[-1] - Re13["Y"]
Re15 = pd.read_csv(path.join(pasta, "velo-for-yplusRe15.csv"))
Re15["Dw"] = Re15["Y"].iloc[-1] - Re15["Y"]
Re18 = pd.read_csv(path.join(pasta, "velo-for-yplusRe18.csv"))
Re18["Dw"] = Re18["Y"].iloc[-1] - Re18["Y"]
Re18liso = pd.read_csv(path.join(pasta, "velo-for-yplusRe18liso.csv"))
Re18liso["Dw"] = Re18liso["Y"].iloc[-1] - Re18liso["Y"]

rho = 1000
mu = 0.001
tau10 = 1.256  # 1.275
tau13 = 2.3682  # 2.4
tau15 = 3.204  # 3.25
tau18 = 4.7926  # 4.89
tau18liso = 3.68446  # 3.82

ut_10 = np.sqrt(tau10 / rho)
ut_13 = np.sqrt(tau13 / rho)
ut_15 = np.sqrt(tau15 / rho)
ut_18 = np.sqrt(tau18 / rho)
ut_18liso = np.sqrt(tau18liso / rho)

Re10["U/ut"] = Re10["Velo"] / ut_10
Re10["y+"] = rho * ut_10 * (Re10["Dw"] / 1000) / mu

Re13["U/ut"] = Re13["Velo"] / ut_13
Re13["y+"] = rho * ut_13 * (Re13["Dw"] / 1000) / mu

Re15["U/ut"] = Re15["Velo"] / ut_15
Re15["y+"] = rho * ut_15 * (Re15["Dw"] / 1000) / mu

Re18["U/ut"] = Re18["Velo"] / ut_18
Re18["y+"] = rho * ut_18 * (Re18["Dw"] / 1000) / mu

Re18liso["U/ut"] = Re18liso["Velo"] / ut_18liso
Re18liso["y+"] = rho * ut_18liso * (Re18liso["Dw"] / 1000) / mu

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
    Re10["y+"],
    Re10["U/ut"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,340 [m$^3$/h]",
    marker="s",
    c=cor[0],
    markevery=0.018,
)
ax.plot(
    Re13["y+"],
    Re13["U/ut"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    c=cor[1],
    markevery=0.018,
)
ax.plot(
    Re15["y+"],
    Re15["U/ut"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    c=cor[2],
    markevery=0.018,
)
ax.plot(
    Re18["y+"],
    Re18["U/ut"],
    lw=1,
    ls="",
    ms=6,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    c=cor[3],
    markevery=0.018,
)
ax.plot(
    Re18liso["y+"],
    Re18liso["U/ut"],
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
    label=r"$U^+=y^+$",
    c="k",
)
k = 0.41
C = 5.51
ax.plot(
    np.linspace(7, 90, 30),
    1 / k * np.log(np.linspace(7, 90, 30)) + C,
    lw=2,
    ls="dotted",
    label=r"Lei Log parede lisa",
    c="darkblue",
)

ax.xaxis.set_ticks([1, 5, 11.25, 30, 100], labels=["1", "5", "11.25", "30", "100"])
ax.grid()
# ax.plot(Re18_malha6["Velocity Magnitude"],Re18_malha6["Position"])
# ax.plot(experimental['x'],experimental['Curve1'], label = r"Experimental Re ~ 11900 $\alpha$ = 0,8", ms =5, marker = '^',mfc='none')
ax.set(xlabel=r"$y^+$", ylabel=r"$U^+$ = U/u$_\tau$ [-]")

ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)

ax.legend()


Ks = 0.1e-3
Cmu = 0.09
k_nearwall = 1.514e-2
u_ast = (k_nearwall ** 0.5) * (Cmu ** (1 / 4))
Ksplus = rho * Ks * u_ast / mu
Cs = 1

DB = (
    1
    / k
    * np.log((Ksplus - 2.25) / 87.75 + Cs * Ksplus)
    * np.sin(0.4258 * (np.log(Ksplus) - 0.811))
)
