
from f_w import makePath, createMatrix, floydWarshall
import unittest

class TestFloydMarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        adjacencyList = {
            0: [(1, 2), (3, 9)],
            1: [(2, 3)],
            2: [(3, 1)],
            3: [(0, 6)],
        }

        # Assume createMatrix is defined to convert adjacency lists to matrices
        matrix = createMatrix(adjacencyList)
        
        dist, parent = floydWarshall(matrix)

        # Updated assertions based on new paths
        assert dist[0][2] == 5, "Path from 0 to 2 should have cost 5"
        assert dist[1][3] == 4, "Path from 1 to 3 should have cost 4"
        assert dist[0][3] == 6, "Path from 0 to 3 should have cost 6"

        # Updated path check
        path = makePath(parent, 0, 3)
        assert path == [0, 1, 2, 3], f"Path from 0 to 3 should be [0, 1, 2, 3], got {path}"
        
        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()

