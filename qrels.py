"""qrels.py: It simply formats qrels for terrier evaluation."""

__author__      = "John Moras"
__website__ = "https://moras.gr"
__email__ = "john@moras.gr"
__copyright__   = "Copyright 2020, Thessaloniki , Greece"


import os
import sys 
import argparse


#specify arguments for the script
parser = argparse.ArgumentParser()
parser.add_argument("-i","--inputfile",dest="inputFile", help='Input file to read')
parser.add_argument("-o","--outputfile",dest="outputFile",default="qrels-out.txt",help='Output file to store modified data')
parser.add_argument("-s","--seperator",dest="seperator",default = "\t",help="Specify the seperator between fields")
parser.add_argument("-n","--newseperator",dest="newsperator",default=" 0 ",help="New seperator between fields")
parser.add_argument('-sc',"--seperatorcount",dest="seperatorcount",default=1,help="Seperate nth fields starting from left")

args = parser.parse_args()

#create a list to store new qrels
qrelsFormatted = []

if args.inputFile != '':  
    #check if input file exists
    if not os.path.isfile(args.inputFile):
       print("File path {} does not exist. Exiting...".format(args.inputFile))
       sys.exit()
    
    with open(args.inputFile) as fp:       
       for line in fp:
           if args.seperator != "" and args.seperatorcount > 0:
               newline = line.replace(args.seperator,str(args.newsperator),args.seperatorcount)
               qrelsFormatted.append(newline)                                 
           else:
               print('Error for info check -h option')
    print(qrelsFormatted) 
else:
    print('Error for info check -h option')

if args.outputFile != '':
    with open(args.outputFile, 'w') as filehandle:
        for qrelitem in qrelsFormatted:
            filehandle.write(qrelitem)
