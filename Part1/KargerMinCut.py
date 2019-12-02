import numpy as np

def pick_uniformly_edge(nrof_edges, adj_list):
    size = int(np.sum(nrof_edges))
    index = np.random.choice(np.arange(size), 1)[0]

    is_found = False
    i = 0
    while not is_found and i < len(nrof_edges):
        if int(np.sum(nrof_edges[:i + 1])) <= index:
            i += 1
        else:
            u = i
            j = index - int(np.sum(nrof_edges[:i])) - 1 #if index > 0 else 0
            is_found = True

    v = adj_list[u][j]

    return u, v

def create_nrof_edges_list(adj_list):
    nrof_edges = [len(values) for key, values in adj_list.items()]
    return nrof_edges

def create_vertices_map(adj_list):
    return np.arange(len(adj_list))

def update_adj_list(u, v, adj_list, vertices_map):
    for i in range(len(adj_list[u])):
        adj_list[u][i] = vertices_map[adj_list[u][i]]
    for i in range(len(adj_list[v])):
        if adj_list[v][i] != u and vertices_map[adj_list[v][i]] == u:
            print(0)
        adj_list[v][i] = vertices_map[adj_list[v][i]]

    return

def update_v_incident_edges(u, v, adj_list):
    for i in range(len(adj_list[v])):
        if v in adj_list[adj_list[v][i]]:
            index = adj_list[adj_list[v][i]].index(v)
            adj_list[adj_list[v][i]][index] = u
        else:
            print(0)
    return

def merge_into_single_vertex(u, v, adj_list):

    adj_list[u] = [value for value in np.concatenate((adj_list[u], adj_list[v]))
                   if value != u and value != v]
    update_v_incident_edges(u, v, adj_list)
    del adj_list[v]

    return

def update_vertices_map(u, v, vertices_map):
    vertices_map[v] = u
    return

def update_nrof_edges(u, v, nrof_edges, adj_list):
    nrof_edges[u] = len(adj_list[u])
    nrof_edges[v] = 0

    return


def run_Karger_min_cut(adj_list):
    nrof_edges = create_nrof_edges_list(adj_list)
    nrof_unique = len(list(adj_list.keys()))

    while nrof_unique != 2:
        u, v = pick_uniformly_edge(nrof_edges, adj_list)
        merge_into_single_vertex(u, v, adj_list)
        update_nrof_edges(u, v, nrof_edges, adj_list)

        nrof_unique -= 1

    min_cut = np.min(np.array(nrof_edges)[np.where(np.array(nrof_edges) > 0)[0]])

    return min_cut

with open('/Users/macbook/PycharmProjects/StanfordAlgorithms/Part1/data/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt', 'r') as f:
    data = f.readlines()

for _ in range(100):
    adj_list = {id :[int(item) - 1 for item in el.split()[1:]] for id, el in enumerate(data)}

    min_cut = run_Karger_min_cut(adj_list)
    print(min_cut)
