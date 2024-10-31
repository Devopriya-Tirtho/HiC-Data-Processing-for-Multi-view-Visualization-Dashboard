# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:29:56 2024

@author: Hp
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:41:57 2024

@author: Hp
"""

import csv



# Predefined variables
hic_file = 'GSM1671431_33_Rudnerlab_HindIII_HiC_BNS1733_42C120m.matrix.txt'  # Replace with your Hi-C data file path
# Open the interaction matrix file and read its content
with open(hic_file, 'r') as file:
    hic_matrix = [line.strip().split(',') for line in file.readlines()]

# Debugging: Print first few lines to check format
#for i, line in enumerate(hic_matrix[:5]):
#    print(f"Line {i}: {line} - Columns: {len(line)}")

num_nodes = 404  # Replace with the actual number of nodes
#num_nodes = 1258  # Replace with the actual number of nodes
num_chr = 1  # Replace with the actual number of chromosomes
#num_chr = 3  # Replace with the actual number of chromosomes
linear_freq = 10000  # Linear frequency value
scale = 1.0  # Scaling factor for interaction frequency
out_file_name = 'GSM1671431_33_Rudnerlab_HindIII_HiC_BNS1733_42C120m.matrix.csv'  # Output CSV file

# Chromosome start and end positions - Replace with actual values
#chr_start = [1, 559, 1013]  # Example start positions
chr_start = [1]
#chr_stop = [558, 1012, 1258]  # Example end positions
chr_stop = [404]
# Open the output file for writing in CSV format
with open(out_file_name, 'w', newline='') as out_file:
    csv_writer = csv.writer(out_file, delimiter=',')
    # Write the header for Gephi
    csv_writer.writerow(["Source", "Target", "interaction_type", "Weight"])
    csv_writer.writerow([1, 404, f"linear1", 10000.0])
    # For each chromosome
    for chr_num in range(1, num_chr + 1):
        for j in range(chr_start[chr_num - 1], chr_stop[chr_num - 1]):
            # Write linear interactions for Gephi
            csv_writer.writerow([j, j+1, f"linear{chr_num}", linear_freq])

# Open the interaction matrix file and read its content

with open(hic_file, 'r') as file:
    hic_matrix = [line.strip().split(',') for line in file.readlines()]


# Convert the decimals to integers and store them in a new list



# For each line after the header line in hic_matrix
frequencies = [[0] * num_nodes for _ in range(num_nodes)]

# For each line in hic_matrix
for row in range(len(hic_matrix)):
    matrix_line = hic_matrix[row]

    # Check if the line has the expected number of columns
    if len(matrix_line) != num_nodes:
        raise ValueError(f"Row {row + 1} in hic_matrix does not have the expected number of columns. Found {len(matrix_line)} columns.")

    for col in range(1, num_nodes):
        value = matrix_line[col]
        adjusted_row_index = row   # Adjusting for 0-based index
        adjusted_col_index = col   # Adjusting for skipped first column
        try:
            frequencies[adjusted_row_index][adjusted_col_index] = 0 if value == "NA" else float(value) * scale
        except IndexError:
            raise IndexError(f"Index error at row {row}, col {col} (adjusted indices: {adjusted_row_index}, {adjusted_col_index})")


# Append non-linear interactions to the CSV file
with open(out_file_name, 'a', newline='') as out_file:
    csv_writer = csv.writer(out_file, delimiter=',')
    for row in range(len(frequencies)):
        for col in range(row + 1, len(frequencies)):
            if frequencies[row][col] != 0:
                # Adjust for zero-based index by adding 1 for chromosome number determination
                source_chr = next((i + 1 for i, stop in enumerate(chr_stop) if row <= stop), None) + 1
                sink_chr = next((i + 1 for i, stop in enumerate(chr_stop) if col <= stop), None) + 1
                interaction_type = "intra-interaction" if source_chr == sink_chr else "inter-interaction"
                # Write to CSV, ensuring chromosomes are numbered from 1 to 404
                csv_writer.writerow([row+1, col+1, interaction_type, frequencies[row][col]])

