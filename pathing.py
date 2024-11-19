import math
import graph_data
import global_game_data
from numpy import random
from custompriorityqueue import PriorityQueue

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

def get_available_options(currIndex):
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    return graph[currIndex][1]

def get_graph():
    currGraph = graph_data.graph_data[global_game_data.current_graph_index]
    return currGraph


def get_dfs_path():
    path1 = []
    path2 = []
    currIndex = 0
    options = get_available_options(currIndex)
    currTarget = global_game_data.target_node[global_game_data.current_graph_index]
    endNode = len(get_graph()) - 1

    #precondition assert statments
    graph = get_graph()
    assert len(graph) > 1
    assert 0 <= currTarget < len(graph)
    assert 0 <= endNode < len(graph)
    
    def dfs(end, start):
        #Seen nodes set to avoid revisiting
        seen = set()
        stack = [[start]]
        
        while stack:
            #Select current node
            path = stack.pop()
            node = path[-1]

            #If node is found, return path
            if node == end:
                return path
            
            if node in seen:
                continue
            
            #Get neighbors
            for option in get_available_options(node):
                new = list(path)
                new.append(option)
                stack.append(new)

            seen.add(node)

        return None
    
    #finding target
    path1 = dfs(currTarget, 0)

    #finding end node
    path2 = dfs(endNode, currTarget)

    finalPath = path1 + path2[1:]

    #postcondition assert statments
    assert currTarget in finalPath 
    assert finalPath[-1] == endNode
    for i in range(len(finalPath) - 1):
        assert finalPath[i + 1] in graph[finalPath[i]][1]
    return []



def bfs(target, start):
    curr = start
    visited = set()
    queue = []
    path = []
    queue.append(start)

    
    while queue:
        #Selecting current node, adding to path
        curr = queue.pop()
        path.append(curr)

        for node in get_available_options(curr):
            if node not in visited:
                #If final node is found
                if node == target:
                    path.append(node)
                    return path
                #Add node to be visited
                visited.add(node)
                queue.append(node)

     

def get_bfs_path():
    path1 = []
    path2 = []
    currIndex = 0
    options = get_available_options(currIndex)
    currTarget = global_game_data.target_node[global_game_data.current_graph_index]
    endNode = len(get_graph()) - 1
    graph = get_graph()

    #precondition assert statments
    assert len(graph) > 1
    assert 0 <= currTarget < len(graph)
    assert 0 <= endNode < len(graph)

    #finding target
    path1 = bfs(currTarget, 0)

    #finding end node
    path2 = bfs(endNode, currTarget)

    finalPath = path1 + path2[1:]
    #postcondition assert statments
    assert currTarget in finalPath 
    assert finalPath[-1] == endNode
    # for i in range(len(finalPath) - 1):
        # assert finalPath[i + 1] in graph[finalPath[i]][1]
    return[]




def get_random_path():
    path = []
    currIndex = 0
    options = get_available_options(currIndex)
    currTarget = global_game_data.target_node[global_game_data.current_graph_index]
    endNode = len(get_graph()) - 1

    #precondition assert statments
    graph = get_graph()
    assert len(graph) > 1
    assert 0 <= currTarget < len(graph)
    assert 0 <= endNode < len(graph)

    #finding target
    while currIndex != currTarget:
        options = get_available_options(currIndex)
        travelNodeIndex = random.randint(0, len(options))
        travelNode = options[travelNodeIndex]
        path.append(travelNode)
        currIndex = travelNode

    #finding end node
    while currIndex != endNode:
        options = get_available_options(currIndex)
        travelNodeIndex = random.randint(0, len(options))
        travelNode = options[travelNodeIndex]
        path.append(travelNode)
        currIndex = travelNode

    #postcondition assert statments
    assert currTarget in path 
    assert path[-1] == endNode

    return []

def get_dijkstra_path():

    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    pqTarget = PriorityQueue()
    targetVisited = set()
    targetPath = []
    exitIndex = len(graph) - 1
    startIndex = 0
    endVisited = set()
    exitPath = []
    pqEnd = PriorityQueue()

    def calculate_distance(coord1, coord2):
        ychange = coord1[0] - coord2[0]
        ychange = coord1[1] - coord2[1]
        return (ychange ** 2 + ychange ** 2) ** 0.5
    
    #Add first nod as priority 0
    pqTarget.insert(startIndex, 0, [startIndex])
    #Find Path to target
    while not pqTarget.is_empty():
        #Gets current node
        curr, path, dist = pqTarget.delete()
        targetVisited.add(curr)

        #End loop if target node has been reached
        if curr == target_node:
            targetPath = path
            break
        
        for node in graph[curr][1]:
            if node not in targetVisited:
                #Calulate new distance, add if it is shorter then previous
                newDist = calculate_distance(graph[curr][0], graph[node][0])
                newDist = dist + newDist
                if not pqTarget.contains(node):
                    pqTarget.insert(node, newDist, path + [node])
                elif newDist < pqTarget.get_priority(node):
                    pqTarget.update_priority(node, newDist)
                    pqTarget.update_path(node, path + [node])

    #Redo with end node
    pqEnd.insert(target_node, 0, [target_node])
    while not pqEnd.is_empty():
        curr, path, dist = pqEnd.delete()
        endVisited.add(curr)

        if curr == exitIndex:
            exitPath = path
            break

        for node in graph[curr][1]:
            if node not in endVisited:
                newDist = calculate_distance(graph[curr][0], graph[node][0])
                newDist = dist + newDist
                if not pqEnd.contains(node):
                    pqEnd.insert(node, newDist, path + [node])
                elif newDist < pqEnd.get_priority(node):
                    pqEnd.update_priority(node, newDist)
                    pqEnd.update_path(node, path + [node])


    finalpath = targetPath[:-1] + exitPath

    # Postconditions, checking for last and first node
    assert finalpath[0] == startIndex
    assert finalpath[-1] == exitIndex
    #Checks for edges
    for i in range(len(finalpath) - 1):
        assert finalpath[i + 1] in graph[finalpath[i]][1]
    return finalpath[1:]




