#!/usr/bin/env python
import pytest
from new_graph import Node, Edge, Graph


def test_init():
    g = Graph()
    assert len(g._edges) == 0
    assert len(g._nodes) == 0


def test_add_vertex():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    assert 1 in g.nodes()
    assert 2 in g.nodes()


def test_add_edge():
    g = Graph()
    g.add_node(1)
    g.add_edge(3, 2)
    assert len(g.nodes()) == 3
    assert ({3, 2}, 1) in g.edges()


def test_del_edge():
    g = Graph()
    e1 = Edge('a', 'b')
    e2 = Edge('b', 'c')
    e3 = Edge('a', 'c')
    edges = [e1, e2, e3]
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('a', 'c')
    for edge in edges:
        assert edge in g._edges
    g.del_edge('b', 'c')
    assert len(g._edges) == 2
    assert e2 not in g._edges
    assert e1 in g._edges and e3 in g._edges
    try:
        g.del_edge(1, 2)
    except IndexError:
        assert True
    else:
        assert False
    g.del_edge('b', 'a')
    assert len(g._edges) == 1


def test_delete_node():
    g = Graph()
    try:
        g.delete_node('a')
    except IndexError:
        assert True
    else:
        assert False
    for letter in ['a', 'b', 'c', 'd']:
        g.add_node(letter)
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.delete_node('d')
    for edge in g._edges:
        assert 'd' not in edge.connects
    assert len(g._edges) == 3
    g.delete_node('a')
    assert len(g._edges) == 1
    for edge in g._edges:
        assert edge.connects == {'b', 'c'}


def test_has_node():
    g = Graph()
    assert g.has_node('a') is False
    g.add_node('a')
    assert g.has_node('a') is True
    g.add_edge('b', 'c')
    assert g.has_node('b') is True
    g.del_edge('b', 'c')
    assert g.has_node('c') is True


def test_neighbors():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('a', 'c')
    neighbors = g.neighbors('a')
    assert 'b' in neighbors
    assert 'c' in neighbors
    try:
        g.neighbors('q')
    except IndexError:
        assert True
    else:
        assert False


def test_adjacent():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    try:
        g.adjacent('a', 'e')
    except IndexError:
        assert True
    else:
        assert False
    assert g.adjacent('a', 'b') is True
    assert g.adjacent('c', 'b') is False


def test_dfs():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')
    g.add_edge('d', 'e')
    assert g.dfs('a') == ['a', 'b', 'c', 'd', 'e']
    g.add_edge('a', 'e')
    assert g.dfs('a') == ['a', 'b', 'c', 'd', 'e']

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('a', 'd')
    assert len(g.dfs('a')) == 4
    for item in ['a', 'b', 'c', 'd']:
        assert item in g.dfs('a')
    assert g.dfs('b')[:2] == ['b', 'a']
    try:
        g.dfs('h')
    except IndexError:
        assert True
    else:
        assert False


def test_bfs():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('a', 'g')
    g.add_edge('b', 'e')
    g.add_edge('e', 'g')
    g.add_edge('b', 'f')
    g.add_edge('f', 'd')
    g.add_edge('f', 'c')
    g.add_edge('c', 'h')
    assert g.bfs('a') == ['a', 'b', 'd', 'g', 'e', 'f', 'c', 'h']


def test_weighted_edges():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('a', 'g')
    g.add_edge('b', 'e')
    g.add_edge('e', 'g')
    g.add_edge('b', 'f')
    g.add_edge('f', 'd')
    g.add_edge('f', 'c')
    g.add_edge('c', 'h')

    assert g.adjacent('a', 'b') is True
    assert g.adjacent('a', 'c') is False
    g.del_edge('a', 'b')
    assert g.neighbors('a') == ['d', 'g']
