from vaspwfc import vaspwfc
import numpy as np
import pymatgen
import pymatgen as mg
from pymatgen.io.vasp import inputs
from pymatgen.io.vasp import outputs
from pymatgen.symmetry import bandstructure as bs


def get_b(ak,bk):
    norm=np.sum([np.abs(ak[i])**2+np.abs(bk[i])**2 for i in range(len(ak))])
    Sx=np.sum([ak[i]*np.conj(bk[i])+bk[i]*np.conj(ak[i]) for i in range(len(ak))])/norm
    Sy=np.sum([ak[i]*np.conj(bk[i])-bk[i]*np.conj(ak[i]) for i in range(len(ak))])/norm
    Sz=np.sum([np.abs(ak[i])**2-np.abs(bk[i])**2 for i in range(len(ak))])/norm
    b=(1-np.sqrt(np.abs(Sx)**2+np.abs(Sy)**2+np.abs(Sz)**2))/2
    return b

def generate_b(wavecar,filename,bands):
    wav=vaspwfc(wavecar,lsorbit=True)
    data_r=[[wav.readBandCoeff(ikpt=ikpt+1,iband=iband+1,norm=False) for ikpt in range(wav._nkpts)] for iband in range(wav._nbands)]
    b=[[get_b(data_r[iband][ikpt][:int(len(data_r[iband][ikpt])/2)],data_r[iband][ikpt][int(len(data_r[iband][ikpt])/2):]) for ikpt in range(wav._nkpts)] for iband in bands]
    dk=[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
    with open(filename,'w') as f:
        for iband in range(len(bands)):
            f.write("band = "+str(iband+1)+"\n")
            for idk in dk:
                for ikpt in range(wav._nkpts):
                    s='%5.3f %5.3f %5.3f %.12f'%(wav._kvecs[ikpt][0]+idk[0],wav._kvecs[ikpt][1]+idk[1],wav._kvecs[ikpt][2]+idk[2],b[iband][ikpt])+'\n'
                    f.write(s)

