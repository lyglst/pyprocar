import pyprocar
import pdb
#pdb.set_trace()
pyprocar.fermi3D('PROCAR','OUTCAR',bands=[2,3,4,5],plotting_package='mayavi',mode='external',color_file='bsq.txt')
