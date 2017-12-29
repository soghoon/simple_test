import numpy as np 
import scipy.constants as spc

mc = spc.m_e * spc.c
mc2 = spc.m_e * spc.c**2
'''We do not need mc3 / if we need we can built it any time. please check. this'''
''' Ok.'''

### Particle datas ###
particle_IDs = [1,2,3,4,5]
particle_gammas = [1.01,1.33,2.34,4.44,1.0]


plt.plot(partie_IDs, particle_gammas)
plt.show()