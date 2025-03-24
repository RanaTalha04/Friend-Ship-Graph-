**📊 Social Network Graph Analysis**
This project analyzes a friendship graph using NetworkX and Matplotlib. It cleans the dataset, constructs the graph, and computes key network measures such as:

Degree distribution 📈

Clustering coefficient distribution 🔄

Path length distribution 🔍

🛠 Features
✅ Reads and cleans a CSV adjacency list to remove empty nodes.
✅ Constructs an undirected graph from the cleaned dataset.
✅ Removes a specified node (630 by default).
✅ Ensures the graph remains connected by keeping the largest component.
✅ Computes graph properties such as:

Degree distribution (how many connections each node has).

Clustering coefficient (how well neighbors of a node are connected).

Path length distribution (shortest path between nodes).
✅ Visualizes these properties using histograms.

📥 Installation
🔹 Requirements
Ensure you have Python 3.x installed. Install the dependencies using:

sh
Copy
Edit
pip install networkx matplotlib pandas numpy
🚀 How to Use
Place your CSV file (Friendship_Graph_2022.csv) in the project directory.

Run the script:

sh
Copy
Edit
python graph_analysis.py
The script will:

Clean and load the graph.

Remove an unwanted node (630 by default).

Ensure connectivity (keep largest component).

Generate histograms for degree, clustering coefficient, and path length.

📊 Output Visualizations
The script generates three histograms:
1️⃣ Degree Distribution – Shows the number of connections per node.
2️⃣ Clustering Coefficient Distribution – Indicates the cliquishness of nodes.
3️⃣ Path Length Distribution – Displays shortest paths between nodes (only if the graph is connected).

📜 Example CSV Format
The input CSV should be in adjacency list format, like this:

Copy
Edit
603,605,606,607,726,709,706,609
604,626,602,608,640,609,621,63,628
605,603,606,607,726,709,706,609
Each row represents a node and its connected neighbors.

📄 File Structure
bash
Copy
Edit
/Social-Network-Graph-Analysis
│── Friendship_Graph_2022.csv    # Input data (Adjacency list)
│── cleaned_graph.adjlist        # Processed graph
│── graph_analysis.py            # Main Python script
│── README.md                    # This documentation
📌 Next Steps
Save computed metrics to a CSV file for further analysis.

Implement a graph visualization with interactive D3.js.

Compare the real-world network to random graphs.

