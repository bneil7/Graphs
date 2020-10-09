
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


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bfs(self, starting_vertex_id, target_vertex_id):
        # Create an empty Queue and enqueue A PATH to the starting vertex ID
        # Create a Set to store visited vertices
        q = Queue()
        visited = set()
        # WHILE the queue is not empty... (q.size() > 0)
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            #### end_of_path_node = path[-1]
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET VERTEX
                if v == target_vertex_id:
                    # IF SO, RETURN PATH
                    return path  # Found it!
                # Then, either way, mark it as visited..
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    # q.enqueue(neighbor) # WE DON'T WANT TO ENQUEUE THE NEIGHBOR, WE WANT THE PATH
                    new_path = path + [neighbor]
                    q.enqueue(new_path)
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
