# pcost.py
#
# Exercise 1.27

"""
portfolio.csv의 각 컬럼은 보유 종목의 이름, 주식 수, 매수가격에 해당한다. 
이 파일을 열어 전체 행을 읽은 뒤, 포트폴리오의 전체 주식을 매수하는 데 드는 비용을 계산하는 
pcost.py 프로그램을 작성한다.
"""

with open("data/portfolio.csv", "rt") as file:
    cost = 0
    headers = next(file)  # 헤더 추출
    for line in file:
        # print(line)
        row = line.split(",")
        # print(row)
        cost += int(row[1]) * float(row[2])
        # print(cost)
    print("Total cost", cost)
