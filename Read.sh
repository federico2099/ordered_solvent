#read the energy of ONIOM results
for i in *-modi.log
do
	grep "ONIOM: extrapolated energy =   " $i
done

