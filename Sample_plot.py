

# PACOTES
from os import listdir, path
import pandas as pd
import re
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import MultipleLocator as ML
from sys import platform

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=18)  # fontsize of the axes title
plt.rc("axes", labelsize=14)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=13)  # fontsize of the tick labels
plt.rc("ytick", labelsize=13)  # fontsize of the tick labels
plt.rc("legend", fontsize=9)  # legend fontsize
plt.rc("font", size=13)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("deep", 6) 




"ABRINDO TODOS OS ARQUIVOS"



entrada = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 2 dpm\Casos 1 a 4"
entrada2 = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 2 dpm\Samples quebra sem adesao 12-07-2022"
entrada3 = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 2 dpm\Casos 5 a 8"
saida =   r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Figuras\DPM"





## GRÁFICOS TIPO 1
#   time x parcels in fluido

f = open(path.join(entrada, "time x parcels in fluido.tsv"), mode="r")
t_parcels = pd.read_csv(f,skiprows=2,header=0, sep='\t',decimal='.',engine='python')

# GRÁFICOS TIPO 2
f = open(path.join(entrada, "caso 1.txt"), mode="r")
z_dat_1 = pd.read_csv(f,header=0, sep='\t',decimal='.',engine='python')
f = open(path.join(entrada, "caso 2.txt"), mode="r")
z_dat_2 = pd.read_csv(f,header=0, sep='\t',decimal='.',engine='python')
f = open(path.join(entrada, "caso 3.txt"), mode="r")
z_dat_3 = pd.read_csv(f,header=0, sep='\t',decimal='.',engine='python')
f = open(path.join(entrada, "caso 4.txt"), mode="r")
z_dat_4 = pd.read_csv(f,header=0, sep='\t',decimal='.',engine='python')


# GRÁFICOS TIPO 3
f = open(path.join(entrada2, "dtg_const caso 1.csv"), mode="r")
dtg_const_1 = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_const caso 2.csv"), mode="r")
dtg_const_2 = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_const caso 3.csv"), mode="r")
dtg_const_3 = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_const caso 4.csv"), mode="r")
dtg_const_4 = pd.read_csv(f,header=0,decimal='.',engine='python')

f = open(path.join(entrada3, "dtg_const caso 5.csv"), mode="r")
dtg_const_5 = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_const caso 6.csv"), mode="r")
dtg_const_6 = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_const caso 7.csv"), mode="r")
dtg_const_7 = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_const caso 8.csv"), mode="r")
dtg_const_8 = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')


# GRÁFICOS TIPO 4
'Casos 1 a 4'
f = open(path.join(entrada2, "dtg_perfis z 1 caso 1.csv"), mode="r")
dtg_1_in = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 369 caso 1.csv"), mode="r")
dtg_1_out = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 1 caso 2.csv"), mode="r")
dtg_2_in = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 369 caso 2.csv"), mode="r")
dtg_2_out = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 1 caso 3.csv"), mode="r")
dtg_3_in = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 369 caso 3.csv"), mode="r")
dtg_3_out = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 1 caso 4.csv"), mode="r")
dtg_4_in = pd.read_csv(f,header=0,decimal='.',engine='python')
f = open(path.join(entrada2, "dtg_perfis z 369 caso 4.csv"), mode="r")
dtg_4_out = pd.read_csv(f,header=0,decimal='.',engine='python')

'Casos 5 a 8'
f = open(path.join(entrada3, "dtg_perfis z 1 caso 5.csv"), mode="r")
dtg_5_in = pd.read_csv(f,header=0,decimal='.',sep = '\t',engine='python')
f = open(path.join(entrada3, "dtg_perfis z 369 caso 5.csv"), mode="r")
dtg_5_out = pd.read_csv(f,header=0,decimal='.',sep = '\t',engine='python')
f = open(path.join(entrada3, "dtg_perfis z 1 caso 6.csv"), mode="r")
dtg_6_in = pd.read_csv(f,header=0,decimal='.',sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_perfis z 369 caso 6.csv"), mode="r")
dtg_6_out = pd.read_csv(f,header=0,decimal='.',sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_perfis z 1 caso 7.csv"), mode="r")
dtg_7_in = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_perfis z 369 caso 7.csv"), mode="r")
dtg_7_out = pd.read_csv(f,header=0,decimal='.',sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_perfis z 1 caso 8.csv"), mode="r")
dtg_8_in = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')
f = open(path.join(entrada3, "dtg_perfis z 369 caso 8.csv"), mode="r")
dtg_8_out = pd.read_csv(f,header=0,decimal='.', sep = '\t', engine='python')



"GRAFICO 1"
vazao_na_entrada = 0.14159  #kg/s
t_parcels = t_parcels.fillna(0)
t_parcels['t'] = t_parcels['t']-t_parcels['t'].min()


t = np.arange(0,10,1e-3)
t = np.append(t,10.0)

nt = np.interp(t,t_parcels['t'],t_parcels['number_tracked'])
sc = np.interp(t,t_parcels['t'],t_parcels['scaped'])



# Plot 1
#plt.plot(t,nt)
mass_in_domain = 100*0.0488*nt/nt.max()
fig, ax = plt.subplots(tight_layout=True)
plt.plot(t,mass_in_domain,
            alpha=0.9,
            ls='-',
            color = cor[3])

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
#ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.95, 0.75))
ax.set(ylabel=r"Concentração volumétrica no domínio $\alpha_d$", xlabel=r"t [s]")
anot = 'Caso 1\n'
anot += r'$Q$ = 600 L/h'
anot += '\n'
anot += r'$\rho=5$ cP'
anot += '\n'
anot += r'$Re$ = 5150'
anot += '\n'
anot += r'$\alpha_d = 5\%$'

plt.text(8,2,anot,wrap=True,fontsize=11,bbox=dict(facecolor='white', alpha=1))
plt.show()





"GRAFICO 2"
mdpm = 0.0493*vazao_na_entrada
mass_balance = mdpm*np.append(0,np.diff(nt))/np.append(0,np.diff(nt)).max()
dpm_out = mdpm*sc/sc.max()




fig, ax = plt.subplots(tight_layout=True)
ax.plot(t,mass_balance,lw=2,
            alpha=0.9,
            ls='-',
            label =r'Diferença entrada e saída',
            color = cor[0])
ax.plot(t,dpm_out,lw=2,
            alpha=0.9,
            ls='-',
            label =r'Saída',
            color = cor[1])

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.95, 0.75))
ax.set(ylabel=r"Vazão mássica $\dot{m}_d$ [kg/s]", xlabel=r"t [s]")
anot = 'Caso 1\n'
anot += r'$Q$ = 600 L/h'
anot += '\n'
anot += r'$\rho=5$ cP'
anot += '\n'
anot += r'$Re$ = 5150'
anot += '\n'
anot += r'$\alpha_d = 5\%$'

plt.text(6.1,0.0029,anot,wrap=True,fontsize=11,bbox=dict(facecolor='white', alpha=1))
plt.show()





























# PRESSÃO MEDIA EM CADA PLANO
# AREA AVE OF PRESSURE

fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    z_dat_1['Z'],
    z_dat_1['PRESSAO']/1000,
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    z_dat_2['Z'],
    z_dat_2['PRESSAO']/1000,
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label='Caso 2, 1000 L/h',
    marker="o",
    mfc="none",
)
ax.plot(
    z_dat_3['Z'],
    z_dat_3['PRESSAO']/1000,
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label='Caso 3, 600 L/h',
    marker="*",
    mfc="none",
)
ax.plot(
    z_dat_4['Z'],
    z_dat_4['PRESSAO']/1000,
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label='Caso 4, 1000 L/h',
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.95, 0.75))
ax.set(ylabel=r"Pressão estática manométrica [kPa]", xlabel=r"z [mm]")



# TDR MEDIO EM CADA PLANO
# AREA AVE OF TURBULENT DISSIPATION RATE


fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    z_dat_1['Z'],
    z_dat_1['TDR'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    z_dat_2['Z'],
    z_dat_2['TDR'],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    z_dat_3['Z'],
    z_dat_3['TDR'],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 3, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    z_dat_4['Z'],
    z_dat_4['TDR'],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 4, 1000 L/h",
    marker="x",
    mfc="none",
)
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.95, 0.75))
ax.set(ylabel=r"Taxa de dissipação da turbulência, $\varepsilon$, [$m^2/s^3$] ", xlabel=r"z [mm]")







## MAX VEL

fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    z_dat_1['Z'],
    z_dat_1['MAX VEL'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    z_dat_2['Z'],
    z_dat_2['MAX VEL'],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    z_dat_3['Z'],
    z_dat_3['MAX VEL'],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 3, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    z_dat_4['Z'],
    z_dat_4['MAX VEL'],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 4, 1000 L/h",
    marker="x",
    mfc="none",
)
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.75))
ax.set(ylabel=r"Velocidade máxima [$m/s$] ", xlabel=r"z [mm]")







# MED VEL


fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    z_dat_1['Z'],
    z_dat_1['MED VEL'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    z_dat_2['Z'],
    z_dat_2['MED VEL'],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    z_dat_3['Z'],
    z_dat_3['MED VEL'],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 3, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    z_dat_4['Z'],
    z_dat_4['MED VEL'],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 4, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.75))
ax.set(ylabel=r"Velocidade média [$m/s$] ", xlabel=r"z [mm]")











# PLOTS COM DPM


fig, ax = plt.subplots(dpi=100, tight_layout=True)

ax.plot(
    1000*dtg_const_1['z'],
    dtg_const_1['V_med'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_2['z'],
    dtg_const_2['V_med'],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_3['z'],
    dtg_const_3['V_med'],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 3, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_4['z'],
    dtg_const_4['V_med'],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 4, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.plot(
    1000*dtg_const_5['z'],
    dtg_const_5['V_med'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 5, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_6['z'],
    dtg_const_6['V_med'],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 6, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_7['z'],
    dtg_const_7['V_med'],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 7, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_8['z'],
    dtg_const_8['V_med'],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 8, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.75))
ax.set(ylabel=r"Velocidade média das gotas [$m/s$] ", xlabel=r"z [mm]")





# COMPARATIVO ENTRE AS VELOCIDADES MEDIAS DO ÓLEO E DAS GOTÍCULAS DE ÁGUA


fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    z_dat_1['Z'],
    z_dat_1['MED VEL'],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_1['z'],
    dtg_const_1['V_med'],
    lw=1,
    alpha=1,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h gotas",
    marker="*",
    mfc="none",
    color = cor[3],
)
ax.plot(
    z_dat_2['Z'],
    z_dat_2['MED VEL'],
    lw=1,
    alpha=1,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_2['z'],
    dtg_const_2['V_med'],
    lw=1,
    alpha=1,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h gotas",
    marker="x",
    mfc="none",
    color = cor[4],
)

ax.plot(
    1000*dtg_const_5['z'],
    dtg_const_5['V_med'],
    lw=1,
    alpha=1,
    ls="--",
    ms=5,
    label="Caso 5, 600 L/h gotas",
    marker="d",
    mfc="none",
    color = cor[0],
)

ax.plot(
    1000*dtg_const_6['z'],
    dtg_const_6['V_med'],
    lw=1,
    alpha=1,
    ls="--",
    ms=5,
    label="Caso 6, 1000 L/h gotas",
    marker="+",
    mfc="none",
    color = cor[1],
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.75))
ax.set(ylabel=r"Velocidade média [$m/s$] ", xlabel=r"z [mm]")





D = 'D50'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    1000*dtg_const_1['z'],
    1e6*dtg_const_1[D],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 1, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_2['z'],
    1e6*dtg_const_2[D],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 2, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_3['z'],
    1e6*dtg_const_3[D],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 3, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_4['z'],
    1e6*dtg_const_4[D],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 4, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.75))
ax.set(ylabel=r"Diâmetro D10 [$\mu m$]", xlabel=r"z [mm]")








D = 'D10'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
# ax.plot(
#     1000*dtg_const_1['z'],
#     1e6*dtg_const_1[D],
#     lw=1,
#     alpha=0.9,
#     ls="--",
#     ms=5,
#     label="Caso 1, 600 L/h",
#     marker="s",
#     mfc="none",
# )
ax.plot(
    1000*dtg_const_2['z'],
    1e6*dtg_const_2[D],
    lw=2,
    alpha=0.9,
    ls=":",
    ms=6,
    label="Caso 2, 1000 L/h, $\mu=5$ cP, $Re$ = 8590",
    marker="o",
    mfc="none",
    color = cor[3],
)
# ax.plot(
#     1000*dtg_const_3['z'],
#     1e6*dtg_const_3[D],
#     lw=1,
#     alpha=0.9,
#     ls="-.",
#     ms=5,
#     label="Caso 3, 600 L/h",
#     marker="*",
#     mfc="none",
# )
ax.plot(
    1000*dtg_const_4['z'],
    1e6*dtg_const_4[D],
    lw=2,
    alpha=0.9,
    ls="-",
    ms=6,
    label="Caso 4, 1000 L/h, $\mu=7$ cP, $Re$ = 6135",
    marker="x",
    mfc="none",
    color = cor[2],
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.53, 0.22))
ax.set(ylabel=r"Diâmetro D10 [$\mu m$]", xlabel=r"z [mm]")




D = 'D90'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
# ax.plot(
#     1000*dtg_const_1['z'],
#     1e6*dtg_const_1[D],
#     lw=1,
#     alpha=0.9,
#     ls="--",
#     ms=5,
#     label="Caso 1, 600 L/h",
#     marker="s",
#     mfc="none",
# )
ax.plot(
    1000*dtg_const_2['z'],
    1e6*dtg_const_2[D],
    lw=2,
    alpha=1,
    ls=":",
    ms=6,
    label="Caso 2, 1000 L/h, $\mu=5$ cP, $Re$ = 8590",
    marker="o",
    mfc="none",
    color = cor[3],
)
# ax.plot(
#     1000*dtg_const_3['z'],
#     1e6*dtg_const_3[D],
#     lw=1,
#     alpha=0.9,
#     ls="-.",
#     ms=5,
#     label="Caso 3, 600 L/h",
#     marker="*",
#     mfc="none",
# )
ax.plot(
    1000*dtg_const_4['z'],
    1e6*dtg_const_4[D],
    lw=2,
    alpha=1,
    ls="-",
    ms=6,
    label="Caso 4, 1000 L/h, $\mu=7$ cP, $Re$ = 6135",
    marker="x",
    mfc="none",
    color = cor[2],
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.54, 0.22))
ax.set(ylabel=r"Diâmetro D90 [$\mu m$] ", xlabel=r"z [mm]")



















'Casos com diametro medio 120'
D = 'D10'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    1000*dtg_const_5['z'],
    1e6*dtg_const_5[D],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 5, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_6['z'],
    1e6*dtg_const_6[D],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 6, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_7['z'],
    1e6*dtg_const_7[D],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 7, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_8['z'],
    1e6*dtg_const_8[D],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 8, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.55))
ax.set(ylabel=r"Diâmetro D10 [$\mu m$] ", xlabel=r"z [mm]")






'Casos com diametro medio 120'
D = 'D50'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    1000*dtg_const_5['z'],
    1e6*dtg_const_5[D],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 5, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_6['z'],
    1e6*dtg_const_6[D],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 6, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_7['z'],
    1e6*dtg_const_7[D],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 7, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_8['z'],
    1e6*dtg_const_8[D],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 8, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.55))
ax.set(ylabel=r"Diâmetro D50 [$\mu m$] ", xlabel=r"z [mm]")






'Casos com diametro medio 120'
D = 'D90'
fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
    1000*dtg_const_5['z'],
    1e6*dtg_const_5[D],
    lw=1,
    alpha=0.9,
    ls="--",
    ms=5,
    label="Caso 5, 600 L/h",
    marker="s",
    mfc="none",
)
ax.plot(
    1000*dtg_const_6['z'],
    1e6*dtg_const_6[D],
    lw=1,
    alpha=0.9,
    ls=":",
    ms=5,
    label="Caso 6, 1000 L/h",
    marker="o",
    mfc="none",
)
ax.plot(
    1000*dtg_const_7['z'],
    1e6*dtg_const_7[D],
    lw=1,
    alpha=0.9,
    ls="-.",
    ms=5,
    label="Caso 7, 600 L/h",
    marker="*",
    mfc="none",
)
ax.plot(
    1000*dtg_const_8['z'],
    1e6*dtg_const_8[D],
    lw=1,
    alpha=0.9,
    ls="-",
    ms=5,
    label="Caso 8, 1000 L/h",
    marker="x",
    mfc="none",
)

ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.45, 0.55))
ax.set(ylabel=r"Diâmetro D90 [$\mu m$] ", xlabel=r"z [mm]")

















threshold = 0.01

# fig, ax = plt.subplots(dpi=100, tight_layout=True)
# ax.plot(
#      1e6*dtg_1_in['diameter'],
#      dtg_1_in['frac_mass'],
#      lw=2,
#      alpha=0.9,
#      ls="--",
#      ms=5,
#      label="Caso 1 entrada",
#      marker="s",
#      mfc="none",
# )
# df = dtg_1_out[['diameter','frac_mass']]
# df = df.drop(df[df['frac_mass'] < threshold].index) 
# ax.plot(
#     1e6*df['diameter'],
#     df['frac_mass'],
#     lw=2,
#     alpha=1,
#     ls=":",
#     ms=6,
#     label="Caso 1 saida",
#     marker="o",
#     mfc="none",
#     color = cor[3],
# )
# ax.grid()
# ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
# ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.7, 0.62))
# ax.set(ylabel=r"Fração Mássica $Y_g$ > 0,01 [%]", xlabel=r"Diâmetro [$\mu$m]")




# fig, ax = plt.subplots(dpi=100, tight_layout=True)
# ax.plot(
#      1e6*dtg_2_in['diameter'],
#      dtg_2_in['frac_mass'],
#      lw=2,
#      alpha=0.9,
#      ls="--",
#      ms=5,
#      label="Caso 2 entrada",
#      marker="s",
#      mfc="none",
# )
# df = dtg_2_out[['diameter','frac_mass']]
# df = df.drop(df[df['frac_mass'] < threshold].index) 
# ax.plot(
#     1e6*df['diameter'],
#     df['frac_mass'],
#     lw=2,
#     alpha=1,
#     ls=":",
#     ms=6,
#     label="Caso 2 saida",
#     marker="o",
#     mfc="none",
#     color = cor[3],
# )
# ax.grid()
# ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
# ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.7, 0.62))
# ax.set(ylabel=r"Fração Mássica $Y_g$ > 0,01 [%]", xlabel=r"Diâmetro [$\mu$m]")



# fig, ax = plt.subplots(dpi=100, tight_layout=True)
# ax.plot(
#      1e6*dtg_3_in['diameter'],
#      dtg_3_in['frac_mass'],
#      lw=2,
#      alpha=0.9,
#      ls="--",
#      ms=5,
#      label="Caso 3 entrada",
#      marker="s",
#      mfc="none",
# )
# df = dtg_3_out[['diameter','frac_mass']]
# df = df.drop(df[df['frac_mass'] < threshold].index) 
# ax.plot(
#     1e6*df['diameter'],
#     df['frac_mass'],
#     lw=2,
#     alpha=1,
#     ls=":",
#     ms=6,
#     label="Caso 3 saida",
#     marker="o",
#     mfc="none",
#     color = cor[3],
# )
# ax.grid()
# ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
# ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.7, 0.62))
# ax.set(ylabel=r"Fração Mássica $Y_g$ > 0,01 [%]", xlabel=r"Diâmetro [$\mu$m]")



fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
     1e6*dtg_4_in['diameter'],
     dtg_4_in['frac_mass'],
     lw=2,
     alpha=0.9,
     ls="--",
     ms=5,
     label="Caso 4 entrada",
     marker="s",
     mfc="none",
     color=cor[0],
)
df = dtg_4_out[['diameter','frac_mass']]
df = df.drop(df[df['frac_mass'] < threshold].index)
ax.plot(
    1e6*df['diameter']-1,
    1.05*df['frac_mass'],
    lw=2,
    alpha=1,
    ls=":",
    ms=6,
    label="Caso 4 saída",
    marker="o",
    mfc="none",
    color = cor[3],
)
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.7, 0.62))
ax.set(ylabel=r"Fração mássica $Y_g$ > 0,01 [%]", xlabel=r"Diâmetro [$\mu$m]")







fig, ax = plt.subplots(dpi=100, tight_layout=True)
ax.plot(
     1e6*dtg_8_in['diameter'],
     dtg_8_in['frac_mass_acum'],
     lw=2,
     alpha=0.9,
     ls="--",
     ms=5,
     label="Caso 8 entrada",
     marker="s",
     mfc="none",
     color=cor[0],
)

# fig, ax = plt.subplots(dpi=100, tight_layout=True)
df = dtg_8_out[['diameter','frac_mass']]
df = df.drop(df[df['frac_mass'] < threshold].index)

ax.plot(
     1e6*dtg_8_out['diameter'],
     dtg_8_out['frac_mass_acum'],
    lw=2,
    alpha=1,
    ls=":",
    ms=6,
    label="Caso 8 saída",
    marker="o",
    markevery = 0.06,
    mfc="none",
    color = cor[3],
)
ax.grid()
ax.tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax.legend(loc="right", fancybox=True, shadow=True, ncol=1, bbox_to_anchor=(0.85, 0.52))
ax.set(ylabel=r"Fração mássica acumulada [%]", xlabel=r"Diâmetro [$\mu$m]")






#entrada, D10, D50, D90
fig,ax = plt.subplots(1,2,tight_layout=True,dpi=100,figsize=(8, 4.5))

D_carac_1a4 = np.array([[14.54, 14.46, 14.26, 14.48, 12.92],
                        [29.37, 29.35, 29.37, 29.37, 29.37],
                        [59.43, 59.3, 55.62, 59.42, 54.65]])

D_carac_5a8 = np.array([[88, 77.945, 64.288, 77.945, 64.14],
                        [121, 114.95, 95.27, 112.96, 94.863],
                        [160, 154.45, 128.44, 151.71, 128.158]])

ax[0].scatter(['Entrada', 'Caso 1', 'Caso 2', 'Caso 3', 'Caso 4'],
              D_carac_1a4[0],
              s=40,
              marker="o",
              edgecolors="face",
              c = cor[3])
ax[0].scatter(['Entrada', 'Caso 1', 'Caso 2', 'Caso 3', 'Caso 4'],
              D_carac_1a4[1],
              s=40,
              marker="s",
              edgecolors="face",
              c = cor[4])
ax[0].scatter(['Entrada', 'Caso 1', 'Caso 2', 'Caso 3', 'Caso 4'],
              D_carac_1a4[2],
              s=40,
              marker="d",
              edgecolors="face",
              c = cor[5])


ax[1].scatter(['Entrada', 'Caso 5', 'Caso 6', 'Caso 7', 'Caso 8'],
              D_carac_5a8[0],
              s=40,
              marker="o",
              edgecolors="face",
              c = cor[3])
ax[1].scatter(['Entrada', 'Caso 5', 'Caso 6', 'Caso 7', 'Caso 8'],
              D_carac_5a8[1],
              s=40,
              marker="s",
              edgecolors="face",
              c = cor[4])
ax[1].scatter(['Entrada', 'Caso 5', 'Caso 6', 'Caso 7', 'Caso 8'],
              D_carac_5a8[2],
              s=40,
              marker="d",
              edgecolors="face",
              c = cor[5])


ax[0].set_xlabel('(a)')
ax[1].set_xlabel('(b)')

ax[0].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[0].tick_params(axis="x", which="both", direction="inout")
ax[1].tick_params(axis="both", which="both", direction="in", top=1, right=1)
ax[1].tick_params(axis="x", which="both", direction="inout")

fig.supylabel(r"Diâmetro $\mu$m")
fig.legend(['D10','D50','D90'],framealpha=0.9)
plt.show()
















# entrada4 = r"C:\Users\Murilo\Google Drive\Arquivos PG Murilo\Resultados de simulações\Etapa 2 dpm\Dados brutos casos 1 a 8"
# # f = open(path.join(entrada4, "z1 caso 1"), mode="r")


# # cols = np.array([3, 4, 5, 6, 7, 9, 11])
# # if platform == "linux" or platform == "linux2":
# #     names = pd.read_csv(f, sep='[\(\)\s]+', skiprows=1,usecols=(cols-1),header=None, decimal=",",nrows=1, engine='python', dtype=str)
# # elif platform == "darwin":
# #     pass
# # elif platform == "win32":
# #     names = pd.read_csv(f, sep='[\(\)\s]+', skiprows=1,usecols=cols,header=None, decimal=",",nrows=1, engine='python', dtype=str)


# # names = names.values[0].tolist()
# names = ['diameter']
# f = open(path.join(entrada4, "z1 caso 1.dpm"), mode="r")
# z1caso1 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 1.dpm"), mode="r")
# z369caso1 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 2.dpm"), mode="r")
# z1caso2 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 2.dpm"), mode="r")
# z369caso2 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 3.dpm"), mode="r")
# z1caso3 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 3.dpm"), mode="r")
# z369caso3 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 4.dpm"), mode="r")
# z1caso4 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 4.dpm"), mode="r")
# z369caso4 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')


# f = open(path.join(entrada4, "z1 caso 5.dpm"), mode="r")
# z1caso5 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 5.dpm"), mode="r")
# z369caso5 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 6.dpm"), mode="r")
# z1caso6 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 6.dpm"), mode="r")
# z369caso6 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 7.dpm"), mode="r")
# z1caso7 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 7.dpm"), mode="r")
# z369caso7 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z1 caso 8.dpm"), mode="r")
# z1caso8 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')

# f = open(path.join(entrada4, "z369 caso 8.dpm"), mode="r")
# z369caso8 = pd.read_csv(f, sep='[\(\)\s]+',skiprows=2,usecols=[7],names=names, engine='python')




# plt.figure()
# plt.boxplot([1e6*z1caso1['diameter'],1e6*z369caso1['diameter'],
#              1e6*z1caso2['diameter'],1e6*z369caso2['diameter'],
#              1e6*z1caso3['diameter'],1e6*z369caso3['diameter'],
#              1e6*z1caso4['diameter'],1e6*z369caso4['diameter']])

# plt.figure()
# plt.boxplot([1e6*z1caso5['diameter'],1e6*z369caso5['diameter'],
#              1e6*z1caso6['diameter'],1e6*z369caso6['diameter'],
#              1e6*z1caso7['diameter'],1e6*z369caso7['diameter'],
#              1e6*z1caso8['diameter'],1e6*z369caso8['diameter']])





