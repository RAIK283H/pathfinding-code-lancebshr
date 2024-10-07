# Pathfinding Starter Code
Derived Requirements:
1: The Random player shall have a randomly assigned path which begins with the start node,
ends with the exit node, and hits the target along the path. The path shall be a valid
traversal such that each sequential pair of nodes in the path are connected by an edge.

Random solution: The random path selected is truly random. There are no added features to help it.
Instead, every time a player touches a node, it randomly selects one node out of a list of possible
nodes to travel to, and then moves to that node. The proccess is then continuously repeated.

2: Create a statistic that tracks the amount of nodes touched in a walk for each player.
This statistic will be updated live and will be reset after the player has made a successful run.

This statistic was selected because it gives the user important details of the effiency of the 
players run.