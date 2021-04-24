# to prepeare the csv file for the cos\theta calculations. 

import re
import os
import glob

##remove extra information
allLine = []
with open("cluster_C2H5O4S.xyz", "r") as sfile:
    with open("cluster_C2H5O4S-deleted.xyz", "w") as tfile:
        for line in sfile:
            if 'Step ' in line:
                del line
            elif 'C ' in line:
                allLine.append(line.strip() + '\n')
            elif 'S ' in line:
                allLine.append(line.strip() + '\n')
            else:
                del line
        tfile.writelines(allLine)
        tfile.close()
    sfile.close()

##change useful atoms to O--for the visualization in VMD--not useful for multiple snapshots
with open("cluster_C2H5O4S-deleted.xyz", "r") as sfile:
    with open("cluster_C2H5O4S-deleted.xyz-replaced.xyz", "w") as tfile:
        lines = sfile.readlines()
        for i in range(0, 14400, 3):
            lines[i]=re.sub("C","O",lines[i])
        for j in range(2, 14400, 3):
            lines[j]=re.sub("S","O",lines[j])
        tfile.writelines(lines)
        tfile.close()
    sfile.close()

##removge extra information
newallLine = []
with open("cluster_C2H5O4S-deleted.xyz-replaced.xyz", "r") as sfile:
    with open("cluster_C2H5O4S-deleted.xyz-replaced-cleaned.xyz", "w") as tfile:
        for line in sfile:
            if 'O ' in line:
                newallLine.append(line.strip() + '\n')
        tfile.writelines(newallLine)
        tfile.close()
    sfile.close()


