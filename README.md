# ordered_solvent

some tools used for modelling ordered solvent with LAMMPS

crin.py is used to convert the in.lmp produced by [fftool](https://github.com/agiliopadua/fftool) to the form we like, just three parts (pair_coeff, SHAKE, dump_modify) are changed 

xyz2gif is used to convert a series of coordinates (xyz format) to seperate input files of Gaussian/xtb/MOPAC. The xyz2gjf module of the [Molclus](http://www.keinsci.com/research/molclus.html) program is used here. Needs to be improved, too many files currently....
