import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: Read and Clean Graph Data
with open("Friendship_Graph_2022.csv", "r", encoding="utf-8") as infile, open("cleaned_graph.adjlist", "w", encoding="utf-8") as outfile:
    for line in infile:
        clean_line = ",".join([x.strip() for x in line.split(",") if x.strip()])
        outfile.write(clean_line + "\n")

# Step 2: Load Graph
G = nx.read_adjlist("cleaned_graph.adjlist", delimiter=",")

# Step 3: Clean Node Names
G = nx.relabel_nodes(G, lambda x: x.strip().replace("\ufeff", "").replace("\r", ""))

print("Cleaned Nodes:", list(G.nodes))

# Step 4: Remove Specific Node
your_node = "630"  
if your_node in G:
    G.remove_node(your_node)
    print(f"Removed node: {your_node}")
else:
    print(f"Node {your_node} not found in graph.")

# Step 5: Handle Disconnected Graph (Keep Largest Connected Component)
if not nx.is_connected(G):  
    components = list(nx.connected_components(G))
    print("Connected Components Sizes:", [len(c) for c in components])

    LCC = max(components, key=len)
    G = G.subgraph(LCC).copy()

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10)
plt.title("Updated Social Network Graph")
plt.show()

# Step 6: Compute Graph Metrics
degree_dict = dict(G.degree())
clustering_dict = nx.clustering(G)

# Ensure graph is connected for path length computation
if nx.is_connected(G):
    path_length_dict = dict(nx.shortest_path_length(G))
    all_path_lengths = [dist for node in path_length_dict for dist in path_length_dict[node].values() if node != dist]
else:
    all_path_lengths = []

# Step 7: Visualizing Distributions

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Degree Distribution
axes[0].hist(degree_dict.values(), bins=np.arange(0, max(degree_dict.values()) + 1, 1), color='skyblue', edgecolor='black')
axes[0].set_title("Degree Distribution")
axes[0].set_xlabel("Degree")
axes[0].set_ylabel("Frequency")

# Clustering Coefficient Distribution
axes[1].hist(clustering_dict.values(), bins=20, color='lightcoral', edgecolor='black')
axes[1].set_title("Clustering Coefficient Distribution")
axes[1].set_xlabel("Clustering Coefficient")
axes[1].set_ylabel("Frequency")

# Path Length Distribution (if connected)
if all_path_lengths:
    axes[2].hist(all_path_lengths, bins=20, color='lightgreen', edgecolor='black')
    axes[2].set_title("Path Length Distribution")
    axes[2].set_xlabel("Shortest Path Length")
    axes[2].set_ylabel("Frequency")
else:
    axes[2].text(0.5, 0.5, "Graph is not connected", fontsize=14, ha='center')

plt.tight_layout()
plt.show()
