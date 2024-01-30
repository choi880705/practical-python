# pcost.py
#
# Exercise 1.30

"""
연습 문제 1.27의 pcost.py 프로그램 코드를 가져다가 portfolio_cost(filename) 함수를 만들어 보라. 
이 함수는 파일명을 입력으로 받아 포트폴리오 데이터를 읽고, 포트폴리오의 총 비용을 부동소수점으로 반환한다.
"""


def portfolio_cost(filename):
    """매수 파일을 열어서, 매수금액을 계산

    Args:
        filename (file): 매수 정보가 들어있는 파일
    """
    with open(filename, "rt") as f:
        cost = 0
        headers = next(f).split(",")  # 헤더 추출, 분리
        for line in f:  # 모든 라인 처리
            row = line.split(",")  # 티커, 수량, 가격
            cost += int(row[1]) * float(row[2])  # 수량 * 가격
    return cost


cost = portfolio_cost("data/portfolio.csv")
print("Total cost:", cost)
