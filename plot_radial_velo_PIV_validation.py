# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:12:02 2022

@author: Murilo
"""

import matplotlib as mpl
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
plt.rc("legend", fontsize=12)  # legend fontsize
plt.rc("font", size=13)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("husl", 8)

pasta = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Figuras\Validacao PIV\Outros autores"

a = open(path.join(pasta, "PIV no anular Re11900.csv"), mode="r")
experimental = pd.read_csv(a, decimal=",")

# plt.scatter(experimental)
# experimental.plot()

Re10 = pd.read_csv(path.join(pasta, "Re10000.csv"))
Re10["Velocity [ m s^-1 ]"] = (
    Re10["Velocity [ m s^-1 ]"] / Re10["Velocity [ m s^-1 ]"].max()
)
Re10["Y [ mm ]"] = (Re10["Y [ mm ]"] - Re10["Y [ mm ]"].iloc[0]) / (
    Re10["Y [ mm ]"].iloc[-1] - Re10["Y [ mm ]"].iloc[0]
)

Re13 = pd.read_csv(path.join(pasta, "Re13000.csv"))
Re13["Velocity [ m s^-1 ]"] = (
    Re13["Velocity [ m s^-1 ]"] / Re13["Velocity [ m s^-1 ]"].max()
)
Re13["Y [ mm ]"] = (Re13["Y [ mm ]"] - Re13["Y [ mm ]"].iloc[0]) / (
    Re13["Y [ mm ]"].iloc[-1] - Re13["Y [ mm ]"].iloc[0]
)

Re15 = pd.read_csv(path.join(pasta, "Re15000.csv"))
Re15["Velocity [ m s^-1 ]"] = (
    Re15["Velocity [ m s^-1 ]"] / Re15["Velocity [ m s^-1 ]"].max()
)
Re15["Y [ mm ]"] = (Re15["Y [ mm ]"] - Re15["Y [ mm ]"].iloc[0]) / (
    Re15["Y [ mm ]"].iloc[-1] - Re15["Y [ mm ]"].iloc[0]
)

Re18 = pd.read_csv(path.join(pasta, "Re18000.csv"))
Re18["Velocity [ m s^-1 ]"] = (
    Re18["Velocity [ m s^-1 ]"] / Re18["Velocity [ m s^-1 ]"].max()
)
Re18["Y [ mm ]"] = (Re18["Y [ mm ]"] - Re18["Y [ mm ]"].iloc[0]) / (
    Re18["Y [ mm ]"].iloc[-1] - Re18["Y [ mm ]"].iloc[0]
)

# Re18_malha6 = pd.read_csv(r'C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Codigos python e processamentos\velo_malha6.csv')
# Re18_malha6["Velocity Magnitude"] = Re18_malha6["Velocity Magnitude"]/Re18_malha6["Velocity Magnitude"].max()
# Re18_malha6["Position"] = (Re18_malha6["Position"] - Re18_malha6["Position"].iloc[0] )/ (Re18_malha6["Position"].iloc[-1] - Re18_malha6["Position"].iloc[0] )


fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    Re10["Velocity [ m s^-1 ]"],
    Re10["Y [ mm ]"],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Q = 0,34 [m$^3$/h]",
    marker="s",
    mfc="none",
)
ax.plot(
    Re13["Velocity [ m s^-1 ]"],
    Re13["Y [ mm ]"],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Q = 0,455 [m$^3$/h]",
    marker="o",
    mfc="none",
)
ax.plot(
    Re15["Velocity [ m s^-1 ]"],
    Re15["Y [ mm ]"],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Q = 0,523 [m$^3$/h]",
    marker="*",
    mfc="none",
)
ax.plot(
    Re18["Velocity [ m s^-1 ]"],
    Re18["Y [ mm ]"],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Q = 0,629 [m$^3$/h]",
    marker="x",
    mfc="none",
)

# ax.plot(Re18_malha6["Velocity Magnitude"],Re18_malha6["Position"])
ax.plot(
    experimental["x"],
    experimental["Curve1"],
    label=r"Experimental Re ~ 11900 $\beta$ = 0,8",
    ms=5,
    marker="^",
    mfc="none",
)
ax.set(
    xlabel=r"Magnitude de velocidade V/V$_{max}$ [-]",
    ylabel=r"Posição radial normalizada [-]",
)
# ax.set_xlim = [0,1]
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend()
