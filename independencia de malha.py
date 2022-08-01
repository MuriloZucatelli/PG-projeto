# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:18:45 2022

@author: Murilo
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import MultipleLocator as ML

sns.set_style("ticks")  # darkgrid, white grid, dark, white and ticks

plt.rc("axes", titlesize=18)  # fontsize of the axes title
plt.rc("axes", labelsize=14)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=13)  # fontsize of the tick labels
plt.rc("ytick", labelsize=11)  # fontsize of the tick labels
plt.rc("legend", fontsize=12)  # legend fontsize
plt.rc("font", size=13)  # controls default text sizes

# cor = sns.color_palette('Set2')
# cor = sns.color_palette('deep')
# sns.color_palette("Paired") #sequencia de cores pairadas entre claro e escuro na sequencia
cor = sns.color_palette("husl", 4)


#Caso 2.5 m/s

v = np.array([3.1578434, 3.1576651,3.201])
p = np.array([151.51968, 156.18348,169.5271])
E = np.array([266.8392, 260.07275, 285.2])


#Caso 1.5 m/s

v = np.array([1.8822014, 1.8861565, 1.9146072])    # grosseira, media, fina
p = np.array([56.328242, 58.170484, 63.123542])
E = np.array([52.28027, 52.162182, 58.097829])

def Vtoh(V):
    return 1000 * (V) ** (1 / 3)


Vg = 10.176742e-11  # 9.4919e-11
Vm = 7.5417967e-11  # na válvula 6.5034e-11
Vf = 6.1835755e-11  # m3

h = Vtoh(np.array([Vf, Vm, Vg]))
#
#   Facet average of volume cells cuted by a plane in the z = 200 mm
#
# h = Vtoh(np.array([4.9199723e-11, 1.7203592e-11, 9.8603455e-12]))

fig, ax = plt.subplots(3, 1, tight_layout=True, sharex=True)
fig.subplots_adjust(hspace=0)

# ax[0].scatter(
#     h,
#     v,
#     ,
#     alpha=0.9,
#     ls="--",
#     ms=5,
#     marker=("o", "*", "v"),
#     mfc=(cor[0], cor[1], cor[2]),
#     color=cor[3],
# )

ax[0].plot(h, v, ls="dotted", lw=2, marker="s", c=cor[2])
ax[0].set_ylabel(r"V $[m/s]$")
ax[0].set_yticks(v)
ax[0].yaxis.set_major_formatter(StrMethodFormatter("{x:,.2f}"))

ax[1].plot(h, p, ls="dotted", lw=2, marker="s", c=cor[2])
ax[1].set_ylabel("P [kPa]")
ax[1].set_yticks(p)
ax[1].yaxis.set_major_formatter(StrMethodFormatter("{x:,.1f}"))

ax[2].plot(h, E, ls="dotted", lw=2, marker="s", c=cor[2])
ax[2].set_ylabel(r"$\varepsilon$ $[m^2/s^3]$")
ax[2].set_yticks([E[2], E[0]])
ax[2].yaxis.set_major_formatter(StrMethodFormatter("{x:,.1f}"))
# ax[2].yaxis.set_major_locator(ML(5))

# ax.xaxis.set_xlabel()
fig.supxlabel("Tamanho médio do elemento h [mm]")
ax[1].set_xticks(h)
ax[2].get_xaxis().set_major_formatter(StrMethodFormatter("{x:,.3f}"))
plt.show()



## Implementacao GCI
r = [h[1]/h[0], h[2]/h[1]]  #r21 r32
e = np.array([[v[1]-v[0], v[2]-v[1]],
             [p[1]-p[0], p[2]-p[1]],
             [E[1]-E[0], E[2]-E[1]]])  #e21 v2-v1 e e32 v3-v2
phi = np.stack((v,p,E))  #e21 v2-v1 e e32 v3-v2

#chute
p0 = 1
erro = 1e-5
N = 100

def q(p,c,r):
    if(e[c][1]/e[c][0] < 0):
        s = -1
    elif(e[c][1]/e[c][0] == 0): 
        s = 0
    else:
        s = 1
    return np.log((r[0]**p-s)/(r[1]**p-s))

def f(p,c,r,e):
    return p - (1/np.log(r[0]))*abs(np.log(abs(e[c][1]/e[c][0]))+q(p,c,r))

def g(p,c,r,e):
    return (1/np.log(r[0]))*abs(np.log(abs(e[c][1]/e[c][0]))+q(p,c,r))


def fixedPointIteration(p0, erro, N, c, r, e):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        p1 = g(p0,c,r,e)
        print('Iteration-%d, p = %0.6f and f(p) = %0.6f' % (step, p1, f(p1,c,r,e)))
        p0 = p1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(p1,c,r,e)) > erro

    if flag==1:
        print('\nRequired root is: %0.8f' % p1)
    else:
        print('\nNot Convergent.')
    return p1



# Starting Newton Raphson Method
p_value = np.zeros(3)
for i in range(3):
    p_value[i] = fixedPointIteration(p0, erro, N, i, r, e)


# Valor extrapolado
phi_extr = np.zeros(3)
for i in range(3):
    phi_extr[i] = (r[0]**p_value[i] * phi[i][0] - phi[i][1])/(r[0]**p_value[i] -1)

# Calculando os erros
erro_aprox = np.zeros(3)
erro_extr = np.zeros(3)
gci = np.zeros(3)
for i in range(3):
    erro_aprox[i] = 100*abs( (phi[i][0] - phi[i][1]) / phi[i][0] )
    erro_extr[i] = 100*abs( (phi_extr[i] - phi[i][0]) / phi_extr[i] )
    gci[i] = 1.25*erro_aprox[i] / ( r[0]**p_value[i] - 1 )

# plt.close()

