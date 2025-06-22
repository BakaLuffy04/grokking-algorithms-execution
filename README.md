
# 💻 LeetCode Solutions by Sparsh Jindal

This repository contains my personal solutions to problems from [LeetCode](https://leetcode.com/), written as part of my data structures and algorithms learning journey. Each solution is written clearly with a focus on readability and efficiency.

---

## 🧠 What's Inside?

- 📝 **Descriptive filenames**: Each file starts with the problem number and name for easy reference.
- 🚀 Regular updates as I continue to practice and improve.

---

## 🧾 Code Snippet Format

Each solution follows this consistent structure:

```python
# Problem: 704. Binary Search
# Link: https://leetcode.com/problems/binary-search/description/
# Difficulty: Easy

def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                high = mid-1
            else:
                low = mid+1
        return -1
```

* **Header**: Problem title, link, difficulty.
* **Clean function** with variable names and logic clearly outlined.

---

## 🔗 Connect

If you want to discuss DSA, algorithms, or projects, feel free to connect:

* **LeetCode**: [My Profile](https://leetcode.com/u/pXhYyQZYwV/)
* **GitHub**: [Sparsh Jindal](https://github.com/BakaLuffy04)


*Stay consistent. One question a day keeps confusion away* 🚀
