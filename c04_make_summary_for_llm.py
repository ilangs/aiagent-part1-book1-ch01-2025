# 앞선 결과를 활용하여 **AI Agent 또는 LLM 입력용 요약 데이터**를 하나의 CSV 파일로 생성
# - 전체 대출 건수
# - 가장 많이 대출된 도서명
# - 대출이 가장 많은 분류
# - 대출이 가장 많았던 월
# 결과는 **1행짜리 데이터프레임**으로 구성되어야 합니다.
# 힌트
# 전체 대출 건수는 원본 데이터의 행 개수를 활용합니다.
# 최댓값 추출은 정렬 후 `iloc[0]`을 사용합니다.
# 단일 행 데이터는 `dict → DataFrame` 방식이 가장 간단합니다.
# 결과 파일명 예시: `loan_summary_for_llm.csv`

import pandas as pd
import matplotlib.pyplot as plt

# CSV 읽기
df = pd.read_csv("C:/Users/Donga/Downloads/seoul_library_202511_category.csv", encoding="utf-8-sig")

df.columns

# 전체 대출 건수
total_loans = len(df)   

# 가장 많이 대출된 도서명
most_borrowed_book = df['도서명'].value_counts().idxmax()
# most_borrowed_book_count = df['도서명'].value_counts().max()

# 대출이 가장 많은 분류
most_borrowed_category = df['분류'].value_counts().idxmax()
# most_borrowed_category_count = df['분류'].value_counts().max()  

# # 대출이 가장 많았던 월
# df['대출월'] = pd.to_datetime(df['대출일자']).dt.month
# most_borrowed_month = df['대출월'].value_counts().idxmax()
# most_borrowed_month_count = df['대출월'].value_counts().max()

# 요약 데이터프레임 생성
summary_data = {
    "전체 대출 건수": total_loans,
    "가장 많이 대출된 도서명": most_borrowed_book,
    # "도서명 대출 건수": most_borrowed_book_count,
    "대출이 가장 많은 분류": most_borrowed_category,
    # "분류 대출 건수": most_borrowed_category_count,
    # "대출이 가장 많았던 월": most_borrowed_month,
    # "월별 대출 건수": most_borrowed_month_count
}
summary_df = pd.DataFrame([summary_data])

# CSV로 저장
summary_df.to_csv(
    "C:/workspace/part2/book1/ch01/loan_summary_for_llm.csv",
    index=False, 
    encoding="utf-8-sig"
    )
  