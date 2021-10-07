import os
import subprocess
import pymatgen as pmg
import numpy as np
dir = '/lustre/athall/LLZO/cubic/Ta/bulk_mod/vol_relax/rand_100'

energies = []

os.chdir(dir)
for dirname in next(os.walk('.'))[1]:
### Method to test for completeness ###
#    print(dirname)
#    os.system('tail -1 '+dir+'/%s/relax/vaspinput/OUTCAR' % dirname)
### Saves the toten from vasprun ###
    run = pmg.io.vasp.Vasprun('%s/relax/vaspinput/vasprun.xml' % dirname)
    energies.append([dirname,run.final_energy])

np.save('energies.npy',energies)

energ = []

for i in np.load('energies.npy'):
    i[1] = i[1].replace(' eV', '')
    energ.append([i[0],float(i[1])])

np.save('energies.npy',energ)
