import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

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

# Step 6: Compute Graph Metrics
average_degree = sum(dict(G.degree()).values()) / len(G.nodes)
average_clustering = nx.average_clustering(G)

# Ensure the graph is connected for path-related metrics
if nx.is_connected(G):
    average_path_length = nx.average_shortest_path_length(G)
    diameter = nx.diameter(G)
else:
    average_path_length, diameter = "Graph is not connected", "Graph is not connected"

assortativity = nx.degree_assortativity_coefficient(G)

# Find highest and lowest degree nodes
degree_dict = dict(G.degree())
highest_degree_node = max(degree_dict, key=degree_dict.get)
lowest_degree_node = min(degree_dict, key=degree_dict.get)

# Step 7: Display Metrics in a Table
data = {
    "Metric": [
        "Average Degree",
        "Average Clustering Coefficient",
        "Average Path Length",
        "Diameter",
        "Assortativity Coefficient",
        "Highest Degree Node",
        "Lowest Degree Node",
    ],
    "Value": [
        average_degree,
        average_clustering,
        average_path_length,
        diameter,
        assortativity,
        highest_degree_node,
        lowest_degree_node,
    ],
}

df = pd.DataFrame(data, index=None)
print("\nGraph Metrics:\n", df)

# Step 8: Visualize the Graph
plt.figure(figsize=(12, 10))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10)
plt.title("Updated Social Network Graph")
plt.show()

# print("Total Nodes:", G.number_of_nodes())
# print("Total Edges:", G.number_of_edges())
# print("Is Graph Connected?", nx.is_connected(G))
# print("Number of Connected Components:", nx.number_connected_components(G))

# print("Nodes:", list(G.nodes)[:10])  
# print("Edges:", list(G.edges)[:10])  

# isolated_nodes = [node for node in G.nodes if G.degree(node) == 0]
# print("Isolated Nodes:", isolated_nodes)
# print("Is '630' still in graph?", "630" in G.nodes)

# if "63" in G.nodes:
#     print("Node 63 exists in the graph!")
#     print("It has edges with:", list(G.neighbors("63")))