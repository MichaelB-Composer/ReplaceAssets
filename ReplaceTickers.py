### ReplaceTickers.py
### Michael___B (Composer Discord)
### 1/7/2024
###
### Python script to replace assets in a symphony text file based
###  on "inputFiles" mapping csv files. One output text for every
###  input csv file.
###
###  

import csv

initialSymphony = 'TestSymphony.txt'

inputFiles = [
    'Mapping_EndOfYear',
    'Mapping_Main',
    'Mapping_IRA'
]

### No need to edit below this line

tempFile = 'temp.txt'
fname = initialSymphony.split(".")[0]


# Strip off new line character and double spaces
f = open(initialSymphony)
contents = f.read()
f.close()
new_contents = contents.replace('\n', '')
f = open(tempFile, 'w')
f.write(new_contents)
f.close()




for inputFile in inputFiles:
    csvFile = inputFile+'.csv'
    mainStr = inputFile.split("_")[-1]
    outputFile = fname+'_'+mainStr+'.txt'
    
    asset0 = []  
    asset1 = []

    with open(csvFile, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            asset0.append(row[0])
            asset1.append(row[1])

    with open(tempFile, "rt") as fin:
        with open(outputFile, "wt") as fout:
            for line in fin:
                newline = ' '.join(line.split())
                for idx, asset in enumerate(asset0):
                    str0 = 'asset "'+asset0[idx]+'"'
                    str1 = 'asset "'+asset1[idx]+'"'
                    newline = newline.replace(str0, str1)   
                fout.write(newline)



