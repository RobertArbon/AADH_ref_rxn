from ase import io
from ase.neb import NEB
from ase.optimize import MDMin, BFGS
from ase.calculators.dftb import Dftb 
import copy

calc = Dftb(label='neb_path1',
Hamiltonian_MaxAngularMomentum_='',
Hamiltonian_MaxAngularMomentum_O='"p"',
Hamiltonian_MaxAngularMomentum_H='"s"',
Hamiltonian_MaxAngularMomentum_C='"p"',
Hamiltonian_MaxAngularMomentum_N='"p"')

all = io.Trajectory('../common/kr_geoms.traj')
initial = all[0]
final = all[6]
#initial.set_calculator(calc=calc)
#final.set_calculator(calc=calc)

#print(len(all))
#print(initial.get_positions())
#print(final.get_positions())
#images = [all[0]]
#for i in range(1,7):
#    images += [all[i]]

images = [initial]
images += [copy.deepcopy(initial) for i in range(3)]
images += [final]

neb = NEB(images, k=0.01)

# Interpolate linearly the potisions of the three middle images:
neb.interpolate()
io.write('initial_guess.pdb', images, format='pdb')

# Set calculators:
for image in images[1:4]:
    image.set_calculator(calc=calc)
    e = image.get_potential_energy()
    forces = image.get_forces()
    f = (forces**2).sum(axis=1).sum(axis=0)
    print('e = {0:10.5f}, f = {1:10.5f}'.format(e, f))
# Optimize:
optimizer = BFGS(neb, trajectory='path1.traj')
optimizer.run(fmax=0.04)
