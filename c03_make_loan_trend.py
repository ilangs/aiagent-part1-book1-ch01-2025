# 대출일자 컬럼을 활용하여 **월별 대출 건수 추이 그래프**를 작성 (선 그래프)
# 대출일 컬럼을 `datetime` 타입으로 변환합니다.
# `dt.to_period("M")` 또는 `dt.strftime("%Y-%m")`을 사용해 월 단위로 변환합니다.
# 월 단위로 `groupby()` 집계를 수행합니다.
# `matplotlib`을 사용해 선 그래프를 생성합니다.
# x축은 월, y축은 대출 건수로 설정합니다.

import pandas as pd
import matplotlib.pyplot as plt

# CSV 읽기
df = pd.read_csv("C:/Users/Donga/Downloads/seoul_library_202511.csv", encoding="utf-8-sig")

df.columns

# 대출일 컬럼을 datetime 타입으로 변환
df['대출일자'] = pd.to_datetime(df['대출일자']) 
df['대출월'] = df['대출일자'].dt.to_period('M')

# 월별 대출 건수 집계
loan_trend = df.groupby('대출월').size()
loan_trend

# 선 그래프 작성
plt.figure()
loan_trend.plot(kind='line', marker='o')    
plt.title('월별 대출 추이')
plt.xlabel('월') 
plt.ylabel('대출 건수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()    
