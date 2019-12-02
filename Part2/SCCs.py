import numpy as np
import gc
import pickle
import sys

from tqdm import tqdm
from collections import Counter

sys.setrecursionlimit(10000000)

global t
global s

def read_data():
    with open('../Part1/data/_410e934e6553ac56409b2cb7096a44aa_SCC.txt',
              'r') as f:
        data = []
        [data.append([int(item) for item in el.split()]) for el in f.readlines()]
    nrof_vertices = len(np.unique(np.reshape(data, [-1])))
    with open('./data/SCCs_data.pickle', 'wb') as f:
        pickle.dump([nrof_vertices, data], f)
    print('Saved')

def read_converted_data():
    with open('../Part1/data/SCCs_data.pickle', 'rb') as f:
        nrof_vertices, data = pickle.load(f)

    print(nrof_vertices)
    print(len(data))

    print('Read data finished')

    return nrof_vertices, data

def get_graph(nrof_vertices, data, is_reversed=False):
    reversed_graph = [[] for _ in range(nrof_vertices)]
    for edge in tqdm(data):
        if is_reversed:
            reversed_graph[edge[1] - 1].append(edge[0] - 1)
        else:
            reversed_graph[edge[0] - 1].append(edge[1] - 1)
    return reversed_graph

def get_explored_array(nrof_vertices):
    return np.array([False for el in range(nrof_vertices)], dtype=np.bool)

def get_leaders_array(nrof_vertices):
    return np.array([-1 for el in range(nrof_vertices)], dtype=np.int32)

def get_finishing_time_array(nrof_vertices):
    return np.array([-1 for el in range(nrof_vertices)], dtype=np.int32)

def DFS(graph, node, explored_vertices, leaders):
    global t
    global s
    global arcs

    explored_vertices[node] = node
    leaders[node] = s
    for arc_node in graph[node]:
        if explored_vertices[arc_node] == -1:
            if s == 874930:
                print(arc_node)
            DFS(graph, arc_node, explored_vertices, leaders)

    t += 1
    explored_vertices[node] = t

    return

def DFS_while(graph, in_node, explored_vertices, leaders, finishing_time):
    global t
    global s
    global arcs

    stack_vertices = [in_node]
    explored_vertices[in_node] = True
    while len(stack_vertices) > 0:
        node = stack_vertices[-1]
        leaders[node] = s
        is_appended = False
        for arc_node in graph[node]:
            if not explored_vertices[arc_node]:
                stack_vertices.append(arc_node) #DFS(graph, arc_node, explored_vertices, leaders)
                explored_vertices[arc_node] = True
                is_appended = True

        if not is_appended:
            finishing_time[node] = t
            t += 1
            stack_vertices.pop(len(stack_vertices) - 1)

    return

def DFS_Loop(nrof_vertices, graph, explored_vertices, leaders, finishing_time):
    global t
    global s
    t = 0
    s = None

    for i in np.arange(0, nrof_vertices)[::-1]:
        print(i)
        if not explored_vertices[i]:
            s = i
            DFS_while(graph, i, explored_vertices, leaders, finishing_time)

    return

def read_toy_example():
    data = [[7, 1], [1, 4], [4, 7],
            [9, 7], [6, 9], [9, 3], [3, 6],
            [8, 6], [8, 5], [2, 8], [5, 2]]
    nrof_vertices = 9

    return nrof_vertices, data

def rename_graph(data, vertices_map):
    for i, item in enumerate(data):
        data[i] = [vertices_map[item[0] - 1] + 1, vertices_map[item[1] - 1] + 1]

    return data

nrof_vertices, data = read_converted_data()

print('Start first phase')
reversed_graph = get_graph(nrof_vertices, data, True)
explored_vertices = get_explored_array(nrof_vertices)
leaders_vertices = get_leaders_array(nrof_vertices)
finishing_time = get_finishing_time_array(nrof_vertices)
DFS_Loop(nrof_vertices, reversed_graph, explored_vertices, leaders_vertices, finishing_time)

# with open('../Part1/data/finishing_time.pickle', 'wb') as f:
#     pickle.dump(finishing_time, f)

del reversed_graph
gc.collect()

# with open('/Users/macbook/PycharmProjects/StanfordAlgorithms/Part1/data/explored_vertices.pickle', 'rb') as f:
#     explored_vertices = pickle.load(f)

# print('Rename graph')
# data = rename_graph(data, finishing_time)

with open('../Part1/data/renamed_graph.pickle', 'rb') as f:
    data = pickle.load(f)

print('Start second phase')
graph = get_graph(nrof_vertices, data, False)
explored_vertices = get_explored_array(nrof_vertices)
leaders_vertices = get_leaders_array(nrof_vertices)
finishing_time = get_finishing_time_array(nrof_vertices)
DFS_Loop(nrof_vertices, graph, explored_vertices, leaders_vertices, finishing_time)

del graph
del data
gc.collect()

leaders_count = dict(Counter(leaders_vertices))
values = np.sort(list(leaders_count.values()))[-5:]
print(values)
print(leaders_count)

# 875714
# 5105043