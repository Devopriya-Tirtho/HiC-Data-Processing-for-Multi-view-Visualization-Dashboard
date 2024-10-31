# Hi-C Data Preparation for Genomic Visualization

This repository contains codes and datasets for transforming raw Hi-C data into formats suitable for multi-view visualization in my thesis work. The focus is on preparing adjacency matrices from Hi-C contact matrices, with special handling for datasets like *Bacillus subtilis*, which require additional processing.

---

## 2D Graph Coordinates Generation

This project uses a modified version of the ForceAtlas2 layout algorithm for weighted graphs. The 2D graph coordinates are generated using code inspired by the [Weighted_GPUGraphLayout](https://github.com/Devopriya-Tirtho/Weighted_GPUGraphLayout) repository.

### How to Run

1. Navigate to the appropriate directory where your code is located.
2. Run the following command to generate the 2D coordinates:
   ```bash
   graph_viewer cpu max_iterations num_snaps sg|wg scale gravity exact edgelist_path out_path [csv|png|bin]
   ```
   - **cpu**: Indicates the use of the CPU implementation.
   - **max_iterations**: The number of iterations to run the layout algorithm.
   - **num_snaps**: Number of snapshots to render during the layout process.
   - **sg|wg**: Choose between strong (`sg`) or weak gravity (`wg`).
   - **scale**: Scale factor for the repulsive force.
   - **gravity**: Scale factor for the gravitational force.
   - **exact**: Use exact O(|V|^2) force calculation.
   - **edgelist_path**: Path to your edge list file (in text format, whitespace-separated).
   - **out_path**: Path to save the output file.
   - **[csv|png|bin]**: Choose the output format (default is `png`).

Refer to the [Weighted_GPUGraphLayout](https://github.com/Devopriya-Tirtho/Weighted_GPUGraphLayout) repository for further details on the ForceAtlas2 algorithm and its application to weighted graphs.

---

## 3D Graph Data Preparation

This project visualizes datasets as 3D force-directed graphs using the `3d-force-graph` library. The main purpose is to extract 3D coordinates of graph nodes after running the layout algorithm.

### How It Works

1. **Dataset Selection**: 
   - Choose from available datasets (e.g., Bacillus, Agrobacterium, Yeast) using a dropdown menu. The selected dataset will render as a 3D graph with nodes and links.
   
2. **Graph Layout Execution**:
   - The graph rendering runs 10 times, measuring and displaying the average execution time.
   - The force-directed algorithm stabilizes the nodes based on repulsive and attractive forces.

3. **3D Coordinate Extraction**:
   - Once the graph stabilizes, export the x, y, and z coordinates of all nodes.
   - Click the **"Export Node Coordinates to CSV"** button to download these coordinates for external use.

### Key Steps to Capture 3D Coordinates

1. Run the 3D graph layout using the provided dropdown to select a dataset.
2. Wait for the layout to stabilize after 10 iterations.
3. Use the **Export** feature to save the 3D coordinates to a CSV file.

Refer to the [3DGraphVisualization](https://github.com/Devopriya-Tirtho/3DGraphVisualization) repository for the full code and instructions.

---

## Heatmap and Parallel Plot Data Preparation

This project prepares edge data for visualizing genomic interactions through heatmaps and parallel plots. The complete edge dataset is used for heatmap visualization, while a filtered subset of top-weighted edges is prepared for parallel plot visualization.

### How It Works

#### Full Edge File for Heatmap
The edge data is processed using a custom script to ensure compatibility with heatmap visualization. The entire set of edges, including all source, target, and weight interactions, is converted into the appropriate format.

#### Top Weighted Edges for Parallel Plot
To simplify and enhance the readability of parallel plot visualizations, only the top-weighted edges for each source node are extracted using the `Top10EdgePerSourceFromJson.py` script.

### Running the Edge Data Processing Scripts

1. **Full Edge Data for Heatmap**:
   - Use the provided Jupyter Notebook `CSV_TO_EDGE_(heatmap)_EdgeDataPreparation.ipynb` to process the complete edge file.
   - The output will be a JSON or CSV file that can be directly used for heatmap visualizations.

2. **Top Weighted Edges for Parallel Plot**:
   - Use the Python script `Top10EdgePerSourceFromJson.py` to generate the top 10 weighted edges per source node.
   - Run the script with the following command:
     ```bash
     python Top10EdgePerSourceFromJson.py
     ```
   - Ensure you replace the `json_filepath` and `output_filepath` in the script with the correct paths to your input and output files.

### Notes

- The full edge dataset captures all interactions for comprehensive heatmap visualizations.
- The top-weighted edge subset is optimized for clear and effective parallel plot visualizations.

---

## License

This project is licensed under the MIT License.
