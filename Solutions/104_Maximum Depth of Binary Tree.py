# Problem: 104. Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Difficulty: Easy

def maxDepth(self, root):
        count = 0
        if not root:
            return 0
        q = [root]
        while q:
            count= count+1
            li=[]
            for i in q:
                if i.left:
                    li.append(i.left)
                
                if i.right:
                    li.append(i.right)
            q = li
        return count
