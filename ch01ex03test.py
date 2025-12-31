import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print("np.__version__:", np.__version__)
# print("pd.__version__:", pd.__version__)
# print("Matplotlib OK")


num_list = [1, 2, 3, 4, 5]
print(num_list)  # 파이썬 기본 리스트
data = np.array(num_list) 
print(data) # 넘파이 array (배열)
# 넘파이 Array에는 여러가지 집계함수가 포함되어 있다.
print(data.mean()) # 넘파이 array의 평균
print(data.max()) # 넘파이 array의 최대값