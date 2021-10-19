import networkx as nx
import matplotlib.pyplot as plt


def get_nodes():
    nodes = []
    colors = []
    with open("nodes.txt") as f:
        for line in f:
            node = line[:-1].split(",")
            nodes.append(node[0])
            colors.append(node[1])

    return nodes, colors


def get_edges():
    edges = []
    with open("edges.txt") as f:
        for line in f:
            edge = line[:-1].split(",")
            edges.append((edge[0], edge[1]))

    return edges


if __name__ == '__main__':

    print(get_nodes())
    print(get_edges())

    G = nx.Graph()
    G.add_nodes_from(get_nodes()[0])
    G.add_edges_from(get_edges())

    colors = get_nodes()[1]
    print(colors)

    nx.draw_spring(G, node_color=colors)
    plt.show()
