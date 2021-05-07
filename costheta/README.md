## costheta

### This is the tool used to calculate the angles between the dipole moment of each ions and the external electric field. 

#### In each folder, input.txt, delete.py and a jupyter notebook is provided.

#### Usage:
**Step1:** `travis -p traj-EMIM-ESO4-E2-NVT.lmp -i input.txt` ## This is used to extact the molecules from the MD trajectory.

**Step2:** `python3 delete.py` ## This is used to exact the coordinates of the used atoms.

**Step3:** `cp cluster_C8H15N2-deleted.xyz cluster_C8H15N2-deleted.csv; sed -i -e "s/\  /,/g" cluster_C8H15N2-deleted.csv` ## This is to change xyz to csv. 

**Step4:** use the jupyter notebook in each folder to calculate the average $cos\theta$ and $\theta$.

#### If you have any question, feel free to email me `Longkun.Xu@anu.edu.au`
