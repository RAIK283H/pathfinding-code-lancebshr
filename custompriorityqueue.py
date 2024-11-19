print("priorityqueue module loaded")

class PriorityQueue:
    def __init__(self):
        self.queue = {}  # Priority queue with {priority: [(node_index, path)]}

    def insert(self, node_index, priority, path):

        if priority in self.queue:
            self.queue[priority].append((node_index, path))
        else:
            self.queue[priority] = [(node_index, path)]

    def delete(self):
        if not self.queue:
            raise IndexError("Priority Queue is empty")

        # Get the lowest priority value
        max_priority = min(self.queue.keys())

        # Remove and return the first node index and path from this priority level
        node_index, path = self.queue[max_priority].pop(0)

        # Clean up if there are no more nodes at this priority level
        if not self.queue[max_priority]:
            del self.queue[max_priority]

        return node_index, path, max_priority

    def update_priority(self, node_index, new_priority):

        for priority in self.queue:
            for i, (n_index, path) in enumerate(self.queue[priority]):
                if n_index == node_index:
                    # Remove from old priority level
                    self.queue[priority].pop(i)

                    if not self.queue[priority]:
                        del self.queue[priority]

                    # Add to new priority level with existing path
                    self.insert(node_index, new_priority, path)
                    return
        
    def update_path(self, node_index, new_path):
        """
        Updates the path associated with a given node index.
        """
        for priority in self.queue:
            for i, (n_index, path) in enumerate(self.queue[priority]):
                if n_index == node_index:
                    # Update the path for the node index
                    self.queue[priority][i] = (node_index, new_path)
                    return


    def contains(self, node_index):

        for priority in self.queue:
            for n_index, _ in self.queue[priority]:
                if n_index == node_index:
                    return True
        return False

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        """
        return not bool(self.queue)
    
    def get_priority(self, node_index):
        """
        Gets the priority of a given node index.
        """
        for priority in self.queue:
            for n_index, _ in self.queue[priority]:
                if n_index == node_index:
                    return priority
        
        raise ValueError(f"Node index {node_index} not found in the priority queue")

    def get_path(self, node_index):
        """
        Gets the path associated with a given node index.
        """
        for priority in self.queue:
            for n_index, path in self.queue[priority]:
                if n_index == node_index:
                    return path

        raise ValueError(f"Node index {node_index} not found in the priority queue")
    
    def print_queue(self):
        """
        Prints the current state of the priority queue.
        """
        if not self.queue:
            print("Priority Queue is empty")
        else:
            print("Priority Queue contents:")
            for priority in sorted(self.queue.keys()):
                print(f"Priority {priority}:")
                for node_index, path in self.queue[priority]:
                    print(f"  Node: {node_index}, Path: {path}")