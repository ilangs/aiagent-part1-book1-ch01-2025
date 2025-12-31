# 도서 대출 CSV 파일에서 **대출 건수가 가장 많은 도서 10권**을 찾아 대출 건수 기준 내림차순으로 정렬
# 결과는 데이터프레임 형태로 정리하고 CSV 파일로 저장하십시오.
# 결과 데이터는 다음 컬럼을 포함해야 합니다.
# 컬럼명	설명
# 도서명	도서 제목
# 대출건수	해당 도서의 전체 대출 횟수

import pandas as pd

df = pd.read_csv(
    "C:/Users/Donga/Downloads/seoul_library_202511.csv",
    encoding="utf-8-sig"
)

df.columns

loan_counts = df['도서명'].value_counts()

top10_books = loan_counts.head(10)
top10_books

top10_df = top10_books.reset_index()
top10_df.columns = ['도서명', '대출건수']
top10_df

top10_df.to_csv(
    "C:/workspace/part2/book1/ch01/top10_books_by_loan.csv",
    index=False,
    encoding="utf-8-sig"
)

