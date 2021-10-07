import os
import subprocess
import pymatgen as pmg
import numpy as np
dir = '/lustre/athall/LLZO/cubic/Ta/bulk_mod/Li_then_Ta'

energies = []

os.chdir(dir)
for dirname in next(os.walk('.'))[1]:
### Method to test for completeness ###
#    print(dirname)
#    os.system('tail -1 '+dir+'/%s/relax/vaspinput/OUTCAR' % dirname)
### Saves the toten from vasprun ###
    run = pmg.io.vasp.Vasprun('%s/relax/vaspinput/vasprun.xml' % dirname)
    struct = pmg.Structure.from_file('%s/relax/vaspinput/vasprun.xml' % dirname)
    energies.append([dirname,struct.volume,run.final_energy])
np.save('energies.npy',energies)

energ = []

for i in np.load('energies.npy'):
    i[2] = i[2].replace(' eV', '')
    energ.append([i[0],i[1],float(i[2])])

np.save('energies.npy',energ)
