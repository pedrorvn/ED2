import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import nxviz as nv
import seaborn as sns

# ''''''''''''''''''''' REDE 1 '''''''''''''''''''''

G1 = nx.read_adjlist("sx-mathoverflow.txt")
print("1st network data:")
print("{} nodes and {} edges".format(G1.number_of_nodes(),G1.number_of_edges()))
print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G1)))
print("Number of connected components: {}".format(nx.number_connected_components(G1)))
print("Size of largest connected component: {}".format(len(max(nx.connected_components(G1),key=len))))
print("Average clustering coefficient: {}\n".format(nx.average_clustering(G1)))

# average degree of neighbors
degree1, avg_neigh_degree1 = zip(*nx.average_degree_connectivity(G1).items())

# convert to list
degree1 = list(degree1)
avg_neigh_degree1 = list(avg_neigh_degree1)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree1,y=avg_neigh_degree1,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0,None)
plt.show()

 

# ''''''''''''''''''''' REDE 2 '''''''''''''''''''''

G2 = nx.read_edgelist("Amazon0302.txt")
print("2nd network data:")
print("{} nodes and {} edges".format(G2.number_of_nodes(),G2.number_of_edges()))
print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G2)))
print("Number of connected components: {}".format(nx.number_connected_components(G2)))
print("Size of largest connected component: {}".format(len(max(nx.connected_components(G2),key=len))))
print("Average clustering coefficient: {}\n".format(nx.average_clustering(G2)))

# average degree of neighbors
degree2, avg_neigh_degree2 = zip(*nx.average_degree_connectivity(G2).items())

# convert to list
degree2 = list(degree2)
avg_neigh_degree2 = list(avg_neigh_degree2)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree2,y=avg_neigh_degree2,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
#ax.set_xlim(0,None)
plt.show()
 
# ''''''''''''''''''''' REDE 3 '''''''''''''''''''''

G3 = nx.read_edgelist("web-NotreDame.txt")
print("3rd network data:")
print("{} nodes and {} edges".format(G3.number_of_nodes(),G3.number_of_edges()))
print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G3)))
print("Number of connected components: {}".format(nx.number_connected_components(G3)))
print("Size of largest connected component: {}".format(len(max(nx.connected_components(G3),key=len))))
print("Average clustering coefficient: {}\n".format(nx.average_clustering(G3)))

# average degree of neighbors
degree3, avg_neigh_degree3 = zip(*nx.average_degree_connectivity(G3).items())

# convert to list
degree3 = list(degree3)
avg_neigh_degree3 = list(avg_neigh_degree3)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree3,y=avg_neigh_degree3,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
#ax.set_xlim(0,None)
plt.show()
 
# ''''''''''''''''''''' REDE 4 '''''''''''''''''''''

G4 = nx.read_edgelist("roadNet-CA.txt")
print("4th network data:")
print("{} nodes and {} edges".format(G4.number_of_nodes(),G4.number_of_edges()))
print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G4)))
print("Number of connected components: {}".format(nx.number_connected_components(G4)))
print("Size of largest connected component: {}".format(len(max(nx.connected_components(G4),key=len))))
print("Average clustering coefficient: {}\n".format(nx.average_clustering(G4)))

# average degree of neighbors
degree4, avg_neigh_degree4 = zip(*nx.average_degree_connectivity(G4).items())

# convert to list
degree4 = list(degree4)
avg_neigh_degree4 = list(avg_neigh_degree4)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree4,y=avg_neigh_degree4,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
#ax.set_xlim(0,None)
plt.show()
 
# ''''''''''''''''''''' REDE 5 '''''''''''''''''''''

G5 = nx.read_edgelist("twitter_combined.txt")
print("5th network data:")
print("{} nodes and {} edges".format(G5.number_of_nodes(),G5.number_of_edges()))
print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G5)))
print("Number of connected components: {}".format(nx.number_connected_components(G5)))
print("Size of largest connected component: {}".format(len(max(nx.connected_components(G5),key=len))))
print("Average clustering coefficient: {}".format(nx.average_clustering(G5)))

# average degree of neighbors
degree5, avg_neigh_degree5 = zip(*nx.average_degree_connectivity(G5).items())

# convert to list
degree5 = list(degree5)
avg_neigh_degree5 = list(avg_neigh_degree5)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree5,y=avg_neigh_degree5,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
#ax.set_xlim(0,None)
plt.show()