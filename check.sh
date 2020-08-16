#check which jobs failed
for i in *.log
do
	grep "Normal termination " $i
	echo $i
done


