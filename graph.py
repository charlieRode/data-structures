#!/usr/bin/env python


class Edge(object):
    def __init__(self, vertex1, vertex2):
        # For now, this is an unordered set since our edges have no direction
        # and hence (v1, v2) will be counted the same as (v2, v1)
        self.connects = set((vertex1, vertex2))


class Graph(object):
    def __init__(self):
        self._edges = set()
        self._verticies = set()

    def nodes(self):
        return self._verticies

    def edges(self):
        return [edge.connects for edge in self._edges]

    def add_vertex(self, data):
        self._verticies.add(data)
        return

    def add_edge(self, data1, data2):
        self._verticies = self._verticies.union({data1, data2})
        edge = Edge(data1, data2)
        self._edges.add(edge)
        return

