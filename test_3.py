import pyprocar
import pdb
#pdb.set_trace()
pyprocar.bandsplot('PROCAR_2',outcar='OUTCAR_2',fermi=8.02,kticks=[0,119,239,359],knames=['G','X','W','K'],mode='parametric',spin='b',external_file='bsq_2.txt',vmin=-11,vmax=0)
#pyprocar.bandsplot('PROCAR_3',outcar='OUTCAR_3',fermi=8.20,kticks=[0,39,79,119],knames=['G','X','W','K'],mode='plain',elimit=[-11,16])
