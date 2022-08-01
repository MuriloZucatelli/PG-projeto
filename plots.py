# -*- coding: utf-8 -*-
"""
Created on Tue May 10 07:06:36 2022

@author: Murilo
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=18)  # fontsize of the axes title
plt.rc("axes", labelsize=14)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=13)  # fontsize of the tick labels
plt.rc("ytick", labelsize=13)  # fontsize of the tick labels
plt.rc("legend", fontsize=13)  # legend fontsize
plt.rc("font", size=13)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("husl", 8)

# plt.style.use("sea")


#'Solarize_Light2',
#'_classic_test_patch',
#'_mpl-gallery',
#'_mpl-gallery-nogrid',
#'bmh',
#'classic',
#'dark_background',
#'fast',
#'fivethirtyeight',
#'ggplot',
#'grayscale',
#'seaborn',
#'seaborn-bright',
#'seaborn-colorblind',
#'seaborn-dark',
#'seaborn-dark-palette',
#'seaborn-darkgrid',
#'seaborn-deep',
#'seaborn-muted',
#'seaborn-notebook',
#'seaborn-paper',
#'seaborn-pastel',
#'seaborn-poster',
#'seaborn-talk',
#'seaborn-ticks',
#'seaborn-white',
#'seaborn-whitegrid',
#'tableau-colorblind10'


## RESULTADOS DE VALIDACAO
mdot = np.array([0.340, 0.455, 0.523, 0.629])
Dp_exp = np.array([9241, 16872, 22541, 32393])
Dp_num = np.array([9029.4, 16462, 21972, 32205])

fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    mdot,
    Dp_exp,
    linewidth=2,
    linestyle="--",
    markersize=10,
    label="Experimental",
    marker="s",
    color=cor[0],
)
ax.plot(
    mdot,
    Dp_num,
    linewidth=2,
    linestyle="--",
    markersize=10,
    label="Numérico",
    marker="o",
    color=cor[3],
)
ax.set(xlabel=r"Vazão volumétrica [m$^3$/h]", ylabel=r"$\Delta$ P [Pa]")
ax.minorticks_on()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend()
