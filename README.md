# Hi-C Data Preparation for Genomic Visualization

This repository contains codes and datasets for transforming raw Hi-C data into formats suitable for multi-view visualization in my thesis work. 

---

## Data Preprocessing for Visualization
First, the focus is on preparing adjacency matrices from Hi-C contact matrices.
### Input Data Description: Hi-C Contact Matrices
Hi-C technology generates matrices representing interaction frequencies between pairs of genomic bins, providing insights into the spatial organization of the genome. However, the *Bacillus subtilis* dataset from the NCBI database presents a unique challenge: it lacks row and column headers. To address this, specific preprocessing steps and scripts are required to create adjacency matrices from raw Hi-C data.

### Special Case Handling for *Bacillus subtilis* Data

#### Step 1: Initial Cleaning
The first and most crucial step is to clean the raw Hi-C data by replacing any whitespace characters with commas. This ensures that the data is structured correctly before further processing.

#### Step 2: Data Transformation Process
We use a series of Python scripts to transform the cleaned data into an adjacency matrix:

1. **RawHiCData_TO_AdjacencyMatrix**: Transforms the formatted Hi-C data into an adjacency matrix.
2. **WithoutConsecutiveBinDeletion_CsvtoTxt**: Converts the adjacency matrix from CSV to TXT format, ensuring no consecutive bins are deleted.
3. **txtTOjson_reduceDataset**: Converts the TXT file into a JSON format optimized for visualization.

These steps ensure that the *Bacillus subtilis* data is accurately processed for visualizations.

---

## 2D Graph Coordinates Generation

This project uses a modified version of the ForceAtlas2 layout algorithm for weighted graphs. The 2D graph coordinates are generated using code inspired by the [Weighted_GPUGraphLayout](https://github.com/Devopriya-Tirtho/Weighted_GPUGraphLayout) repository.

### How to Run

1. Navigate to the appropriate directory where your code is located.
2. Run the following command to generate the 2D coordinates:
   ```bash
   graph_viewer cpu max_iterations num_snaps sg|wg scale gravity exact edgelist_path out_path [csv|png|bin]
   ```
   - **cpu**: Use the CPU implementation.
   - **max_iterations**: Number of iterations to run the layout algorithm.
   - **num_snaps**: Number of snapshots to render during the layout process.
   - **sg|wg**: Strong (`sg`) or weak gravity (`wg`).
   - **scale**: Scale factor for the repulsive force.
   - **gravity**: Scale factor for the gravitational force.
   - **exact**: Use exact O(|V|^2) force calculation.
   - **edgelist_path**: Path to the edge list file (whitespace-separated).
   - **out_path**: Path to save the output file.
   - **[csv|png|bin]**: Output format (default: `png`).

---

## 3D Graph Data Preparation

This project visualizes datasets as 3D force-directed graphs using the `3d-force-graph` library. The purpose is to extract 3D coordinates of graph nodes after running the layout algorithm.

### How It Works

1. **Dataset Selection**: Choose from datasets (e.g., Bacillus, Agrobacterium, Yeast) using a dropdown menu.
2. **Graph Layout Execution**: The graph rendering runs 10 times to stabilize node positions.
3. **3D Coordinate Extraction**: Export the stabilized x, y, and z coordinates to a CSV file.

Refer to the [3DGraphVisualization](https://github.com/Devopriya-Tirtho/3DGraphVisualization) repository for more details.

---

## Node Smoothing for 3D Data

### Overview

The 3D data preparation involves two steps:

1. **Extraction of Raw 3D Coordinates**: Export coordinates from the 3D graph visualization.
2. **Node Smoothing**: Apply a smoothing algorithm to enhance node positions.

### Node Smoothing Process

1. **Load Coordinates**: Load the exported CSV file containing node `id`, `x`, `y`, and `z` coordinates.
2. **Apply Smoothing**: Adjust node positions by averaging with neighbors to reduce jitter.
3. **Save Smoothed Coordinates**: Save the smoothed data to a new CSV file.

### How to Run the Smoothing Script

1. Open the `NodeSmoothing_3DVisEnhancer.ipynb` notebook.
2. Load your exported CSV file.
3. Run the script to smooth the coordinates and save them.

---

## Edge Data Processing for Heatmap and Parallel Plot Visualizations

### Full Edge File for Heatmap
Process the entire edge dataset for heatmap visualization. The script outputs a JSON or CSV file for use in visualizations.

### Top Weighted Edges for Parallel Plot
Extract only the top-weighted edges for each source node using `Top10EdgePerSourceFromJson.py`.

### Running the Scripts

1. **Full Edge Data for Heatmap**:
   - Use `CSV_TO_EDGE_(heatmap)_EdgeDataPreparation.ipynb` to process the data.
2. **Top Weighted Edges for Parallel Plot**:
   - Run `Top10EdgePerSourceFromJson.py`:
     ```bash
     python Top10EdgePerSourceFromJson.py
     ```
   - Update `json_filepath` and `output_filepath` as needed.

---

## License

This project is licensed under the MIT License.
