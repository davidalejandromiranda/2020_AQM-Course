# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:02:23 2018

@author: David A. Miranda, PhD
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_session()

x,p,hbar = symbols('x,p,hbar')
n = symbols('n', integer=True)
psi = cos(n*pi*x/4)/sqrt(2)

pretty_print(('psi(x)',psi))

E_x2 = simplify(integrate(x**2 * psi**2, (x, -2, 2)))
E_x  = simplify(integrate(x * psi**2, (x, -2, 2)))
sigma2_x = (E_x2 - E_x**2).simplify()

pretty_print(('sigma_x^2', sigma2_x))

E_p2 = simplify(-hbar**2*integrate(psi * diff(psi, x, 2), (x, -2, 2)))
E_p  = simplify(-1j*hbar*integrate(psi * diff(psi, x), (x, -2, 2)))

sigma2_p = (E_p2 - E_p**2).simplify()


pretty_print(('sigma_p^2', sigma2_p))


s2_x = sigma2_x.args[1][0].evalf()
s2_p = sigma2_p.args[1][0].evalf()

s2_p = s2_p.subs({hbar:1})  # It doew hbar = 1

sx = np.array([])
sp = np.array([])

n_eval = np.arange(1,10)

for nn in n_eval:
    sx = np.append(sx, sqrt(s2_x.subs({n:nn})))
    sp = np.append(sp, sqrt(s2_p.subs({n:nn})))

plt.plot(n_eval, sx*sp, 'ko', label=r'$\sigma_x \sigma_p/\hbar$')
plt.plot(n_eval, sp, 'k^', label=r'$\sigma_p/\hbar$')
plt.plot(n_eval, sx, 'kv', label=r'$\sigma_x$')

plt.xlabel('n')
plt.legend()
