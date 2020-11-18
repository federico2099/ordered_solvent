#A script used to prepare the input file of LAMMPS
#To Use: python3 crin.py
#Author: Longkun Xu (https://longkunxuluke.github.io/)
#Updated time: 9 Oct 2020

import os
import sys
import argparse
import shutil 
import fileinput
import re
import inspect

#copy template file
name = input("the name of the job is :")
jobtype = input("the type of the job is [1] NPT [2] NVT [3] NPT-pol [4] NVT-pol :")
Fieldstrrength = input("the strrength of external electric field is [unit in V/angstrrom, along z direction] :")

if jobtype == "1":
    old_lmp = '/scratch/x69/lx3539/file/template'
if jobtype == "2":
    old_lmp = '/scratch/x69/lx3539/file/template-2'
if jobtype == "3":
    old_lmp = '/scratch/x69/lx3539/file/template-3'
if jobtype == "4":
    old_lmp = '/scratch/x69/lx3539/file/template-4'
old_pbs = '/scratch/x69/lx3539/file/template.pbs'

shutil.copy(old_lmp, name + '.lmp')
shutil.copy(old_pbs, name + '.pbs')

#replacing template strring
list = ["lmp", "pbs"]
for i in list:
    fin = open(name + '.' + i, "r")
    data = fin.read()
    data = data.replace('template', name)
    data = data.replace('Fieldstrength', Fieldstrrength)
    fin.close()
    fin = open(name + '.' + i, "w")
    fin.write(data)
    fin.close()

#replacing pair_coeff part
if jobtype == "1" or "2":
    FA = open('in.lmp', 'r')
    strr = '\n'
    allLine = []
    for line in FA:
        if 'pair_coeff' in line:
            strr += line.strip() + '\n'
            allLine.append(line.strip() + '\n')
        else:
            allLine.append('')
    FA.close()
    FB = open(name + '.lmp', 'r')
    data = FB.read()
    data = data.replace('pair_coeff_placeholder', strr)
    FB.close()
    FB = open(name + '.lmp', 'w')
    FB.write(data)
    FB.close()

#replacing fix SHAKE part
FA = open('in.lmp', 'r')
strr = '\n'
allLine = []
for line in FA:
    if 'SHAKE' in line:
        strr += line.strip() + '\n'
        allLine.append(line.strip() + '\n')
    else:
        allLine.append('')
FA.close()
FB = open(name + '.lmp', 'r')
data = FB.read()
data = data.replace('SHAKE_placeholder', strr)
FB.close()
FB = open(name + '.lmp', 'w')
FB.write(data)
FB.close()

#replacing dump_modify part
if jobtype == "1" or "2":
    FA = open('in.lmp', 'r')
    strr = '\n'
    allLine = []
    for line in FA:
        if 'dump_modify' in line:
            strr += line.strip() + ''
    FA.close()
    FB = open(name + '.lmp', 'r')
    data = FB.read()
    data = data.replace('dump_modi_placeholder', strr)
    FB.close()
    FB = open(name + '.lmp', 'w')
    FB.write(data)
    FB.close()

#removing elfield line if no external electric field
#if Fieldstrrength == "0":
#    with open(name + '.lmp') as oldfile, open(name + '-new.lmp', 'w') as newfile:
#       for line in oldfile:
#            if not 'efield' in line:
#                newfile.write(line)
#    shutil.copy(name + '.pbs', name + '-new.pbs')
#    print("please qsub the new pbs file")

#count the occurences of drude particles in 'Masses' 
if jobtype == "3" or "4":
    datap = open('data-p.lmp', 'r')
    occurences = 0
    for line in datap:
        if 'DP' in line:
            occurences = occurences + 1
        if 'Bond Coeffs' in line:
            break
    datap.close()

#changing the fix DRUDE part
if jobtype == "3" or "4":
    datap = open('data-p.lmp', 'r')
    fix_DRUDE = 'fix DRUDE all drude '
    for line in datap:
        if 'DC' in line:
            fix_DRUDE = fix_DRUDE + 'C '
        if 'DP' in line:
            fix_DRUDE = fix_DRUDE + 'D '
        if '# H' in line:
            fix_DRUDE = fix_DRUDE + 'N '
        if 'Bond Coeffs' in line:
            break
    FB = open(name + '.lmp', 'r')
    data = FB.read()
    data = data.replace('fix_DRUDE_placeholder', fix_DRUDE)
    FB.close()
    FB = open(name + '.lmp', 'w')
    FB.write(data)
    FB.close()
    datap.close()

#counting the number of different atoms 
groupatoms = " "
groupcores = " "
groupdrudes = " "
if jobtype == "3" or "4":
    line_number = 0
    datap = open('data-p.lmp', 'r')
    for line in datap:
            line_number += 1
            if '#' in line:
                groupatoms = groupatoms + " " + str(line_number - 16)
            if 'DC' in line:
                groupcores = groupcores + " " + str(line_number - 16)
            if 'DP' in line:
                groupdrudes = groupdrudes + " " + str(line_number - 16)
            if 'Bond Coeffs' in line:
                break
    FB = open(name + '.lmp', 'r')
    data = FB.read()
    data = data.replace('group-atoms-placeholder', groupatoms)
    data = data.replace('group-cores-placeholder', groupcores)
    data = data.replace('group-drudes-placeholder', groupdrudes)
    FB.close()
    FB = open(name + '.lmp', 'w')
    FB.write(data)
    FB.close()
    datap.close()

#dump_modify part of the polarizable force field
if jobtype == "3" or "4":
    FA = open('in.lmp', 'r')
    strr = '\n'
    allLine = []
    for line in FA:
        if 'dump_modify' in line:
            strr += line.strip() + ''
    FA.close()
    strr = strr + " D" * occurences
    FB = open(name + '.lmp', 'r')
    data = FB.read()
    data = data.replace('dump_modi_placeholder', strr)
    FB.close()
    FB = open(name + '.lmp', 'w')
    FB.write(data)
    FB.close()

