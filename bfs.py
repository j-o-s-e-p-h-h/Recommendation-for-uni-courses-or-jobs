from collections import deque

def breadth_first_search(start_node, target_name):
    queue = deque()
    queue.append(start_node)

    target_name = target_name.lower()

    while queue:
        current_node = queue[0]

        if current_node.name.lower() == target_name:
            return current_node
        
        for child in current_node.children:
            queue.append(child)

    return None