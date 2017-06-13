#!/bin/bash
set -e # script terminates if any command exits with non-zero status
set -u # terminates if any variable is unset
set -o pipefail # terminates if command within a pipes exits unsuccessfully
# separate transect number and inside/outside treatment into different columns
#Utilize: ./fixsampleid.sh
for file in /home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/soilNPK.csv
do
	Labels=$(head -1 $file)
	sed -nr 's/#[0-9]+//p' $file >> $file
        Filetail1=$(tail -n8 $file | head -n4)
	Filetail2=$(tail -n4 $file | head -n2)
	Filetail3=$(tail -n2 $file)
	Filehead1=$(head -n22 $file)
	Filehead2=$(head -n27 $file | tail -n1)
	Filehead3=$(head -n30 $file | tail -n1) 
	echo -e "$Filehead1" > $file
	echo -e "$Filetail1" >> $file
	echo -e "$Filehead2" >> $file
	echo -e "$Filetail2" >> $file
	echo -e "$Filehead3" >> $file
	echo -e "$Filetail3" >> $file 
	Fixedtable=$(sed -rn 's/(pp)([+-])([0-9]+)/\2,\3/p' $file)
	echo -e "$Labels" > $file
	for row in $Fixedtable
	do
		echo -e "$row" >> $file
	done 
done

IFS=$(echo -en "\t\n\0")

for file in /home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/tissueNPK.csv
do
        Labels=$(head -1 $file)
	sed -nr 's/#[0-9]+//p' $file >> $file
	Filetail1=$(tail -n6 $file | head -n4)
        Filetail1new=$(echo -e "$Filetail1" | sed -nr 's/([0-9]) (,)/\1\2/p')
        Filetail2=$(tail -n2 $file | head -n1)
        Filetail3=$(tail -n1 $file)
	Filetail3new=$(echo -e "$Filetail3" | sed -nr 's/([0-9]) (,)/\1\2/p')
        Filehead1=$(head -n22 $file)
        Filehead2=$(head -n27 $file | tail -n1)
        Filehead3=$(head -n29 $file | tail -n1) 
        echo -e "$Filehead1" > $file
        echo -e "$Filetail1new" >> $file
        echo -e "$Filehead2" >> $file
        echo -e "$Filetail2" >> $file
        echo -e "$Filehead3" >> $file
        echo -e "$Filetail3new" >> $file 
        Fixedtable=$(sed -rn 's/(pp)([+-])([0-9]+)/\2,\3/Ip' $file)
	echo -e "$Fixedtable"
        echo -e "$Labels" > $file
        for row in $Fixedtable
        do
                echo -e "$row" >> $file
        done 
done

