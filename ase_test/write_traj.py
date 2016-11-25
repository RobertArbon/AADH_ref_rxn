import ase.io as io
from ase import Atom, Atoms
import numpy as np
import os

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

traj = io.Trajectory(filename='./common/kr_geoms.traj', mode='w')

for i in range(1,71):
    atoms = Atoms()
    atoms = import_pdb(atoms, '../common/{}-as.pdb'.format(i))
    traj.write(atoms=atoms)





	 

