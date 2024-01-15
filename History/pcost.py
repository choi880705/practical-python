# pcost.py
"""
포트폴리오 파일(csv파일)을 읽어서 매수합계(수량*매수가격)를 구하는 함수
첫번째 작성
"""
import csv


def portfolio_cost(filename):

    total_cost = 0.0  # 매수합계를 float로 반환

    with open(filename, 'rt') as f:  # 1: 파일을 열고
    
        # 2: 읽은 파일을 rows에 저장
        rows = csv.reader(f)  # 임시 저장

        # 3: 첫번째 줄(name, shares, price)은 headers에 저장
        headers = next(rows)
        
        # 4: 2번째 줄부터 끝까지 매수금액을 계산
        for rowno, row in enumerate(rows, start=1):  # 파일의 각 라인에 대해
            # 4-1: 줄의 각 항목에 제목을 붙여 딕셔너리로 만들어 record_dict에 저장
            record_dict = dict(zip(headers, row))  # {'name': '티커', 'shares': '수량', 'price': '가격'}
            # 4-2: 저장된 수량과 가격을 곱해서 누적으로 더한다
            try:
                nshares = int(record_dict['shares'])  # 딕셔너리의 shares키 값은 정수로 nshares에 저장
                price = float(record_dict['price'])  # 딕셔너리의 price키 값은 플로팅으로 price에 저장
                total_cost += nshares * price  # nshares * price를 전체 더한다.(전체 종목 매수가격합계 계산)

            except ValueError:  # 에러가 발생하면 처리
                print(f"Row {rowno}: Couldn't convert : {row}")
    # 5: 계산값을 리턴한다.
    return total_cost
