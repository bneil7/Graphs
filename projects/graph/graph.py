"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        # check if visited is None
        if visited is None:
            visited = set()

            # add starting vertex to visited set
            visited.add(starting_vertex)

            # check if vertices in the graph have been visited
            for vertex in self.vertices[starting_vertex]:
                if vertex not in visited:
                    self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            # get the first path
            path = q.dequeue()
            # gets last vertex from path, [-1]
            v = path[-1]

            # check if vertex has been visited
            if v not in visited:
                # check if vertex is destination vertex
                if v is destination_vertex:
                    return path
                # add to visited set
                visited.add(v)
                # add a path to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    q.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            # get last path added to stack
            path = s.pop()
            # get last vertex on the path
            v = path[-1]

            # check if the vertex has been visited
            if v not in visited:
                # check if vertex is destination vertex
                if v is destination_vertex:
                    return path

                # add to visited
                visited.add(v)

                # add a path to the v's neighbors to the front of the stack
                for neighbor in self.get_neighbors(v):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    s.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)
        newPath = [*path, starting_vertex]  # *

        # check if last vertex is destination vertex
        if newPath[-1] == destination_vertex:
            return newPath

        for vertex in self.vertices[starting_vertex]:
            # check if neighbors have been visited
            if vertex not in visited:
                # get the neighbor path
                neighborPath = self.dfs_recursive(
                    vertex, destination_vertex, visited, newPath)
                # return the neighborPath so it can be added to path
                if neighborPath:
                    return neighborPath


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print(" --- ")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(" --- ")
    graph.bft(1)
    print("- ^ BFT ^ -")
    print(" --- ")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(" --- ")
    graph.dft(1)
    print("- ^ DFT ^ -")
    print(" --- ")
    print(" --- ")
    graph.dft_recursive(1)
    print("- ^ DFT RECURSIVE ^ -")
    print(" --- ")
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(" --- ")
    print(graph.bfs(1, 6))
    print("- ^ BFS ^ -")
    print(" --- ")
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(" --- ")
    print(graph.dfs(1, 6))
    print("- ^ DFS ^ -")
    print(" --- ")
    print(graph.dfs_recursive(1, 6))
    print("- ^ DFS RECURSIVE ^ -")
    print(" --- ")
