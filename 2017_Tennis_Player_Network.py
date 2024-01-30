#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('2017match')

# Create an undirected graph
G = nx.Graph()

# Add edges from the DataFrame. This will automatically create nodes as well.
for index, row in df.iterrows():
    G.add_edge(row['winner_name'], row['loser_name'])

# Calculate the number of unique opponents for each player
unique_opponents = {player: len(set(nx.all_neighbors(G, player))) for player in G.nodes()}

# Use the number of unique opponents to determine node sizes
node_sizes = [unique_opponents[player] * 40 for player in G.nodes()]  # Adjusted scale factor

# Use a layout that spreads nodes apart based on the number of connections
pos = nx.spring_layout(G, k=1.5, iterations=100)

# Draw the graph with a large figure size
plt.figure(figsize=(5
                    ,14))

# Draw nodes with the node size determined by the number of opponents
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', edgecolors='black', linewidths=0.5)

# Draw edges
nx.draw_networkx_edges(G, pos, alpha=0.1)

# Draw labels for all nodes
nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()}, font_size=4, font_color='black')

# Save the graph to a file
plt.axis('off')  # Turn off the axis
plt.tight_layout()  # Tries to minimize the overlap of graph elements


# Display the graph
plt.show()



# In[ ]:




