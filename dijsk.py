#!/usr/bin/env python

from new_graph import Graph


def less_than(a, b):
    if b == 'infinity':
        return True
    return a < b


def dijkstras_algorithm(graph, initial):
    distances = dict()
    for node in graph._nodes:
        distances[node] = 'infinity'
    unvisited = set([node for node in g._nodes])
    current = graph.get_node(initial)
    distances[current] = 0

    # The condition of this loop is a bit too complicated for a single line.
    # Instead, will use while True/if condition: break construction.
    while True:
        neighbors = graph._neighbors(current.data)
        for neighbor in neighbors:
            # Get the distance from the current node to each of its neighbors
            tentative_dist = graph.get_edge(current.data, neighbor.data).weight
            # If the distance through the current node to the neighboring node is less than
            # the tentative distance to the neighboring node, replace the tentative distance
            # with the new distance.
            if less_than[(distances[current] + tentative_dist), distances[neighbor]]:
                distances[neighbor] = distances[current] + tentative_dist
        unvisited.remove(current)
        # If all nodes that are connected to the initial node have been visited,
        # the algorithm is complete. Break the loop.
        if all(distances[node] == 'infinity' for node in unvisited):
            break

        # Set the current node to the node with the smallest tentative distance in 
        # unvisited
        next_candidates = [node.data for node in unvisited if distances[node] != 'infinity']
        current = graph.get_node(min(next_candidates))

    return distances
