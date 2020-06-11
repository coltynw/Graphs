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
        if v1 in self.vertices and v2 in self.vertices:
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
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # begin at tthe starting vertex
        # explore vertex
        # if unexplored, adjacent vertex
        # explore adjacent vertex
        # Mark explored once all adjacent vertices have been explored (removed from the stack)
        stack = []
        seen = {}
        path = []

        stack.append(starting_vertex)
        seen[starting_vertex] = path

        current = 0
        while len(stack) != 0:
            current = stack.pop()
            print(current)
            nextNode = self.get_neighbors(current)
            for i in nextNode:
                if i not in seen:
                    stack.append(i)
                    seen[i] = [i for i in seen[current]]
                    seen[i].append(current)
    





    def dft_recursive(self, v, seen=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if seen is None:
            seen = {}
            seen[v] = []

        print(v)
        # print(seen)
        nextNode = self.get_neighbors(v)
        for i in nextNode:
            if i not in seen:
                seen[i] = seen[v][:]
                seen[i].append(v)
                self.dft_recursive(i, seen)




    def bfs(self, v, d):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if type(v) != "object":
            v = {'value': v, 'path': [v]}
        q = Queue()
        seen = {}

        q.enqueue(v)
        print("v", v)
        seen[v['value']] = True

        current = 0
        while q.size != 0:
            current = q.dequeue()
            print('bts', current)
            nextNode = self.get_neighbors(current['value'])
            for i in nextNode:
                if i == d:
                    current['path'].append(current['value'])
                    current['path'].append(i)
                    print('wijfw90jef', current['path'])
                    return current['path']
                i = {"value": i, "path": v['path'][:]}
                i['path'].append(current['value'])
                if i['value'] not in seen:
                    q.enqueue(i)

    def dfs(self, starting_vertex, d):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = []
        seen = {}
        path = []

        stack.append(starting_vertex)
        seen[starting_vertex] = path

        current = 0
        while len(stack) != 0:
            current = stack.pop()
            print(current)
            nextNode = self.get_neighbors(current)
            for i in nextNode:
                if i == d:
                    seen[current].append(current)
                    seen[current].append(i)
                    return seen[current]
                if i not in seen:
                    stack.append(i)
                    seen[i] = [i for i in seen[current]]
                    seen[i].append(current)

    def dfs_recursive(self, v, d, seen=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(v)
        if seen is None:
            seen = {}
            seen[v] = []

        # print('dft_rec', v)
        # print('path', seen[v])
        nextNode = self.get_neighbors(v)
        for i in nextNode:
            if i is d:
                seen[v].append(v)
                seen[v].append(d)
                return seen[v]
            if i not in seen:
                seen[i] = seen[v][:]
                seen[i].append(v)
                # self.dft_recursive(i, seen)
                path = self.dfs_recursive(i, d, seen)
                # print("this is the path", path)
                if path:
                    # print()
                    return path
                    

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
