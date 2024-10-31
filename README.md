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

1. **RawHiCData_TO_AdjacencyMatrix**: This script transforms the formatted Hi-C data into an adjacency matrix, making it suitable for subsequent analyses.

2. **WithoutConsecutiveBinDeletion_CsvtoTxt**: Converts the adjacency matrix from CSV to TXT format while ensuring that no consecutive bins are deleted, preserving the integrity of the interaction data.

3. **txtTOjson_reduceDataset**: Converts the TXT file into a JSON format optimized for efficient visualization and reduced dataset size.

These steps ensure that the *Bacillus subtilis* data is accurately represented and ready for use in visualizations.

---

## Data Preparation Summary
- **Initial Cleaning**: Replace whitespace with commas in the raw dataset.
- **Data Transformation**: Use specialized scripts (`RawHiCData_TO_AdjacencyMatrix`, `WithoutConsecutiveBinDeletion_CsvtoTxt`, and `txtTOjson_reduceDataset`) to convert raw Hi-C data into adjacency matrices and export in a JSON format.

This README will be updated with additional instructions or changes as needed. Contributions and suggestions are welcome!

# 3D Force Graph Visualization

This project visualizes datasets as 3D force-directed graphs using the `3d-force-graph` library. It allows dynamic dataset selection and calculates average execution time for rendering. The main purpose here is to extract 3D coordinates of graph nodes after running the layout algorithm.

---

## How It Works

1. **Dataset Selection**: 
   - Choose from available datasets (e.g., Bacillus, Agrobacterium, Yeast) using a dropdown menu. The selected dataset will render as a 3D graph with nodes and links.
   
2. **Graph Layout Execution**:
   - The graph rendering runs 10 times, measuring and displaying the average execution time.
   - The force-directed algorithm stabilizes the nodes based on repulsive and attractive forces.

3. **3D Coordinate Extraction**:
   - Once the graph stabilizes, you can export the x, y, and z coordinates of all nodes.
   - Click the **"Export Node Coordinates to CSV"** button to download these coordinates for external use.

## Key Steps to Capture 3D Coordinates

1. Run the 3D graph layout using the provided dropdown to select a dataset.
2. Wait for the layout to stabilize after 10 iterations.
3. Use the **Export** feature to save the 3D coordinates to a CSV file.

---

## Reference

For the full code and detailed instructions, visit the repository: [3DGraphVisualization](https://github.com/Devopriya-Tirtho/3DGraphVisualization)

---

This setup is optimized for easy extraction of 3D node coordinates, making it suitable for further data analysis or integration into other visualization systems.

# 3D Data Preparation for Visualization

This repository provides the code and instructions for preparing and enhancing 3D data obtained from force-directed graph visualizations. The workflow involves extracting raw 3D coordinates from the graph layout and applying a smoothing algorithm to improve the visualization quality.

---

## Overview

The 3D data preparation process consists of two main steps:

1. **Extraction of Raw 3D Coordinates**: 
   - Run the 3D graph visualization using the `3d-force-graph` library as outlined in the [3DGraphVisualization](https://github.com/Devopriya-Tirtho/3DGraphVisualization) repository.
   - Export the x, y, and z coordinates of all nodes once the layout stabilizes.

2. **Node Smoothing**:
   - Use the provided smoothing script to enhance the positions of the nodes, reducing jitter and improving the overall graph structure.

---

## Node Smoothing Process

### How It Works

1. **Load the Extracted Coordinates**:
   - The exported CSV file containing the node `id`, `x`, `y`, and `z` coordinates is loaded into the smoothing script.
   
2. **Apply Smoothing Algorithm**:
   - The algorithm adjusts the positions of nodes by averaging their coordinates with those of neighboring nodes.
   - This process reduces abrupt changes and provides a more stable and visually appealing graph structure.

3. **Save the Smoothed Coordinates**:
   - The final smoothed coordinates are saved in a new CSV file, ready for use in the multi-view visualization dashboard or other analysis tools.

---

## How to Run the Smoothing Script

1. Open the `NodeSmoothing_3DVisEnhancer.ipynb` notebook.
2. Load your exported node coordinates CSV file into the notebook.
3. Run the provided code cells to smooth the 3D coordinates.
4. Save the smoothed coordinates to a new CSV file for further use.

---

## Prerequisites

- **Python 3** and the following libraries:
  - `pandas` for data manipulation
  - `numpy` for mathematical operations
  - Any other dependencies specified in the notebook

## Notes

- Ensure the raw coordinates are accurately captured before applying smoothing.
- Adjust the parameters in the smoothing algorithm as needed to achieve the desired visualization quality.

---

## License

This project is licensed under the MIT License.

