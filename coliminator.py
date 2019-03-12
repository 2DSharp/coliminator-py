""" 
Coliminator - The CSV duplicate column eliminator
Author - Dedipyaman Das (https://github.com/2dsharp)
"""
import csv
from collections import OrderedDict
import argparse

def removeDuplicate(row, output_file) :
    new_list = list(OrderedDict.fromkeys(row))
    with open(output_file, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(new_list)
    f.close()
    

parser = argparse.ArgumentParser("coliminator.py")
parser.add_argument("input_file", help="The input CSV file to eliminate columns from.", type=str)
parser.add_argument("output_file", help="The output CSV file to print the final results.", type=str)
args = parser.parse_args()

print("Reading from: " + args.input_file)
with open(args.input_file, 'rb') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            removeDuplicate(row, args.output_file)

print("Duplicates removed and written to: " + args.output_file)
csvDataFile.close()
