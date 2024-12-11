
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

        # Create matrix from appropriate adjacency list
        matrix = createMatrix(adjacencyList)
        
        dist, parent = floydWarshall(matrix)

        # Assert correct distance
        assert dist[0][2] == 5, "path should have distance of 5"
        assert dist[1][3] == 4, "path should have distance of 4"
        assert dist[0][3] == 6, "path should have distance of 6"

        # Check for correct path
        path = makePath(parent, 0, 3)
        assert path == [0, 1, 2, 3], f"Path should be [0, 1, 2, 3], instead it was {path}"
        
        print("Tests passed!")

if __name__ == '__main__':
    unittest.main()

