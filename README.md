# Social Network Graph Analysis

## Overview
This project analyzes a social network graph using **NetworkX** and **Matplotlib** in Python. The analysis includes:
- Cleaning and visualizing the graph
- Computing various graph statistics
- Finding centrality measures
- Detecting communities
- Checking for small-world properties
- Generating distributions of node properties

## Features
### 1. **Graph Cleaning & Visualization**
- Reads a CSV file and removes unwanted characters.
- Converts the data into an adjacency list format.
- Visualizes the cleaned graph with labels.

### 2. **Graph Properties**
The following network properties are computed:
- **Average Degree**
- **Average Clustering Coefficient**
- **Average Path Length**
- **Graph Diameter**
- **Assortativity Coefficient**
- **Nodes with Highest & Lowest Degree**

### 3. **Degree, Clustering Coefficient & Path Length Distribution**
- Generates distribution plots for:
  - Node degrees
  - Clustering coefficients
  - Path lengths

### 4. **Centrality Measures (Top-10 Nodes)**
- **Degree Centrality**
- **Closeness Centrality**
- **Betweenness Centrality**
- **Eigenvector Centrality**

### 5. **Community Detection**
- Uses the **asyn_lpa_communities** method from NetworkX to identify communities.
- Visualizes the graph with different colors for each community.

### 6. **Small-World Property Check**
- Compares the clustering coefficient and path length to determine if the graph exhibits small-world behavior.

## Installation & Usage
### Prerequisites
- Python 3.x
- NetworkX
- Matplotlib
- Pandas (optional, for advanced data handling)

### Installation
```bash
pip install networkx matplotlib
```

### Run the Script
```bash
python analysis.py
```

## Git Commands for Repository Management
### Set Up Remote Repository
If you face an error like `remote origin already exists`, you can fix it using:
```bash
git remote remove origin
git remote add origin https://github.com/RanaTalha04/Social-Network-Graph-Analysis.git
git push -u origin master
```

### Pulling Changes
If you encounter `fatal: refusing to merge unrelated histories`, use:
```bash
git pull origin master --allow-unrelated-histories
```

## Future Improvements
- Add dynamic community detection algorithms.
- Enhance visualization with interactive graphs (e.g., using Plotly).
- Optimize large-scale network computations using parallel processing.

## Author
**Muhammad Talha**

---
This project provides a comprehensive analysis of a social network graph, focusing on key graph theory concepts. 🚀

