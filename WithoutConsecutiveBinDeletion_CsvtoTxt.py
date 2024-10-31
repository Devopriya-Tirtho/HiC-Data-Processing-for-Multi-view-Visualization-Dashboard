
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:53:48 2024

@author: Hp
"""

import csv

text_check='linear'

input_file_name = 'GSM1671431_33_Rudnerlab_HindIII_HiC_BNS1733_42C120m.matrix.csv'  # Replace with your actual input file path
output_file_name = 'Basillus_GSM1671431_33_Rudnerlab_HindIII_HiC_BNS1733_42C120m.matrix.txt'  # Name for the new processed file (with .txt extension)

# Function to determine if source and target are consecutive
#def are_consecutive(source, target):
#    return int(target) == int(source) + 1

# Read the input file and write to the output file
with open(input_file_name, mode='r') as infile, open(output_file_name, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Source', 'Target', 'Weight']  # Define the fieldnames to be written to the output
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    
    writer.writeheader()
    for row in reader:
        # Check if source and target are consecutive and interaction_type is not 'linear'
        #if not (are_consecutive(row['Source'], row['Target']) and text_check not in row['interaction_type']):
            # Write row without interaction_type column
        writer.writerow({'Source': int(row['Source']), 'Target': int(row['Target']), 'Weight': float(row['Weight'])})
        #if  (row['interaction_type'] =='linear1' or row['interaction_type'] =='linear2' or row['interaction_type'] =='linear3'):
            # Write row without interaction_type column
            #writer.writerow({field: row[field] for field in fieldnames})
print(f"Processed data written to {output_file_name}")
