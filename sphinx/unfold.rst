Band unfolding
==============

Often times, we need to perform DFT calculations for a supercell geometry rather than the primitive cell. In such cases the band structure becomes quite sophisticated due to the folding of the BZ, and it is difficult to compare the band structure of supercell with that of the primitive cell. The purpose of the band unfolding scheme is to represent the bands within the primitive cell BZ. By calculating the unfolding weight function and plotting the fat bands with the line width proportional to the weight, the unfolded bands can be highlighted. 

Note:
The Brillouin zone of a supercell shrinks respect to the primitive cell. For instance, in a hexagonal primitive lattice the point  H=(1/3, 1/3, 1/2). This point, in a 2x2x2 supercell corresponds to (2/3, 2/3, 1). Therefore, all the distances in the reciprocal space must be doubled (or increased by the respective size of the supercell).


Usage:
First, calculate the band structure in the primitive cell BZ. The PROCAR should be produced with the phase factor included, by setting ``LORBIT=12`` in VASP.

Then the unfold module can be used to plot the unfolded band as follows::

	import numpy as np
	pyprocar.unfold(
	        fname='PROCAR',
	        poscar='POSCAR',
	        outcar='OUTCAR',
	        supercell_matrix=np.diag([2, 2, 2]),
	        efermi=None,
	        shift_efermi=True,
	        elimit=(-5, 15),
	        kticks=[0, 36, 54, 86, 110, 147, 165, 199],
	        knames=['$\Gamma$', 'K', 'M', '$\Gamma$', 'A', 'H', 'L', 'A'],
	        print_kpts=False,
	        show_band=True,
	        savefig='unfolded_band.png')