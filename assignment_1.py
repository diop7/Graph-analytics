import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_node('1', label='Dublin')
G.add_nodes_from([('2', {'label': 'Leon', 'type': 'city'}),
                  ('3', {'label': 'Spain', 'type': 'country'}),
                  ('4', {'label': 'province of Leon', 'type': 'province'}),
                  ('5', {'label': 'Himmo a leon', 'type': 'anthem'}),
                  ('6', {'label': '837', 'type': 'meter'}),
                  ('7', {'label': 'Xiangtian', 'type': 'city'}),
                  ('8', {'label': 'Republic of Ireland', 'type': 'country'}),
                  ('9', {'label': 'Leinster', 'type': 'province'}),
                  ('10', {'label': '553165', 'type': 'Population'}),
                  ('11', {'label': 'Royal Canal', 'type': 'canal'}),
                  ('12', {'label': 'Cloondara', 'type': 'start'}),
                  ('13', {'label': 'Stream', 'type': 'type'}),
                  ('14', {'label': 'capital city', 'type': 'type'}),
                  ('15', {'label': 'Dublin city council', 'type': 'council'}),
                  ('16', {'label': 'River Shannon', 'type': 'River'}),
                  ('17', {'label': '127817', 'type': 'population'}),
                  ('19', {'label': 'Guiness Brewery', 'type': 'brewery'}),
                  ('20', {'label': '208.1', 'type': 'discharge'}),
                  ])



G.add_edges_from([('1', '14')], type='type')
G.add_edges_from([('1', '8')], type='capital of')
G.add_edges_from([('1', '10')], type='total population')
G.add_edges_from([('1', '15')], type='council')
G.add_edges_from([('19', '1')], type='foundation place')
G.add_edges_from([('11', '1')], type='end point')

G.add_edges_from([('2', '6')], type='elevation')
G.add_edges_from([('2', '1'), ('2', '7')], type='twin city')
G.add_edges_from([('2', '4'), ('1', '9')], type='is part of')
G.add_edge('2', '3', type='twin city')
G.add_edges_from([('2', '5')], type='anthem')
G.add_edges_from([('2', '17')], type='total population')
G.add_edges_from([('16', '20')], type='discharge m³/s')
G.add_edges_from([('11', '12')], type='start point')
G.add_edges_from([('11', '20')], type='discharge m³/s')
G.add_edges_from([('11', '16')], type='has junction with')
G.add_edges_from([('12', '8')], type='country')

node_labels = nx.get_node_attributes(G, 'label')
edge_labels = nx.get_edge_attributes(G, 'type')
pos = nx.spring_layout(G)

nx.draw(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos, labels=node_labels)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
plt.show()