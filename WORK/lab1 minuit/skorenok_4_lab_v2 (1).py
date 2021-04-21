#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton


# ## Моделювання процесу пружнього розсіяння іонів на атомі
# 
# Написати програму-функцію, що знаходить кут розсіяння  в залежності від прицільного параметра р і енергії іона Е з використанням напівемпіричної формули:
# 
# $$\cos(\theta/2) = \frac{B + R_c + \Delta}{R_m + R_c}$$
# $$\Delta = A\frac{R_m - B}{1 + G}$$
# 

# ### Встановлення параметрів та констант

# In[90]:


# 1e-2 = 10 MeV
# 1e-3 = 1 MeV
# 1e-4 = 100 KeV
# 1e-5 = 10 KeV
# 1e-6 = 1 KeV

elements = {'D'   :  (1, 2), 
            'Ti'  :  (22, 48),
            '4He' :  (2, 4),
            '12C' :  (6, 12),
            '7Li' :  (3, 7),
            'Si'  :  (14, 28),
            'p'   :  (1, 1),
            '16O' :  (8, 16),
            '41Ar':  (18, 41),
            'T'   :  (1, 3),
            '6Li' :  (3, 6)} 

e = 1
a0 = 0.529

# Moliere 
a_par = [0.35, 0.55, 0.1]
b_par = [0.3, 1.2, 6]
C = [None, 0.67430, 0.00961, 0.00518, 10.0, 6.31400]

# Universal
# a_par = [0.1818, 0.5099, 0.2802, 0.02817]
# b_par = [3.2, 0.9423, 0.4029, 0.2016]
# C = [None, 0.75984, 5.71974, 6.14171, 9.5217, 6.26120]


# ### Безпосередньо функція обрахунку кута розсіяння
# 
# 1. Встановлення характеристик налітаючих іонів та мішені.
# 
# 2. Розрахунок енергії центра мас $E_c$ та безрозмірної енергії $\epsilon$.
# 
# 3. Розрахунок $r_m$ методом Ньютона.
# 
# 4. Кінцевий розрахунок кута розльоту за формулою 17.

# In[91]:


def cos_half_theta(p, element1, element2, E=0.01):
    
    # 1 ---
    Z1, M1 = elements[element1]
    Z2, M2 = elements[element2]
    
    # 2 ---
    a = 0.88534*a0/(np.power(Z1, 0.23) + np.power(Z2, 0.23))
    Ec = E/(1 + M1/M2) # center of mass energy
    epsilon = a*Ec/(Z1*Z2*np.square(e)) # dimensionless "reduced" energy
    
    # 3 ---
    
    def Fi(x):
        return np.sum(np.multiply(a_par, np.exp(-np.multiply(b_par, x))))

    def V(r):
        return Z1*Z2*np.square(e)*Fi(r/a)/r

    def dFi(x):
        return -np.sum(np.multiply(np.multiply(a_par, b_par), np.exp(-np.multiply(b_par, x))))

    def dV(r):
        return -Z1*Z2*np.square(e)*Fi(r/a)/np.square(r) + Z1*Z2*np.square(e)*dFi(r/a)/r

    def to_solve(r, Ec, p):
        return 1 - (V(r)/Ec) - np.square(p/r)

    def get_rm(Ec, p):
        return newton(lambda x: to_solve(x, Ec, p), 0.1)
    
    # 4 ---
    
    B = p/a
    rm = get_rm(Ec, p)
    ro = 2*(Ec - V(rm))/(-dV(rm))
    Rm = rm/a
    Rc = ro/a
    alpha = 1 + C[1]*np.power(epsilon, -1/2)
    betha = (C[2] + np.power(epsilon, 1/2))/(C[3] + np.power(epsilon, 1/2))
    gamma = (C[4] + epsilon)/(C[5] + epsilon)
    A = 2*alpha*epsilon*np.power(B, betha)
    G = gamma/(np.power(1 + np.square(A), 1/2) - A)
    Delta = A*(Rm - B)/(1 + G)
    
    return (B + Rc + Delta)/(Rm + Rc)


# З використанням написаної програми-функції побудувати залежність $sin^2(\theta/2)$ від $В=р/а$ для
# наступних пар іон – атом мішені:
# 1. D - Ti
# 2. 4He - 12C
# 3. 7Li - Si
# 4. p - 16O
# 5. 12C - 41Ar
# 6. T - 6Li
# 
# Розрахунки провести для В в інтервалі від 0 до 2 при енергіях Е=1,10,100 кеВ; 1,10 МеВ.

# In[92]:


def plot_graphs(el=None):
    x = np.linspace(0, 5, 100)

    y = [cos_half_theta(i, *el, 1e-2) for i in x]
    y = np.square(np.sin(np.arccos(y)))

    y1 = [cos_half_theta(i, *el, 1e-3) for i in x]
    y1 = np.square(np.sin(np.arccos(y1)))

    y2 = [cos_half_theta(i, *el, 1e-4) for i in x]
    y2 = np.square(np.sin(np.arccos(y2)))

    y3 = [cos_half_theta(i, *el, 1e-5) for i in x]
    y3 = np.square(np.sin(np.arccos(y3)))

    y4 = [cos_half_theta(i, *el, 1e-6) for i in x]
    y4 = np.square(np.sin(np.arccos(y4)))
    
    plt.figure(figsize=(12, 8))
    plt.ylabel(r'$sin(\theta/2)^2$', fontsize=18)
    plt.xlabel('p', fontsize=18)
    plt.plot(x, y, label='10 MeV')
    plt.plot(x, y1, label='1 MeV')
    plt.plot(x, y2, label='100 KeV')
    plt.plot(x, y3, label='10 KeV')
    plt.plot(x, y4, label='1 KeV')
    plt.legend()
#     plt.yscale('log')
    plt.show()


# In[93]:


plot_graphs(('12C', '41Ar'))


# In[32]:


plot_graphs(('D', 'Ti'))


# In[33]:


plot_graphs(('4He', '12C'))


# In[34]:


plot_graphs(('7Li', 'Si'))


# In[35]:


plot_graphs(('p', '16O'))


# In[36]:


plot_graphs(('T', '6Li'))

