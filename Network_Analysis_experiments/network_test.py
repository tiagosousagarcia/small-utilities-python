#Network analysis exercises, source here: https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python

import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community

#read list of nodes into python
with open('quakers_nodelist.csv', 'r') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader][1:]
    
node_names = [n[0] for n in nodes]

#read list of edges
with open('quakers_edgelist.csv', 'r') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]

#create empty Graph
G = nx.Graph()

#populate Graph
G.add_nodes_from(node_names)
G.add_edges_from(edges)

#Print basic information
print(nx.info(G))

#Create empty dictionaries to populate with attributes
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}

#construct dictionaries from nodes list
for node in nodes:
    hist_sig_dict[node[0]] = node[1]
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]
    
#set attributes based on dictionaries:
nx.set_node_attributes(G, hist_sig_dict, 'historical_significance')
nx.set_node_attributes(G, gender_dict, 'gender')
nx.set_node_attributes(G, birth_dict, 'birth_year')
nx.set_node_attributes(G, death_dict, 'death_year')
nx.set_node_attributes(G, id_dict, 'sdfb_id')

#print birth years of all nodes:
# for n in G.nodes():
#     print(n, G.nodes[n]['birth_year'])
    

#simple network metrics
density = nx.density(G)
print("Network density:", density)

fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target = "George Whitehead")
print("Shortest path between Fell and Whitehead:", fell_whitehead_path)

print("Length of that path: ", len(fell_whitehead_path)-1)

#finding diameter -> because the network is not connected, you need a subgraph to calculate the diameter of the largest community
print(nx.is_connected(G))
components = nx.connected_components(G)
largest_component = max(components, key=len)

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component: ", diameter)

triadic_closure = nx.transitivity(G)
print("Triadic closure: ", triadic_closure)

#calculating centrality

degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')
print(G.nodes['William Penn'])

sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)

betweenness_dict = nx.betweenness_centrality(G)
eigenvector_dict = nx.eigenvector_centrality(G)

nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')

sorted_betweenness = sorted(betweenness_dict.items(), key=itemgetter(1), reverse=True)
print("Top 20 nodes by betweenness centrality:")
for b in sorted_betweenness[:20]:
    print(b)

top_betweenness = sorted_betweenness[:20]

for tb in top_betweenness:
    degree = degree_dict[tb[0]]
    print("Name:", tb[0], " | Betweeness centrality:", tb[1], " | Degree:", degree)

