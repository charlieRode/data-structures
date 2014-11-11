#!/usr/bin/env python


class Node(object):
    def __init__(self, data):
        self.data = data

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
        if not self.has_node(data):
            raise IndexError("{data} not in graph".format(data=data))
            return
        tups = [edge.connects for edge in self._edges if data in edge.connects]
        neighbors = []
        for tup in tups:
            for elem in tup:
                if elem != data:
                    neighbors.append(elem)
        return neighbors


