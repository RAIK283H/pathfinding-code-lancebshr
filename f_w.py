import graph_data
import math


def createMatrix(adjacencyList):
    size = len(adjacencyList)
    matrix = [[math.inf] * size for _ in range(size)] 
    for i in range(size):
        matrix[i][i] = 0
    for i in range(size):
        for neighbor, weight in adjacencyList[i]:
            matrix[i][neighbor] = weight  

    return matrix


def floydWarshall(matrix):
    n = len(matrix)
    parent = [[None] * n for _ in range(n)]
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0

            elif matrix[i][j] != math.inf:
                dist[i][j] = matrix[i][j]
                parent[i][j] = j 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                newDist = dist[i][k] + dist[k][j]
                if newDist < dist[i][j]:
                    dist[i][j] = newDist
                    parent[i][j] = parent[i][k]

    return dist, parent
       
def makePath(parent, start, end):
    if parent[start][end] is None:
        return []
    
    path = [start]
    while start != end:
        start = parent[start][end]
        path.append(start)

    return path

def main():
    # test the function
    adjacencyList = {
            0: [(1, 2), (3, 9)],
            1: [(2, 3)],
            2: [(3, 1)],
            3: [(0, 6)],
        }
    
    start_node = 0
    end_node = 3
    matrix = createMatrix(adjacencyList)
        
    dist, parent = floydWarshall(matrix)

   
    path = makePath(parent, start_node, end_node)
    
    
    print(f"The shortest path is {path} with a distance of {dist[start_node][end_node]}.")

main()
