# pcost_1.py
"""
포트폴리오 파일(csv파일)을 읽어서 매수합계를 구하는 함수
"""
import csv


def portfolio_cost(filename):
    """
    포트폴리오 파일(csv파일)을 읽어서 매수합계를 구하는 함수
    """
    total_cost = 0.0  # 매수합계를 float로 반환

    with open(filename, 'rt') as f:  # 파일을 열고
        rows = csv.reader(f)  # 임시 저장
        headers = next(rows)  # 첫줄(name, shares, price)은 headers
        for rowno, row in enumerate(rows, start=1):  # 파일의 각 라인에 대해
            record_dict = dict(zip(headers, row))  # 각 줄의 항목에 제목을 붙여 딕셔너리로 만든다
            # {'name': '티커', 'shares': '수량', 'price': '가격'}
            try:
                nshares = int(record_dict['shares'])  # 딕셔너리의 shares키 값은 정수로 nshares에 저장
                price = float(record_dict['price'])  # 딕셔너리의 price키 값은 플로팅으로 price에 저장
                total_cost += nshares * price  # nshares * price를 전체 더한다.(전체 종목 매수가격합계 계산)

            except ValueError:  # 에러가 발생하면 처리
                print(f"Row {rowno}: Couldn't convert : {row}")

    return total_cost
