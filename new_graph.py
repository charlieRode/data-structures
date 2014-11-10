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


class Edge(object):
    # I'm storing the edge as a set of two data points,
    # rather than two Node objects for simplicities sake.
    # May need to change this later.
    def __init__(self, data1, data2):
        self.connects = set((data1, data2))


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

    def nodes(self):
        return [node.data for node in self._nodes]

    def edges(self):
        return [edge.connects for edge in self._edges]

    def delete_edge(self, data1, data2):
        self._edges.remove()

    def delete_node(self, data):
        try:
            self._nodes.pop()
        except KeyError:
            raise IndexError('graph is empty')

        