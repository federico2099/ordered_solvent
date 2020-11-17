# ordered_solvent

some tools used for modelling ordered solvent and ionic liquids with LAMMPS

crin.py is used to prepare the input files for LAMMPS using the information in the in.lmp, data.lmp, data-p.lmp files produced by [fftool](https://github.com/agiliopadua/fftool) and add the information of the external electric field, to use, just ```python3 crin.py```and provide the information accordingly. 

--- below is still under construction---
xyz2gif is used to convert a series of coordinates (xyz format) to seperate input files of Gaussian/xtb/MOPAC. The xyz2gjf module of the [Molclus](http://www.keinsci.com/research/molclus.html) program is used here. Needs to be improved, too many files currently....
