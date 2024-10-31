# HiC-Data-Processing-for-Multi-view-Visualization-Dashboard
# Hi-C Data Preparation for Genomic Visualization

This repository contains codes and datasets for transforming raw Hi-C data into formats suitable for multi-view visualization in my thesis work. The focus is on preparing adjacency matrices from Hi-C contact matrices, with special handling for datasets like *Bacillus subtilis*, which require additional processing.

---

## Data Preprocessing for Visualization

### Input Data Description: Hi-C Contact Matrices
Hi-C technology generates matrices representing interaction frequencies between pairs of genomic bins, providing insights into the spatial organization of the genome. However, the *Bacillus subtilis* dataset from the NCBI database presents a unique challenge: it lacks row and column headers. To address this, specific preprocessing steps and scripts are required to create adjacency matrices from raw Hi-C data.

---

## Special Case Handling for *Bacillus subtilis* Data

### Step 1: Initial Cleaning
The first and most crucial step is to clean the raw Hi-C data by replacing any whitespace characters with commas. This ensures that the data is structured correctly before further processing.

### Step 2: Data Transformation Process
We use a series of Python scripts to transform the cleaned data into an adjacency matrix:

1. **Raw Data to Adjacency Matrix**: This script transforms the formatted Hi-C data into an adjacency matrix, making it suitable for subsequent analyses.

2. **CSV to TXT Conversion Without Consecutive Bin Deletion**: Converts the adjacency matrix from CSV to TXT format while ensuring that no consecutive bins are deleted, preserving the integrity of the interaction data.

3. **TXT to JSON for Reduced Dataset**: Converts the TXT file into a JSON format optimized for efficient visualization and reduced dataset size.

These steps ensure that the *Bacillus subtilis* data is accurately represented and ready for use in visualizations.

---

## Data Preparation Summary
- **Initial Cleaning**: Replace whitespace with commas in the raw dataset.
- **Data Transformation**: Use specialized scripts to convert raw Hi-C data into adjacency matrices and export in a JSON format.

This README will be updated with additional instructions or changes as needed. Contributions and suggestions are welcome!
