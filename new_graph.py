#!/usr/bin/env python


class Node(object):
    def __init__(self, data):
        self.data = data
        self.visited = None

    def __repr__(self):
        return "Node({data})".format(data=self.data)

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)


class Edge(object):
    # I'm storing the edge as a set of two data points,
    # rather than two Node objects for simplicity's sake.
    # May need to change this later.
    def __init__(self, data1, data2):
        self._d1 = data1
        self._d2 = data2
        self.connects = set((data1, data2))

    def __repr__(self):
        return "Edge({data1}, {data2})".format(data1=self._d1, data2=self._d2)

    def __str__(self):
        return str(self.connects)

    def __eq__(self, other):
        return self.connects == other.connects

    def __hash__(self):
        return hash(self._d1) ^ hash(self._d2)


class Graph(object):
    def __init__(self):
        self._edges = set()
        self._nodes = set()

    def add_node(self, data):
        self._nodes.add(Node(data))
        return

    def add_edge(self, data1, data2):
        self._nodes.add(Node(data1))
        self._nodes.add(Node(data2))
        self._edges.add(Edge(data1, data2))
        return

    def nodes(self):
        return [node.data for node in self._nodes]

    def edges(self):
        return [edge.connects for edge in self._edges]

    def delete_edge(self, data1, data2):
        edge = Edge(data1, data2)
        if edge in self._edges:
            self._edges.remove(edge)
        else:
            raise IndexError(str(Edge(data1, data2)) + " does not exist")
        return

    def delete_node(self, data):
        if Node(data) in self._nodes:
            self._nodes.remove(Node(data))
        else:
            raise IndexError(str(Node(data)) + " does not exist")
        temp = set()
        for edge in self._edges:
            if data not in edge.connects:
                temp.add(edge)
        self._edges = self._edges.intersection(temp)
        return

    def has_node(self, data):
        return data in self.nodes()

    def neighbors(self, data):
        """Returns a list of all adjacent nodes to 'data'"""
        if not self.has_node(data):
            raise IndexError("{data} not in graph".format(data=data))
            return
        # tups are the tuples that represent the edges that connect (node1, node2),
        # where node1 is data being passed to neighbors()
        # E.g. if neighbors('a') is called, tups might be ('a', 'b'),
        # ('a', 'd'), ('a', 'f')...
        tups = [edge.connects for edge in self._edges if data in edge.connects]
        neighbors = []
        for tup in tups:
            for elem in tup:
                if elem != data:
                    neighbors.append(elem)
        return neighbors

    def _neighbors(self, data):
        return [node for node in self._nodes if node.data in self.neighbors(data)]

    def adjacent(self, data1, data2):
        """Returns True iff data1 and data2 are connected by an edge"""
        if self.has_node(data1) is False or self.has_node(data2) is False:
            raise IndexError("one or both of the supplied nodes does not exist")
            return
        else:
            return Edge(data1, data2) in self._edges

    def _get_node(self, data):
        for node in self._nodes:
            if data == node.data:
                return node

    def dfs(self, start):
        """Perfomes a depth-first-traversal, starting at Node(start)"""
        if self.has_node(start) is False:
            raise IndexError("{start} not in graph".format(start=start))
            return
        for node in self._nodes:
            # Assign each  node in the graph the attribute 'visited'
            node.visited = False
            # Full traversal path to be returned by the method
        path = []

        def _traverse(node):
            path.append(node.data)
            node.visited = True
            for neighbor in self._neighbors(node.data):
                if neighbor.visited is False:
                    _traverse(neighbor)

        _traverse(self._get_node(start))
        for node in self._nodes:
            node.visited = False
        return path

        def bfs(self, start):
            """Perfomes a breadth-first-traversal, starting at Node(start)"""
            from queue import Queue
            if self.has_node(start) is False:
                raise IndexError("{start} not in graph".format(start=start))
                return
            for node in self._nodes:
                # Assign each  node in the graph the attribute 'visited'
                node.visited = False
                # Full traversal path to be returned by the method
            path = []
            q = Queue()


            def _get_node(data):
                for node in self._nodes:
                    if data == node.data:
                        return node




            _traverse(_get_node(start))
            for node in self._nodes:
                return path

