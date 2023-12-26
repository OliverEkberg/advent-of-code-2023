from networkx import Graph, minimum_edge_cut, connected_components
from math import prod

graph = Graph()
for line in open('data.txt'):
    starts, ends = [side.split() for side in line.split(': ')]

    for start in starts:
        for end in ends:
            graph.add_edge(start, end)

graph.remove_edges_from(minimum_edge_cut(graph))
print(prod(map(len, connected_components(graph))))
