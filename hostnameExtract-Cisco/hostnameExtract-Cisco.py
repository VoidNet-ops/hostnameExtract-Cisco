"""
.SYNOPSIS
  A program which extracts Cisco hostnames from a single dump file.
  
.DESCRIPTION
  Digests lines from input file and exports individual hostnames that match start and end keys-terms into blank .txt files and a list .txt file. 
  Currently only searches for files in current directory.
  
.PARAMETER <Parameter_Name>
  None
    
.INPUTS
  session.log (Currently only searches in current directory)
  
.OUTPUTS
  ./hostOutput.txt
  ./hostOutput/*
  
.NOTES
  Version:        3.03
  Author:         Dennis Ozmert
  GitHub:         https://github.com/dozmert
  Creation Date:  28/09/2021 @ 9:00am
  Last Updated:   18/11/2021
  Purpose/Change: Device discovery
  License:        GNU General Public License
  
.EXAMPLE
  .\hostExtract-Cisco.py
 
.CITED WORK
  Generic works found on Google.
"""
# --------------------------------------------------
## Imports and values
import os
searchCmd = 'sh log' #key used to find the new config lines. Needs to be changed to regex for flexibility.
fileInput = open('session.log') #Source file
destDir = 'hostOutput' #Destination folder name
# --------------------------------------------------
## Functions
def outputDir(): 
    if os.path.exists(destDir):
        print('Destination directory already exists...')
    else:
        os.mkdir(destDir)
        print('Destination directoring being created...')
#
def hostExtract():
    print('Extracting hosts...')
    global runCount #Temporary method to track count of extracted configs
    runCount = 0
    listOutput = destDir+".txt" #Used to create list .txt
    listOutput = open(listOutput,'w+')  #Used to create list .txt
    for i in fileInput:
        if searchCmd in i:
            runCount += 1 #Found hosts counter
            printMask = i.index('#')
            hostFound = (i[:printMask]) #Used to create output files
            currentDir = os.getcwd()
            saveDir = '/'+str(destDir)+'/'
            nameDir = hostFound+'' #Used to append to end of filename
            compDir = os.path.join(currentDir+saveDir+nameDir+'.txt') #Final output composition
            fileOutput = open(compDir,'w+') #Used to create individual .txt
            fileOutput.close()  #Used to create individual .txt
            listOutput.write(hostFound+'\n')    #Used to create list .txt
    listOutput.close()  #Used to create list .txt
    return runCount
# --------------------------------------------------
## Code start
print('Program starting...')
outputDir()
hostExtract()
print(runCount,'Hosts found using','"'+searchCmd+'".')
print('Program ending.')
# --------------------------------------------------
