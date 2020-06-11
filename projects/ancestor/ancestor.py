class Node:
    def __init__(self, value):
        self.value = value
        self.parents = []
        self.children = []
        self.level = 0

class Graph:
    def __init__(self, ancestors):
        self.nodes = {}
        for i, k in ancestors:
            print(i, k)
            parent = None
            child = None
            if i in self.nodes:
                parent = self.nodes[i]
            else:
                parent = Node(i)
                self.nodes[i] = parent
            if k in self.nodes:
                child = self.nodes[k]
            else:
                child = Node(k)
                self.nodes[k] = child
            parent.children.append(child)
            child.parents.append(parent)
        print(self.nodes)



def earliest_ancestor(ancestors, starting_node):
    graph = Graph(ancestors)
    print(starting_node)
    stack = []
    limit = 0
    furthestAncestor = graph.nodes[starting_node].value

    stack.append(graph.nodes[starting_node])
    while len(stack) != 0:
        node = stack.pop()
        for i in node.parents:
            i.level = node.level + 1
            stack.append(i)
            if limit < i.level:
                limit = i.level
                furthestAncestor = i.value
            elif limit == i.level:
                furthestAncestor = min(i.value, furthestAncestor)
    if furthestAncestor == starting_node:
        return -1
    return furthestAncestor








ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(ancestors, 4))