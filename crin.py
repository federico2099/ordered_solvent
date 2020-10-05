#======convert the in.lmp produced by fftool to the form we like======
#======To Use: python3 crin.py=======

import os
import sys
import argparse
import shutil 
import fileinput
import re

#======copy template file======
name = input("the name of the job is :")
old_lmp = '/scratch/x69/lx3539/file/template'
old_pbs = '/scratch/x69/lx3539/file/template.pbs'
shutil.copy(old_lmp, name + '.lmp')
shutil.copy(old_pbs, name + '.pbs')

#======replacing string======
list = ["lmp", "pbs"]
for i in list:
    fin = open(name + '.' + i, "r")
    data = fin.read()
    data = data.replace('template', name)
    fin.close()
    fin = open(name + '.' + i, "w")
    fin.write(data)
    fin.close()

#======replacing pair_coeff part======
FA = open('in.lmp', 'r')
str = '\n'
allLine = []
for line in FA:
    if 'pair_coeff' in line:
        str += line.strip() + '\n'
        allLine.append(line.strip() + '\n')
    else:
        allLine.append('')
FA.close()
FB = open(name + '.lmp', 'r')
data = FB.read()
data = data.replace('pair_coeff_placeholder', str)
FB.close()
FB = open(name + '.lmp', 'w')
FB.write(data)
FB.close()

#======replacing fix SHAKE part======
FA = open('in.lmp', 'r')
str = '\n'
allLine = []
for line in FA:
    if 'SHAKE' in line:
        str += line.strip() + '\n'
        allLine.append(line.strip() + '\n')
    else:
        allLine.append('')
FA.close()
FB = open(name + '.lmp', 'r')
data = FB.read()
data = data.replace('SHAKE_placeholder', str)
FB.close()
FB = open(name + '.lmp', 'w')
FB.write(data)
FB.close()

#======replacing dump_modify part======
FA = open('in.lmp', 'r')
str = '\n'
allLine = []
for line in FA:
    if 'dump_modify' in line:
        str += line.strip() + '\n'
        allLine.append(line.strip() + '\n')
    else:
        allLine.append('')
FA.close()
FB = open(name + '.lmp', 'r')
data = FB.read()
data = data.replace('dump_modi_placeholder', str)
FB.close()
FB = open(name + '.lmp', 'w')
FB.write(data)
FB.close()

