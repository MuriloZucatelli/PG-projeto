# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


Q = np.array([0.629, 0.523, 0.455, 0.340])  # m3/h


def velo(Q):
    A = 1e-6 * np.pi * (21.5 ** 2 - 15 ** 2) / 4
    return (Q / 3600) / A


print(velo(Q))

"Calculo de Reynolds no espaço anular"
m_dot = 1000 * Q / 3600
Do = 21.5 / 1000  # m
Di = 15 / 1000  # m
Dh = Do - Di  # m
A = 1e-6 * np.pi * (21.5 ** 2 - 15 ** 2) / 4  # m^2
rho = 1000
mu = 0.001


def Re():
    return m_dot * Dh / (mu * A)


def Re_dh(V, Dh, rho, mu):
    return rho * V * Dh / mu


print(Re_dh(velo(Q), Dh, rho, mu))

Re_ast = (rho * velo(Q) / mu) * (
    (Do ** 2 + Di ** 2) / (Do - Di) - (Do + Di) / (np.log(Do / Di))
)
a = Di / Do
Re_3 = (
    rho
    * velo(Q)
    * Dh
    / mu
    * ((1 + a ** 2) * np.log(a) + (1 - a ** 2))
    / (np.log(a) * (1 - a) ** 2)
)

Q = 1046 / 24
Q = np.array([2])
print(velo(Q))
rho = 850
mu = 0.01
print(Re_dh(velo(Q), Dh, rho, mu))
