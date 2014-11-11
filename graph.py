#!/usr/bin/env python


class Edge(object):
    def __init__(self, node1, node2):
        # For now, this is an unordered set since our edges have no direction
        # and hence (n1, n2) will be counted the same as (n2, n1)
        self.connects = set((node1, node2))


class Graph(object):
    def __init__(self):
        self._edges = set()
        self._nodes = set()

    def nodes(self):
        return self._nodes

    def edges(self):
        return [edge.connects for edge in self._edges]

    def add_node(self, data):
        self._nodes.add(data)
        return

    def add_edge(self, data1, data2):
        self._nodes.add(data1)
        self._nodes.add(data2)
        edge = Edge(data1, data2)
        self._edges.add(edge)
        return

    def delete_node(self, data):
        try:
            self._nodes.pop()
        except KeyError:
            raise IndexError('graph is empty')
        else:
            # Must use temp set. Can't change set size during iteration
            _temp = set()
            for edge in self._edges:
                if data not in edge.connects:
                    _temp.add(edge)
            self._edges = _temp
        return