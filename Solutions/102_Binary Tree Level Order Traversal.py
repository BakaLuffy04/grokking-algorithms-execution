# Problem: 102. Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Difficulty: Medium

def levelOrder(self, root):
        # If the tree is empty, return an empty list
        if not root:
            return []
        bfs = []   # This will store the final result with level-wise nodes
        queue = deque([root]) # Initialize the queue with the root node

        # Process nodes level by level until the queue is empty
        while queue:
            level = []  # This list will hold the nodes of the current level

            # Process all nodes in the current level
            for i in range(len(queue)):  # Loop for the number of nodes at the current level
                node = queue.popleft()  # Pop the front node from the queue
                level.append(node.val)  # Add the node's value to the level list
                
                # If the node has a left child, add it to the queue
                if node.left:
                    queue.append(node.left)
                
                # If the node has a right child, add it to the queue
                if node.right:
                    queue.append(node.right)
            
            # After processing all nodes at the current level, add the level list to the bfs
            bfs.append(level)
        
        # Return the result after processing all levels
        return bfs
