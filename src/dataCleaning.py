#!/usr/bin/env python
"""module to format and merge csv files from soil and tissue nutrient analyses"""

import sys, csv, operator, re, os 

with open("../raw/4028_Sparks_NPK.csv","r") as fh: #open raw tissue nutrient analysis file 1 as a file object 
    NPK1 = fh.readlines()[15:] #read csv file without header

with open("../raw/7241-7245_Sparks_NPK.csv","r") as fh: #open raw tissue nutrient analysis file 2 as a file object 
    NPK2 = fh.readlines()[15:20] #read csv file without header

NPK = NPK1 + NPK2 #merge lists

with open("../cleaned/tissueNPK.csv", "w") as fout:
    fout.writelines(NPK) # write merged lists into a single, cleaned file  

data = csv.reader(open("../cleaned/tissueNPK.csv"), delimiter=",") # open cleaned tissue nutrient analysis file
data = [[item for item in row if item != ''] for row in data]
sortedlist = sorted(data, key=lambda x: int(re.search("\d+",x[1]).group())) #sort tissue nutrient data according to second column

with open("../cleaned/tissueNPK.csv", "w") as fout:
    fout.write("Microsite,Transect,TN,P,K\n") # write header
    filewriter = csv.writer(fout, delimiter=",")
    for row in sortedlist:
        filewriter.writerow( (row[1:]) ) # overwrite cleaned file with correctly sorted without lab number column

with open("../raw/PRS_results_for_W_Sparks_project_1632.csv","r") as fh: #open soil nutrient analysis file as a file object 
    NPK = fh.readlines()[6:] #read csv file without header

with open("../cleaned/soilNPK.csv", "w") as fout:
    fout.writelines(NPK) # write lists without messy header into cleaned file

data = csv.reader(open("../cleaned/soilNPK.csv"), delimiter=",") #reopen cleaned soil tissue data
sortedlist = sorted(data, key=lambda x: int(re.search("\d+",x[1]).group())) #sort data according to second column

with open("../cleaned/soilNPK.csv", "w") as fout:
    fout.write("Microsite,Transect,NO3,NH4,K,P\n") #write header
    filewriter = csv.writer(fout, delimiter=",")
    for row in sortedlist:
        filewriter.writerow( (row[1], row[7], row[8], row[11], row[12]) ) # overwrite cleaned file with only Transect, Microsite, nitrate, ammonium, phosphorus, and potassium data

with open("../raw/physical.csv", "r") as fh: # open raw file containing clay and height measurements
    Phys = fh.readlines()[1:] #read csv file without header

with open("../cleaned/physical.csv", "w") as fout: #write height and clay data without header
    fout.writelines(Phys)

data = csv.reader(open("../cleaned/physical.csv"), delimiter=",") # read cleaned height and clay file as csv
sortedlist = sorted(data, key=lambda x: int(re.search("\d+",x[1]).group())) #sort data according to second column


with open("../cleaned/physical.csv", "w") as fout:
    fout.write("Microsite, Transect, Clay_Depth, NumTowers, Height\n") #write header
    filewriter = csv.writer(fout, delimiter=",")
    for row in sortedlist:
        filewriter.writerow( (row[0], row[1], row[3], row[4], row[6]) ) # overwrite clay and height data with sorted data; exclude uncorrected height data and clay data measured in inches

with open("../cleaned/physical.csv", "r") as fh:
    physical = fh.read().splitlines()[1:] #read csv file without header
    phys = list(filter(None, ([row.split(',')[2:] for row in physical]))) #keep only height and clay data
    phys2 = [','.join(row) for row in phys]

with open("../cleaned/soilNPK.csv","r") as fh: #open energy file as a file object 
    soilNPK = fh.read().splitlines()[1:] #read csv file without header


#merge soil nutrient with clay and height data
with open("../cleaned/soilNPKphys.csv", "w") as fout:
    fout.write("Microsite,Transect,NO3,NH4,K,P, Clay_Depth, NumTowers, Height\n") #write header in $outfile
    r=0 #set values that will be used to index lists
    t=0
    q=0
    for row in physical:
        soilTransect = (re.search(r'\d+', soilNPK[r]).group(0)) #define transect number in $soilNPK list
        physTransect = (re.search(r'\d+', row).group(0)) #define transect number in $physical list
        soilSite = (re.search(r'[\+\-]', soilNPK[t]).group(0)) #define microsite in $soilNPK list
        physSite = (re.search(r'[\+\-]', row).group(0)) #define microsite in $physical list
        if soilTransect == physTransect and soilSite == physSite: # if transect and microsite match in $soilNPK and $physical
            fout.write(soilNPK[t]) #write current $soilNPK string
            fout.write(",")
            fout.write(phys2[q]) #write current $phys2 string
            fout.write("\n")
            t = t+1 #increase index by 1
            r = r+1
            q = q+1

#read height and clay file while omitting the data points that do not appear in tissue nutrient data 
with open("../cleaned/physical.csv", "r") as fh:
    physical1 = fh.read().splitlines()[1:27] #read csv file without header

with open("../cleaned/physical.csv", "r") as fh:
    physical2 = fh.read().splitlines()[28:30] #read csv file without header

with open("../cleaned/physical.csv", "r") as fh:
    physical3 = fh.read().splitlines()[31:] #read csv file without header

physical = physical1 + physical2 + physical3
phys = list(filter(None, ([row.split(',')[2:] for row in physical]))) #keep only height and clay data
phys2 = [','.join(row) for row in phys]

with open("../cleaned/tissueNPK.csv","r") as fh: #open cleaned tissue nutrient file 
    tissueNPK = fh.read().splitlines()[1:] #read csv file without header

#merge tissue nutrient data with clay and height data
with open("../cleaned/tissueNPKphys.csv", "w") as fout:
    fout.write("Microsite,Transect,TN,K,P, Clay_Depth, NumTowers, Height\n") #write header in $outfile
    r=0 #set value that will be used to index lists
    t=0
    q=0
    for row in physical:
        soilTransect = (re.search(r'\d+', tissueNPK[r]).group(0)) #define transect in $tissueNPK list
        physTransect = (re.search(r'\d+', row).group(0)) #define transect in $physical list
        soilSite = (re.search(r'[\+\-]', tissueNPK[t]).group(0)) #define dates in $energytimes list as $energydate
        physSite = (re.search(r'[\+\-]', row).group(0)) #define dates in temptimes list as $tempdate
        if soilTransect == physTransect and soilSite == physSite:
            fout.write(tissueNPK[t]) #write current $tissueNPK string
            fout.write(",")
            fout.write(phys2[q]) #write current $phys2 string
            fout.write("\n")
            t = t+1 #increase index by 1
            r = r+1
            q = q+1

os.remove("../cleaned/physical.csv)

