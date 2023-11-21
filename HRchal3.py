#!/bin/python3

import math
import os
import random
import re
import sys

def findShortestPath(graph, start, end):
    shortestDistances = {node: float('inf') for node in graph}
    shortestDistances[start] = 0
    visited = set()

    while True:
        minDistance = float('inf')
        currentNode = None
        for node, distance in shortestDistances.items():
            if node not in visited and distance < minDistance:
                minDistance = distance
                currentNode = node

        if currentNode is None or currentNode == end:
            break

        visited.add(currentNode)

        for neighbor, weight in graph[currentNode].items():
            newDistance = minDistance + weight
            if newDistance < shortestDistances[neighbor]:
                shortestDistances[neighbor] = newDistance

    return shortestDistances[end] if shortestDistances[end] != float('inf') else -1

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())
    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    q = int(input().strip())
    queries = []
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        queries.append((x, y))

    nodeGraph = {}
    for i in range(1, road_nodes + 1):
        nodeGraph[i] = {}

    for i in range(road_edges):
        fromNode = road_from[i]
        toNode = road_to[i]
        weight = road_weight[i]
        nodeGraph[fromNode][toNode] = weight

    for q_itr in range(q):
        x, y = queries[q_itr]
        print(findShortestPath(nodeGraph, x, y))

