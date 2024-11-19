import graph_data
import global_game_data


def getPerm(graph):
    n = len(graph)
    #First perm
    permutation = list(range(n))
    #Curr mobile
    mobile = permutation[n-1]
    all_permutations = [permutation[:]]
    directions = [-1] * n
    

    while mobile != -1:

        neighbor = mobile + directions[mobile]

        #Swapping mobile
        directions[mobile], directions[neighbor] = directions[neighbor], directions[mobile]
        permutation[mobile], permutation[neighbor] = permutation[neighbor], permutation[mobile]
        mobile, neighbor = neighbor, mobile

        for i in range(n):
            if permutation[i] > permutation[mobile]:
                directions[i] = -directions[i]

        all_permutations.append(permutation[:])
        mobile = -1
        mobile = -1

        #Gets new mobile number
        for i in range(n):
            neighbor = i + directions[i]
            if 0 <= neighbor < n and permutation[i] > permutation[neighbor]:
                if mobile == -1 or permutation[i] > permutation[mobile]:
                    mobile = permutation[i]
                    mobile = i

    return all_permutations

def find_hamiltonians(graph, all_permutations):
    hamiltonians = []
    #loops permutations
    for permutation in all_permutations:
        if validate_hamiltonian(graph, permutation):
            hamiltonians.append(permutation)
    return hamiltonians

def validate_hamiltonian(graph, permutation):
    #Checks for 1 node per set
    if set(permutation) != set(range(len(graph))):
        return False
    

    for i in range(len(permutation) - 1):
        #If following node is connected
        if permutation[i + 1] not in graph[permutation[i]][1]:
            return False
        
        #If it connects back around
        if permutation[0] not in graph[permutation[-1]][1]:
            return False
        
    return True
                                       