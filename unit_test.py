import math
import unittest

import global_game_data
import graph_data
import permutation
from pathing import get_dfs_path, get_bfs_path



class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())


    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    #DFS

    def test_dfs_target(self):
        path = get_dfs_path()
        target = global_game_data.target_node[global_game_data.current_graph_index]
        self.assertIn(target, path, "DFS doesn't hit target")

    def test_dfs_happy(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2]],
            [(300, 300), [1, 3, 4]],
            [(400, 400), [2, 5]],
            [(500, 500), [2]],
            [(500, 500), [3]]
        ]]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 3}

        actual = get_dfs_path()
        expected = [0, 1, 2, 3, 5]
        print(actual)
        self.assertEqual(actual, expected)

    
    
    #BFS

    def test_bfs_target(self):
        path = get_bfs_path()
        target = global_game_data.target_node[global_game_data.current_graph_index]
        self.assertIn(target, path, "BFS doesn't hit target")
    
    def test_bfs_happy(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2]],
            [(300, 300), [1, 3, 4]],
            [(400, 400), [2, 5]],
            [(500, 500), [2]],
            [(500, 500), [3]]
        ]]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: 3}

        actual = get_bfs_path()
        expected = [0, 1, 2, 3, 5]
        print(actual)
        self.assertEqual(actual, expected)

    def test_perms4(self):
        correctPerms = {
        (0, 1, 2, 3), (0, 1, 3, 2), (0, 3, 1, 2), (3, 0, 1, 2),
        (3, 0, 2, 1), (0, 3, 2, 1), (0, 2, 3, 1), (0, 2, 1, 3),
        (2, 0, 1, 3), (2, 0, 3, 1), (2, 3, 0, 1), (3, 2, 0, 1),
        (3, 2, 1, 0), (2, 3, 1, 0), (2, 1, 3, 0), (2, 1, 0, 3),
        (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 2, 0), (3, 1, 2, 0),
        (3, 1, 0, 2), (1, 3, 0, 2), (1, 0, 3, 2), (1, 0, 2, 3)}
        graph = [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ]
        perms = set(tuple(p) for p in permutation.getPerm(graph))
        self.assertEqual(correctPerms, perms)
    
    def test_perms0(self):
        correctPerms = {
        (0,)}
        graph = [
        [(0, 0), [0]],
    ]
        perms = set(tuple(p) for p in permutation.getPerm(graph))
        self.assertEqual(correctPerms, perms)

    def test_hcycle(self):
        graph = [
        [(0, 0), [1, 3]],         
        [(200, 0), [0, 2]],         
        [(200, -200), [1, 3]],      
        [(0, -200), [0, 2]]]
        hcycles = [[0, 1, 2, 3], [3, 0, 1, 2], [0, 3, 2, 1], [2, 3, 0, 1], [3, 2, 1, 0], [2, 1, 0, 3], [1, 2, 3, 0], [1, 0, 3, 2]]
        perms = permutation.getPerm(graph)
        test_hcycles = permutation.find_hamiltonians(graph, perms)
        self.assertEqual(hcycles, test_hcycles)

    def test_no_hcycle(self):
        graph = [
        [(0, 0), [1]],         
        [(200, 0), [0, 2]],         
        [(200, -200), [1, 3]],      
        [(0, -200), [2]]]
        hcycles = []
        perms = permutation.getPerm(graph)
        test_hcycles = permutation.find_hamiltonians(graph, perms)
        self.assertEqual(hcycles, test_hcycles)
if __name__ == '__main__':
    unittest.main()
