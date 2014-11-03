#!/usr/bin/env python


class Vertext(object):
    def __init__(self, value):
        self.value = value


class Edge(object):
    def __init__(self):
        self.connects = None


class Graph(object):
    def __init__(self):
        self.edges = []
        self.verticies = []
