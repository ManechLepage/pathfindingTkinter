import heapq


class Node:
    def __init__(self, x, y, cost, parent):
        # The x and y position of the node
        self.x = x
        self.y = y
        # The cost of the node
        self.cost = cost
        # The parent of the node
        self.parent = parent

    def __lt__(self, other):
        # This is used to compare the nodes in the heap
        return self.cost < other.cost


def find_path(grid, start, end):
    # Creating the start and end node with the Node() class
    start = Node(start[0], start[1], 0, None)
    end = Node(end[0], end[1], 0, None)
    # Creating the empty heap (open list)
    heap = []
    # Add the start to the heap
    heapq.heappush(heap, (0, start))
    # Creating the empty visited set
    visited = set()
    # While the open list is not empty
    while heap:
        # Get the node with the lowest cost in the open list
        current_cost, current_node = heapq.heappop(heap)
        # If the node is already visited, skip it
        if (current_node.x, current_node.y) in visited:
            continue
        # Add the node to the visited set
        visited.add((current_node.x, current_node.y))
        # If the node is the end node, the path is found and return the path
        if current_node.x == end.x and current_node.y == end.y:
            path = []
            # Backtrack the path by using the parent attribute of the nodes
            while current_node is not None:
                # Append the node to the path
                path.append((current_node.x, current_node.y))
                # Go to the parent node
                current_node = current_node.parent
            # Return the reversed path and the visited set
            return [path[::-1], visited]
        # Loop through the neighbors of the current node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # Get the neighbor coordinates
            x, y = current_node.x + dx, current_node.y + dy
            # Checking if the neighbor is inside the grid and if it is not a wall
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
                # Calculating the cost of the neighbor and updating it
                new_cost = current_cost + 1
                # If the neighbor is not in the open list, add it
                heapq.heappush(heap, (new_cost, Node(x, y, new_cost, current_node)))
    # If the open list is empty, the path is not found and return None
    return None
