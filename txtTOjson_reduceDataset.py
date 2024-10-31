# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:30:16 2024

@author: Hp
"""

import json
import csv

def generate_top_weights_csv(inter_chromosomal_links, csv_file_path):
    # Exclude weights of 10000.0 and sort the rest
    filtered_links = [link for link in inter_chromosomal_links if link[2] != 10000.0]
    filtered_links.sort(key=lambda x: x[2], reverse=True)  # Sort by weight in descending order
    
    # Take the top 100 weights
    top_100_links = filtered_links[:1000]
    
    
    #chr_start = [1,285,493,548]

#chr_stop = [284,492,547,568]
    # Write to CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Source", "Target", "Weight"])
        for src, tgt, val in top_100_links:
            writer.writerow([src, tgt, val])
            
            
def determine_chromosome(bin_id):
    if 1 <= bin_id <= 404:
    #if 1 <= bin_id <= 284:   
        return 1
    #elif 285 <= bin_id <= 492:
    #elif 559 <= bin_id <= 1012:
        return 2
    #elif 1013 <= bin_id <= 1258:
    #elif 493 <= bin_id <= 547:
        #return 3
    #elif 548 <= bin_id <= 585:
        #return 4
    else:
        return None

def process_data(input_file, output_file):
    nodes = {}
    inter_chromosomal_links = []
    intra_chromosomal_links = []
    
    with open(input_file, 'r') as file:
        next(file)  # Skip header
        for line in file:
            source, target, weight = line.strip().split('\t')
            source_id, target_id = int(source), int(target)
            weight = float(weight)
            source_group = determine_chromosome(source_id)
            target_group = determine_chromosome(target_id)

            # Update nodes
            if source_id not in nodes:
                nodes[source_id] = {"id": f"Node{source_id}", "group": source_group}
            if target_id not in nodes:
                nodes[target_id] = {"id": f"Node{target_id}", "group": target_group}

            # Categorize link
            if source_group == target_group and weight == 10000.0:
                intra_chromosomal_links.append({"source": f"Node{source_id}", "target": f"Node{target_id}", "value": weight})
            else:
                inter_chromosomal_links.append((source_id, target_id, weight))

    # Sort inter-chromosomal links by weight and take the top 20%
    inter_chromosomal_links.sort(key=lambda x: x[2], reverse=True)
    cutoff_index = int(len(inter_chromosomal_links) * 0.5)
    top_inter_chromosomal_links = inter_chromosomal_links[:cutoff_index]
    
    # Call to generate the CSV file for top 100 weights excluding 10000.0
    generate_top_weights_csv(inter_chromosomal_links, 'top_1000_weights_Reduced_GSM1379430_rad21ts-corrected-matrix_hic.csv')


    # Add top inter-chromosomal links to links list
    links = intra_chromosomal_links + [{"source": f"Node{src}", "target": f"Node{tgt}", "value": val} for src, tgt, val in top_inter_chromosomal_links]

    data = {"nodes": list(nodes.values()), "links": links}
    
    # Write to JSON
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)





# Example usage
input_file = 'Basillus_GSM1671431_33_Rudnerlab_HindIII_HiC_BNS1733_42C120m.matrix.txt'  # Update this to your .txt file path
output_file = 'Basillus_42C120m.json'  # Name of the output JSON file
process_data(input_file, output_file)
