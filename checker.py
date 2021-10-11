#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import subprocess
import pymatgen as pmg
import numpy as np


# In[6]:


dir = '/Users/ath/umd_projects/LLZO/cubic/Ta/408/unstressed/Li_trials'


# In[29]:


energies = []

os.chdir(dir)
for dirname in next(os.walk('.'))[1]:
### Method to test for completeness ###
#    print(dirname)
#    os.system('tail -1 '+dir+'/%s/relax/vaspinput/OUTCAR' % dirname)
### Saves the toten from vasprun ###
    run = pmg.io.vasp.Vasprun('%s/relax/vaspinput/vasprun.xml' % dirname)
    struct = pmg.Structure.from_file('%s/relax/vaspinput/vasprun.xml' % dirname)
    en = str(run.final_energy)
    en = en.replace(' eV', '')
    en = float(en)
    vol = struct.volume
    vol = float(vol)
    dirname = str(dirname)
    #print(dirname,vol,en)
    energies.append((dirname,vol,en))

#print(energies.shape)
#print(energies.index(min(energies[:][2])))
np.save('energies.npy',energies)


# In[59]:


E_list = [n[2] for n in energies]


# In[60]:


low_E = min(E_list)


# In[61]:


low_E_index = E_list.index(low_E)


# In[63]:


locate = energies[low_E_index][0]


# In[64]:


print('Lowest energy configuration is in '+str(locate)+' with an energy of '+str(low_E))


# In[ ]:





# In[ ]:




