from charmmutils import charmmutils as chm
import pandas as pd

data = chm.Energy('1-as-solvated-neut-min-310k.ene')

df = data.energies

df.to_csv('output')





