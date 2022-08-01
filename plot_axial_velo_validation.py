# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:47:30 2022

@author: Murilo
"""

# =============================================================================
# Codigo para processar linhas axiais na verificação
# =============================================================================

import numpy as np
import pandas as pd
import os.path as path
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=18)  # fontsize of the axes title
plt.rc("axes", labelsize=14)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=13)  # fontsize of the tick labels
plt.rc("ytick", labelsize=13)  # fontsize of the tick labels
plt.rc("legend", fontsize=9)  # legend fontsize
plt.rc("font", size=10)  # controls default text sizes
cor = sns.color_palette("husl", 7)
pasta = (
    r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Codigos python e processamentos"
)
Re10 = pd.read_csv(path.join(pasta, "velo-axial-anular-validacaoRe10.csv"))
Re13 = pd.read_csv(path.join(pasta, "velo-axial-anular-validacaoRe13.csv"))
Re15 = pd.read_csv(path.join(pasta, "velo-axial-anular-validacaoRe15.csv"))
Re18 = pd.read_csv(path.join(pasta, "velo-axial-anular-validacaoRe18.csv"))

Re10["Z"] = Re10["Z"] - Re10["Z"].iloc[0]
Re13["Z"] = Re13["Z"] - Re13["Z"].iloc[0]
Re15["Z"] = Re15["Z"] - Re15["Z"].iloc[0]
Re18["Z"] = Re18["Z"] - Re18["Z"].iloc[0]

dz = 520.38
fig, ax = plt.subplots(dpi=100, tight_layout=True)
me = 0.02
ax.plot(
    Re10["Z"],
    Re10["VRe10"],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Q = 0,340 [m$^3$/h]",
    marker="s",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re13["Z"],
    Re13["VRe13"],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re15["Z"],
    Re15["VRe15"],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re18["Z"],
    Re18["VRe18"],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    mfc="none",
    markevery=me,
)


ax.set(
    ylabel=r"Magnitude de velocidade V [m/s]", xlabel=r"Posição axial Z [mm]",
)
# ax.set_xlim = [0,1]
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(
    loc="upper center", fancybox=True, shadow=True, ncol=4, bbox_to_anchor=(0.5, 1.15)
)


#
#
#


Re10 = pd.read_csv(path.join(pasta, "velo-axial-coluna-validacaoRe10.csv"))
Re13 = pd.read_csv(path.join(pasta, "velo-axial-coluna-validacaoRe13.csv"))
Re15 = pd.read_csv(path.join(pasta, "velo-axial-coluna-validacaoRe15.csv"))
Re18 = pd.read_csv(path.join(pasta, "velo-axial-coluna-validacaoRe18.csv"))

Re10["Z"] = Re10["Z"] + dz
Re13["Z"] = Re13["Z"] + dz
Re15["Z"] = Re15["Z"] + dz
Re18["Z"] = Re18["Z"] + dz


fig, ax = plt.subplots(dpi=100, tight_layout=True)
me = 0.02
ax.plot(
    Re10["Z"],
    Re10["VRe10"],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Q = 0,340 [m$^3$/h]",
    marker="s",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re13["Z"],
    Re13["VRe13"],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re15["Z"],
    Re15["VRe15"],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re18["Z"],
    Re18["VRe18"],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    mfc="none",
    markevery=me,
)


ax.set(
    ylabel=r"Magnitude de velocidade V [m/s]", xlabel=r"Posição axial Z [mm]",
)
# ax.set_xlim = [0,1]
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(
    loc="upper center", fancybox=True, shadow=True, ncol=4, bbox_to_anchor=(0.5, 1.15)
)

#
#
#

Re10 = pd.read_csv(path.join(pasta, "velo-axial-anular_pos-validacaoRe10.csv"))
Re13 = pd.read_csv(path.join(pasta, "velo-axial-anular_pos-validacaoRe13.csv"))
Re15 = pd.read_csv(path.join(pasta, "velo-axial-anular_pos-validacaoRe15.csv"))
Re18 = pd.read_csv(path.join(pasta, "velo-axial-anular_pos-validacaoRe18.csv"))

Re10["Z"] = Re10["Z"] + dz
Re13["Z"] = Re13["Z"] + dz
Re15["Z"] = Re15["Z"] + dz
Re18["Z"] = Re18["Z"] + dz


fig, ax = plt.subplots(dpi=100, tight_layout=True)
me = 0.02
ax.plot(
    Re10["Z"],
    Re10["VRe10"],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Q = 0,340 [m$^3$/h]",
    marker="s",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re13["Z"],
    Re13["VRe13"],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re15["Z"],
    Re15["VRe15"],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    mfc="none",
    markevery=me,
)
ax.plot(
    Re18["Z"],
    Re18["VRe18"],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    mfc="none",
    markevery=me,
)


ax.set(
    ylabel=r"Magnitude de velocidade V [m/s]", xlabel=r"Posição axial Z [mm]",
)
# ax.set_xlim = [0,1]
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(
    loc="upper center", fancybox=True, shadow=True, ncol=4, bbox_to_anchor=(0.5, 1.2)
)
# ax.set_aspect(200)
