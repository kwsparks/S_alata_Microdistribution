#!/bin/bash
set -e # script terminates if any command exits with non-zero status
set -u # terminates if any variable is unset
set -o pipefail # terminates if command within a pipes exits unsuccessfully
# separate transect number and pitcher-present/pitcher-absent microsite into different columns and correctly sort transect number 
#Utilize: ./fixsampleid.sh
for file in ../cleaned/soilNPK.csv # operate on cleaned soil data
do
	Labels=$(head -1 $file) # create header list
	sed -nr 's/#[0-9]+//p' $file >> $file #append new column with microsite data to file
        Filetail1=$(tail -n8 $file | head -n4) # create list representing data sorted in correct order
	Filetail2=$(tail -n4 $file | head -n2)
	Filetail3=$(tail -n2 $file)
	Filehead1=$(head -n22 $file)
	Filehead2=$(head -n27 $file | tail -n1)
	Filehead3=$(head -n30 $file | tail -n1) 
	echo -e "$Filehead1" > $file # write correctly sorted lists to file
	echo -e "$Filetail1" >> $file
	echo -e "$Filehead2" >> $file
	echo -e "$Filetail2" >> $file
	echo -e "$Filehead3" >> $file
	echo -e "$Filetail3" >> $file 
	Fixedtable=$(sed -rn 's/(pp)([+-])([0-9]+)/\2,\3/p' $file) # create a list with a comma between microsite and transect data
	echo -e "$Labels" > $file # write header
	for row in $Fixedtable
	do
		echo -e "$row" >> $file # write list with separate transect and microsite data to file
	done 
done

IFS=$(echo -en "\t\n\0") # set IFS to ignore splitting at spaces

for file in ../cleaned/tissueNPK.csv # operate on cleaned tissue nutrient data
do
        Labels=$(head -1 $file) # create header list
	sed -nr 's/#[0-9]+//p' $file >> $file
	Filetail1=$(tail -n6 $file | head -n4) # create list of correctly sorted data
        Filetail1new=$(echo -e "$Filetail1" | sed -nr 's/([0-9]) (,)/\1\2/p') # delete space between transect number and comma
        Filetail2=$(tail -n2 $file | head -n1)
        Filetail3=$(tail -n1 $file)
	Filetail3new=$(echo -e "$Filetail3" | sed -nr 's/([0-9]) (,)/\1\2/p')
        Filehead1=$(head -n22 $file)
        Filehead2=$(head -n27 $file | tail -n1)
        Filehead3=$(head -n29 $file | tail -n1) 
        echo -e "$Filehead1" > $file # write correctly sorted data to file
        echo -e "$Filetail1new" >> $file
        echo -e "$Filehead2" >> $file
        echo -e "$Filetail2" >> $file
        echo -e "$Filehead3" >> $file
        echo -e "$Filetail3new" >> $file 
        Fixedtable=$(sed -rn 's/(pp)([+-])([0-9]+)/\2,\3/Ip' $file) # delete pp before transect data
	echo -e "$Fixedtable"
        echo -e "$Labels" > $file # write header
        for row in $Fixedtable
        do
                echo -e "$row" >> $file # write corrected data to file
        done 
done

