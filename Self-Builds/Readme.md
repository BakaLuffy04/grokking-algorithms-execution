# 🛠 Self-Builds

A collection of DIY script / mini‑projects inspired by *Grokking Algorithms*. Each script performs a specific task using Python/NumPy.

---

## 📋 Scripts Overview

| Script Name                   | Description                                              | How to Run                            | Sample Output                                           |
| ----------------------------- | -------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------- |
| `Python_refresher.py`         | Finds all prime numbers less than *n*                    | `python Python_refresher.py <n>`      | `[2, 3, 5, 7, …]`                                       |
| `--`                          | Counts word frequency in a given string                  | `--"`                                 | `{'the': 3, 'cat': 2, …}`                               |
| `array-stats.py`              | Stats on a 5×5 random int array (shape, mean, max, >50)  | `python array-stats.py`               | `Shape: (5,5) Mean: [x,…] Max: y >50: [a, b,…]`         |
| `personal-stats-analyzer.py`  | Logs 10-day bodyweight and sleep stats                   | `python personal-stats-analyzer.py`   | `Mean weight: xx.x, Days with >avg sleep & <avg weight` |
| `compare-progress.py`         | Compares two arrays, outputs "Improved"/"Dropped"/"Same" | `python compare-progress.py` + inputs | `['Improved', 'Same', 'Dropped', …]`                    |
| `bfs-traversal.py`            |	Performs BFS traversal on a graph	                       | `python bfs-traversal.py`             | `BFS Traversal: A -> B -> C -> D …`                     |
| `matrix-calculator.py`        |	Does basic matrix operations: add, multiply, transpose	 | `python matrix-calculator.py`         | `Sum:\n[[...]]\nProduct:\n[[...]]`                      |

---

## 🚀 How to Run

1. **Clone this folder** (or select scripts) to your local machine.
2. **Install dependencies** (only NumPy & optionally Matplotlib):

   ```
   pip install numpy matplotlib
   ```
3. **Run a script** via:

   ```
   python script-name.py [arguments]
   ```

---

## ✅ Sample Outputs

### `compare-progress.py`

```
Enter old marks for 5 subjects: 70 80 90 75 85  
Enter new marks for 5 subjects: 75 80 85 75 90  
-> ['Improved' 'Same' 'Dropped' 'Same' 'Improved']
```

### `personal-stats-analyzer.py` (10‑day data):

```
Mean weight = 95.5 kg  
Max weight = 100 kg  
Std weight = 2.87  
Mean sleep = 5.5 hrs  
Quality days: [1, 2, 3, 4, 5]
```

### `array-stats.py`

```
Array:
[[34 11  5  8  9]
 …]
Shape: (5,5)
Mean: [13.4 53.4 …]
Max: 87
>50: [74 59 …]
```

---
