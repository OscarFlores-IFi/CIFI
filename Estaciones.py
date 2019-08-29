#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:10:46 2019

@author: fh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%#### Generar datos aleatorios. 
#dest = np.random.normal(50,25,(24,2))
norm = np.round(dest,1)
pnorm = pd.DataFrame(norm)
pnorm.columns=['x','y']
pnorm.to_csv('coordenadas.csv')

#%%#### Dibujar mapa. 
plt.figure(figsize=(6,6))
plt.scatter(norm[:,0],norm[:,1],c='k')
plt.scatter([0,100],[0,100],marker='*',c='r',s=100)
plt.grid()
plt.axis('square')
plt.xlabel('x')
plt.ylabel('y')

##%% Rutas ejemplo.
ex = np.array([[[0,42.2,58.2,65.5,70.1,58.4,76,100],
                [0,3.1,15.6,22.1,23.7,26.2,57.5,100]],
                [[0,-4.2,8.8,22.8,30.9,37.2,81.4,100],
                [0,33.4,53,69.6,52.5,35.7,90,100]]])

for i in ex:
    plt.plot(i[0],i[1])

plt.show()