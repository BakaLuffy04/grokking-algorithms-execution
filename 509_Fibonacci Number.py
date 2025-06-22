# Problem: 509. Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/description/
# Difficulty: Easy

class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

        
