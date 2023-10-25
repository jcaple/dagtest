#
# Description:
#
# Given a Directed Acyclic Graph, calculate the longest directed path from 
# that vertex.
#
# Resources:
# - https://networkx.org/documentation/networkx-1.9.1/index.html
# - https://stackoverflow.com/questions/39686213/networkx-most-efficient-way-to-find-the-longest-path-in-a-dag-at-start-vertex-wi
#
# Filename: dagfoo.py
#
# Requirements:
# - pip install networkx
#
# Optional Libraries:
# - pip install matplotlib
#

import networkx as nx
# import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [
        (1,2), 
        (1,3),
        (2,4),
        (3,4),
        (4,5),
        (5,6),
        (2,7),
        (7,8),
        (7,9),
        (7,10),
        (6,1)
    ]
)

# Display Graph for visual inspection if you want
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

# The Vertex to start at
startNode = 1

# The Vertex to end at
endNode = 10

paths = sorted(nx.all_simple_paths(G, source=startNode, target=endNode))
longest = 0
if (len(paths) > 0): longest = len(paths[0])
print("Longest Path: ", longest)