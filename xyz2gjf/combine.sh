#to insert column.txt to the end column of test.gjf and save it to test-modi.gjf

for i in {001..110}
do
	paste ts-il-drude-000$i.gjf column.txt | awk '{$10=""; print}' > ts-il-drude-000$i-modi.gjf
	cp template.pbs ts-il-drude-000$i-modi.pbs
done

