import sys
class Graph:

    def __init__(self, dim1, dim2):
        self.vertexs = []
        self.n_vertexs = dim1 * dim2
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


