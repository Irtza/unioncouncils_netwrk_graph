import pandas as pd
import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



import matplotlib.pyplot as plt

def draw_graph(graph, labels=None, cityname = "City" , graph_layout='spring',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))
    
    plt.title(cityname+"'s Union Council's and chairmans")
    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    plt.show()
    return fig , G


# In[3]:

def make_graph(cityname):
    '''
    takes city: makes graph
    '''
    data = pd.read_csv('data/uc_representative_list/'+cityname+'.csv')
    data.fillna(' ', inplace=True)
    data = data.ix[1:]
    #Top 10
    data = data.head(10)
    graph = []
    for i in range(0, len(data)):
        graph.append(tuple([data.iloc[i,2], cityname ]))
    return graph


# In[6]:

graph1 = make_graph("islamabad")
graph2 = make_graph("lahore")
graph3 = make_graph("peshawar")

fig1 , g1 = draw_graph(graph1 , cityname="islamabad")
fig2 , g2 = draw_graph(graph2 , cityname="lahore")
fig3 , g3 = draw_graph(graph3 , cityname="peshawar")

#fig1.savefig('1_isb.png', dpi=100)
#fig2.savefig('2_lhr.png', dpi=100)
#fig3.savefig('3_pesh.png', dpi=100)

#g1.add_edge(1,2)
#g2.add_edge(1,2)

#K = nx.compose(g1,g2)
#graph_pos=nx.spectral_layout(K)

# draw graph
#nx.draw_networkx_nodes(K,graph_pos)
#nx.draw_networkx_edges(K,graph_pos)
#nx.draw_networkx_labels(K, graph_pos)


#labels = range(len(K))

#plt.title("Council's and chairmans")
#edge_labels = dict(zip(K, labels))
#nx.draw_networkx_edge_labels(K, graph_pos )

# show graph
#fig = plt.gcf()
#fig.set_size_inches(18.5, 10.5)
#plt.show()


# # TODO:
# 
# ###  Export to JSON for d3 js

# In[5]:

type(graph1)


# In[ ]:



