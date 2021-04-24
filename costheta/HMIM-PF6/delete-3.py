# to prepeare the csv file for the cos\theta calculations. 

import re
import os
import glob


##removge extra information
newallLine = []
with open("cluster_C10H19N2-deleted-replaced.xyz", "r") as sfile:
    with open("cluster_C10H19N2-deleted-replaced-cleaned.xyz", "w") as tfile:
        for line in sfile:
            if 'O ' in line:
                newallLine.append(line.strip() + '\n')
        tfile.writelines(newallLine)
        tfile.close()
    sfile.close()


