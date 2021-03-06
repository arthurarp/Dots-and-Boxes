import sys
class Graph:

    def __init__(self, dim1, dim2):
        self.vertexs = []
        self.n_vertexs = dim1 * dim2
        self.n_edges = 0
        center = [231.5, 75]
        index = 0
        

        for i in range(dim1):
            for j in range(dim2):
                vertex = {
                    'index': index,
                    'row': i,
                    'column': j,
                    'adjacency_list': [],
                    'center_of_mass': {'x': center[0], 'y': center[1]},
                }
                self.vertexs.append(vertex)
                center[0] += 84
                index = index + 1
                
            center[0] = 231.5
            center[1] += 75

    def is_empty(self):
        if self.vertexs == []:
            return True
        return False

    def add_vertex(self, data):
        self.vertexs.append(data)

    def get_vertexs(self):
        return self.vertexs

    def get_n_vertexs(self):
        return self.n_vertexs

    def _print(self):
        for vertex in self.vertexs:
            if vertex['adjacency_list'] != []:
                print(vertex)

    def connect_edge(self, origin, destiny):
        self.vertexs[origin]['adjacency_list'].append(destiny)
        self.vertexs[destiny]['adjacency_list'].append(origin)
        self.n_edges += 1

    def is_graph_all_connected(self):
        if self.n_edges == 49:
            return True
        return False

    def is_already_connected(self, origin, destiny):
        if origin['adjacency_list'] == [] or destiny['adjacency_list'] == []:
            return False
        for edge in self.vertexs[origin['index']]['adjacency_list']:
            if edge == destiny['index']:
                print(origin['index'], 'ja conectado')
                return True
        return False

    def clear(self):
        self.vertexs = []
        self.n_edges = 0


