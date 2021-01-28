import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Creating the graph.
df = pd.read_csv("data/prophet_network.tsv", delimiter="\t")
print(df)
gt = nx.DiGraph()
G = nx.from_pandas_edgelist(df, source="influencer", target="influenced", create_using=gt)

# Drawing the graph.
val_map = {'Corbin': 0.5,
           'Barfield': 0.5,
           'Jung': 0.5,
           'Tillich': 0.5,
           'Heidegger': 0.6}
values = [val_map.get(node, 0.25) for node in G.nodes()]
pos = nx.circular_layout(G)
nx.draw(G, pos)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=values)
plt.savefig("images/prophet_network.png")

if __name__ == '__main__':
    pass

