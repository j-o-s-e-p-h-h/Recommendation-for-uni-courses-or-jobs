from collections import deque

def breadth_first_search(root_node, goal_value):
    #queue for first in first out principle
    frontier_queue = deque()

    #adding root to queue
    path = [root_node]
    frontier_queue.append(path)

    while frontier_queue:
        current_path = frontier_queue.pop()
        current_node = current_path[-1]

        #checking if it is the goal