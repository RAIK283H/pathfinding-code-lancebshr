import math
import unittest

import global_game_data
import graph_data

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

    def test_dfs_fail(self):
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

        try:
            get_dfs_path()
        except AssertionError:
            return
        self.fail("DFS doesn't fail")
    
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

    def test_bfs_fail(self):
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

        try:
            get_bfs_path()
        except AssertionError:
            return
        self.fail("BFS doesn't fail")
        
if __name__ == '__main__':
    unittest.main()
