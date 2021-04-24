# to prepeare the csv file for the cos\theta calculations. 

import re
import os
import glob

##remove extra information
allLine = []
with open("cluster_C6H11N2.xyz", "r") as sfile:
    with open("cluster_C8H15N2-deleted.xyz", "w") as tfile:
        for line in sfile:
            if 'Step ' in line:
                del line
            elif 'N ' in line:
                allLine.append(line.strip() + '\n')
            else:
                del line
        tfile.writelines(allLine)
        tfile.close()
    sfile.close()

##change useful atoms to O--for the visualization in VMD--not useful for multiple snapshots
#with open("cluster_C8H15N2-deleted.xyz", "r") as sfile:
#    with open("cluster_C8H15N2-deleted-replaced.xyz", "w") as tfile:
#        lines = sfile.readlines()
#        for i in range(2, 107500, 25):
#            lines[i]=re.sub("C","O",lines[i])
#        for j in range(24, 107500, 25):
#            lines[j]=re.sub("N","O",lines[j])
#        tfile.writelines(lines)
#        tfile.close()
#    sfile.close()

##removge extra information
#newallLine = []
#with open("cluster_C8H15N2-deleted-replaced.xyz", "r") as sfile:
#    with open("cluster_C8H15N2-deleted-replaced-cleaned.xyz", "w") as tfile:
#        for line in sfile:
#            if 'O ' in line:
#                newallLine.append(line.strip() + '\n')
#        tfile.writelines(newallLine)
#        tfile.close()
#    sfile.close()


