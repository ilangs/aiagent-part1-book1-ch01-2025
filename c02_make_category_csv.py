# 도서 분류 컬럼을 기준으로 다음 정보를 집계하십시오.
# - 분류별 전체 대출 건수
# - 분류별 평균 대출 건수
# 집계 결과는 **대출 건수 기준 내림차순**으로 정렬되어야 하며, CSV 파일로 저장되어야 합니다.
# 결과 데이터 예시는 다음과 같습니다.
# | 분류 | 대출건수합계 | 평균대출건수 |


import pandas as pd

# CSV 읽기
df = pd.read_csv("C:/Users/Donga/Downloads/seoul_library_202511.csv", encoding="utf-8-sig")

df.columns

# 분류 매핑
category_map = {
    '0': '총류', '1': '철학', '2': '종교', '3': '사회과학', '4': '자연과학',
    '5': '기술과학', '6': '예술', '7': '어학', '8': '문학', '9': '역사'
}

# 분류 컬럼 생성
df['분류'] = df['주제분류번호'].astype(str).str[0].map(category_map)
# CSV 저장
df.to_csv("C:/Users/Donga/Downloads/seoul_library_202511_category.csv", index=False, encoding="utf-8-sig")


# 분류별 대출건수 집계 (합계 & 평균)
summary = df.groupby('분류')['대출건수'].agg(
    대출건수합계='sum',
    평균대출건수='mean'
).reset_index()

# 대출건수합계 기준 내림차순 정렬
summary = summary.sort_values('대출건수합계', ascending=False)

# CSV 저장
summary.to_csv("loan_by_category.csv", index=False, encoding="utf-8-sig")

print(summary)