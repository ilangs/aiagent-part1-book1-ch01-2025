# 파이썬 리스트 ----------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

total = 0
for n in numbers:
    total += n

print("리스트 합계:", total)

# NumPy 배열 -------------------------------------------------------------

import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print("NumPy 합계:", np.sum(numbers))

# NumPy 배열 -------------------------------------------------------------

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print("배열 평균:", np.mean(arr))
print("배열 합계:", np.sum(arr))

# Pandas DataFrame --------------------------------------------------------

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)

print("평균 점수:", df["score"].mean())
print("최고 점수:", df["score"].max())

# matplotlib 시각화 --------------------------------------------------------

import matplotlib.pyplot as plt

plt.bar(df["name"], df["score"])
plt.title("Student Scores")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()
