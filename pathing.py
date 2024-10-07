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
    global_game_data.current_graph_index
    return graph_data.graph_data[global_game_data.current_graph_index][currIndex][1]

def get_graph():
    currGraph = graph_data.graph_data[global_game_data.current_graph_index]
    return currGraph

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


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
