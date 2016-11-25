import ase.io as io
from ase import Atom, Atoms
import numpy as np
from ase.calculators.nwchem import NWChem
from ase.calculators.dftb import Dftb 
from ase.calculators.emt import EMT
import os
from ase.units import *

def import_pdb(atom_col, file_name):
    """
    Imports a pdb
    """
    filen = open(file_name, 'r')
    orig = np.identity(3)
    trans = np.zeros(3)
    
    for line in filen.readlines():
        if line.startswith('ATOM') or line.startswith('HETATM'):
            try:
                # Only dealing with H, C, O and N so single letter for symbol 
                symbol = line[13].strip().lower().capitalize()
                words = line[30:55].split()
                position = np.array([float(words[0]),
                                     float(words[1]),
                                     float(words[2])])
                position = np.dot(orig, position) + trans
                atoms.append(Atom(symbol, position))
            except:
                pass
    return(atom_col)
    
#calc = NWChem(label='calc/nwchem',
#              maxiter=2000,
#              xc='B3LYP',
#              basis='6-31+G*', 
#              task='energy', 
#              charge=0)
#

energies = []
for i in range(1,8):
    atoms = Atoms()
    atoms = import_pdb(atoms, '../../common/{}-as.pdb'.format(i))
    atoms.set_calculator(Dftb(label='AS_path1', 
                                  atoms=atoms,
                                  Hamiltonian_MaxAngularMomentum_='',
                                  Hamiltonian_MaxAngularMomentum_O='"p"',
                                  Hamiltonian_MaxAngularMomentum_H='"s"',
                                  Hamiltonian_MaxAngularMomentum_C='"p"',
                                  Hamiltonian_MaxAngularMomentum_N='"p"'
                  ))
    energies.append(atoms.get_potential_energy())

norm = energies[0]
for i in range(len(energies)):
    energies[i] = (energies[i]-norm)*mol/kcal

for x in energies:
    print x
