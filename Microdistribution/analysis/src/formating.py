
# coding: utf-8

# In[ ]:

#!/usr/bin/env python
"""module to format and merge csv files based on nutrient analysis"""


# In[11]:

import sys, csv, operator, re

with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/raw/4028_Sparks_NPK.csv","r") as fh: #open energy file as a file object 
    NPK1 = fh.readlines()[15:] #read csv file without header
    
with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/raw/7241-7245_Sparks_NPK.csv","r") as fh: #open energy file as a file object 
    NPK2 = fh.readlines()[15:20] #read csv file without header
    
NPK = NPK1 + NPK2 #merge lists

with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/tissueNPK.csv", "w") as fout:
    fout.writelines(NPK)   

data = csv.reader(open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/tissueNPK.csv"), delimiter=",") 
data = [[item for item in row if item != ''] for row in data]
sortedlist = sorted(data, key=lambda x: int(re.search("\d+",x[1]).group())) #sort according to second column

with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/tissueNPK.csv", "w") as fout:
    fout.write("Microsite,Transect,TN,P,K\n")
    filewriter = csv.writer(fout, delimiter=",")
    for row in sortedlist:
        filewriter.writerow( (row[1:]) )


# In[12]:

import sys, csv, operator, re

with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/raw/PRS_results_for_W_Sparks_project_1632.csv","r") as fh: #open energy file as a file object 
    NPK = fh.readlines()[6:] #read csv file without header
    
with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/soilNPK.csv", "w") as fout:
    fout.writelines(NPK)  

data = csv.reader(open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/soilNPK.csv"), delimiter=",") 
sortedlist = sorted(data, key=lambda x: int(re.search("\d+",x[1]).group())) #sort according to second column

with open("/home/sparks/Desktop/Thesis_Projects/Microdistribution/analysis/cleaned/soilNPK.csv", "w") as fout:
    fout.write("Microsite,Transect,NO3,NH4,K,P\n")
    filewriter = csv.writer(fout, delimiter=",")
    for row in sortedlist:
        filewriter.writerow( (row[1], row[7], row[8], row[11], row[12]) )
 


# In[ ]:



