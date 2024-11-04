import graph_data
import global_game_data
from numpy import random

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
    return finalPath



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
    for i in range(len(finalPath) - 1):
        assert finalPath[i + 1] in graph[finalPath[i]][1]
    return finalPath




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

    return path

def get_dijkstra_path():
    return [1,2]
