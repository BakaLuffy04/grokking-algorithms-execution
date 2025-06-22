# Problem: 206. Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/description/
# Difficulty: Easy

def reverseList(self, head):
        newhead = []
        if not head or not head.next:
            newhead = head
        else:
            newhead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newhead
        
