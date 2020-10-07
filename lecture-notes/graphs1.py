# Graphs
# ------
# Nodes (also called "verts", "vertexes", "vertices") are connected by edges

# Edges MAY have numeric weights associated with them
#   * If not shown, assume all weights are 1 (this is called an "unweighted graph")

# Edges can be directed (one-way only --> ) or undirected (two way <----> )
#   * If there are ONLY undirected edges, we call it an 'undirected graph'
#   * Else we call it a "directed graph"

# Cycle: we can traverse and get back to the starting node somehow
#   if a graph has any cycles in it, we call it a 'cyclic graph'
#   else, it's an 'acyclic graph'

# Representation of graphs
# ------------------------
# Which nodes are adjacent ('directly connected') to a particular node
#
# Adjacency Matrix
#    * big grid that has true/false values showing which nodes are adjacent
#   * or edge weights

# Adjacency list (using a set {} ):
# A: {B, D} <-- A is connected to B & D
# B: {D, C} <-- B is connected to C & D (or D & C, order doesn't matter) !! UNDIRECTED, B & C goes both ways
# C: {C, B} <-- C is connected to C & B !! UNDIRECTED, C & B goes both ways
# D: {} <-- D is connected to nothing

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}  # keys are all verts in the graph, values are sets of adjacent verts

    def add_vertex(self, vertex):
        ''' Add a new unconnected vert '''
        self.vertices[vertex] = set()
        # set() <-- ~1h10m into lecture, https://youtu.be/hST_X7eFWSQ?t=4307
        # creates a dictionary of sets, both use {} in print console

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("nonexistent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    def bft(self, starting_vertex_id):  # using Queue instead of Stack
        q = Queue()
        visited = set()

        # Init:
        q.enqueue(starting_vertex_id)

        # while queue isn't empty
        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                print(v)  # "visit" the node

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):  # using Stack instead of Queue
        q = Stack()
        visited = set()

        # Init:
        q.push(starting_vertex_id)

        # while queue isn't empty
        while q.size() > 0:

            v = q.pop()

            if v not in visited:
                print(v)  # "visit" the node

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)  # 3 is only connected to 2

g.bft(1)
print("--")
g.bft(3)  # only returns 3 because 3 has no neighbors
print("--")
g.bft(2)
print("--")


print(f"{g.vertices}, <--- Test BFT")

g.dft(1)
print("--")
g.dft(2)
print("--")
g.dft(3)
print("--")
g.dft(4)

print(f"{g.vertices}, <--- Test DFT")


# print(g.vertices)


# BREADTH-FIRST TRAVERSAL (BFT)
# https://youtu.be/hST_X7eFWSQ?t=5205 ~1h27m
# ----------------------------
# Init:
#   Add the starting vert to the queue
#
# While the queue is not empty:
#   pop current vert off queue
#   If not visited:
#       "visit" the node (add it to a path, etc.)
#       Track it as visited
#       add all its neighbors (adjacent nodes) to the queue
