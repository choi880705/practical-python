# report_1.py

import csv
from collections import Counter
from typing import Any


def read_portfolio_1(filename: str) -> list:
    """
    주식 포트폴리오 파일(csv파일)에서 이름, 수량, 가격 데이터를 읽어서
    [{이름, 수량, 가격}, ...] 딕셔너리의 리스트를 생성
    :param filename:
    :return portdolio_list:
    """

    portfolio_list = []  # 결과값을 리스트로 반환

    with open(filename, 'rt') as f:  # 파일을 열고
        rows = csv.reader(f)  # 저장
        headers = next(rows)  # 첫줄은 headers로 넘기고

        for row in rows:  # 파일의 각 라인에 대해 딕셔너리를 만든다
            stock_dict = {'name': row[0],  # 첫번째 키 = name
                          'shares': int(row[1]),  # 두번째 키 = shares
                          'price': float(row[2])  # 세번째 키 = price
                          }
            portfolio_list.append(stock_dict)  # 만든 딕셔너리를 리스트 추가한다

    return portfolio_list  # 리스트 = [{딕3}, {딕3}, ..., {딕3}] 형태


def read_portfolio_2(filename: str)-> list:
    """
    포트폴리오 파일(csv파일)을 읽어서 [{이름, 수량, 가격}, ...] 딕셔너리 리스트를 생성
    :param filename:
    :return portdolio_list:
    """

    portfolio_list = []  # 결과값을 리스트로 반환

    with open(filename, 'rt') as f:  # 파일을 열고
        rows = csv.reader(f)  # 저장
        headers = next(rows)  # 첫줄은 headers로 넘기고

        for row in rows:  # 파일의 각 라인에 대해 딕셔너리를 만든다
            row_dict = dict(zip(headers, row))  # 제목과 티커를 합쳐 딕셔너리로 만든다
            stock_dict = {'name': row_dict['name'],  # 첫번째 키 = name
                          'shares': int(row_dict['shares']),  # 두번째 키 = shares
                          'price': float(row_dict['price'])  # 세번째 키 = price
                          }
            portfolio_list.append(stock_dict)  # 만든 딕셔너리를 리스트에 추가한다

    return portfolio_list  # 리스트 = [{딕3}, {딕3}, ..., {딕3}] 형태


def read_prices(filename: str)-> dict:
    """
    현재가격 파일(csv파일)을 읽어서 {티커:가격, 티커:가격,...} 딕셔너리를 생성
    :param filename:
    :return price_dict:
    """

    prices_dict = {}  # 결과값을 딕셔너리로 반환

    f = open(filename, 'r')  # 파일을 열고
    rows = csv.reader(f)  # 저장

    for row in rows:  # 파일의 각 라인에 대해서 딕셔너리를 만든다.
        try:
            prices_dict[row[0]] = float(row[1])  # 종목 : 가격
        except IndexError:  # 에러가 발생하면 처리
            pass

    return prices_dict  # 딕셔너리 = {티커:가격, 티커:가격, ..., 티커:가격}


def make_report(portfolio: list, prices: dict) -> list:
    """
    포트폴리오 리스트와 현재가격 딕셔너리를 입력받아 Name, Shares, Price, Current Price, Change 튜플 리스트 생성
    :param portfolio:
    :param prices:
    :return:
    """

    rows_list = []  # name, shares, price, current_price, change 튜풀로된 리스트

    for stock in portfolio:  # 포트폴리오의 각 종목에 대해
        current_price = prices[stock['name']]  # 현재가격 = 선택한 티커의 현재 가격
        change = current_price - stock['price']  # 변화 = 현재 가격 - 구입 가격
        summary = (stock['name'], stock['shares'], stock['price'], current_price, change)
        rows_list.append(summary)  # 보유 종목 모두 리스트에 넣는다

    return rows_list  # 보유종목 구입가격, 현재가격, 변화 리스트


def print_report(reportdata: list) -> None:
    """
    포맷팅을 이용하여 출력을 보기 좋게 만든다
    """
    headers = ('Name', 'Shares', 'Price', 'Current Price', 'Change')  # 제목줄 이름
    print('%10s %10s %10s %15s %10s' % headers)  # 10문자 10문자 10문자 15문자 10문자 크기 지정
    print(('-' * 10 + ' ') * len(headers))  # -- 표시
    for row in reportdata:
        print('%10s %10d %10.2f %15.2f %10.2f' % row)

    return


def make_total_cost(portfolio: list) -> list:
    """
    포트폴리오 매수가격을 계산
    :param portfolio:
    :return:
    """
    total_cost = 0.0  # 매수가격 초기화
    for s in portfolio:  # 각 보유 종목에 대하여
        total_cost += s['shares'] * s['price']  # "수량*가격"을 모두 더한다

    return total_cost


def make_total_value(portfolio: list, prices: dict) -> list:
    """
    포트폴리오와 현재가격으로부터 현재가치를 계산
    :param portfolio:
    :param prices:
    :return total_value:
    """

    total_value = 0.0  # 현재가격 초기화
    for s in portfolio:  # 각 보유 종목에 대하여
        total_value += s['shares'] * prices[s['name']]  # "보유종목 수량 * 현재가격"을 모두 더한다

    return total_value


def make_holdings(portfolio: list) -> Counter[Any]:
    """
    보유 종목별 보유 수량 계산

    :param portfolio: 
    :return: 
    """

    from collections import Counter  # collection모듈의 Counter함수 import

    holdings_dict = Counter()  # 합계결과를 딕셔너리로 저장
    for s in portfolio:  # 각 종목에 대하여
        holdings_dict[s['name']] += s['shares']  # 종목의 수량을 더한다

    return holdings_dict


# 함수는 여기부터 실행된다.
# portfolio_list = read_portfolio_1('Data/portfolio.csv')  # 파일 읽어서 포트폴리오 리스트 만든다
portfolio_l = read_portfolio_2('Data/portfoliodate.csv')  # 파일 읽어서 포트폴리오 리스트 만든다
prices_d = read_prices('Data/prices.csv')  # 파일 읽어서 현재 가격 딕셔너리 만든다
# report_list = make_report(portfolio_list, prices_dict)  # 포트폴리오에 대한 현재가격, 변화를 튜플 리스트로 만든다
report_l = make_report(portfolio_l, prices_d)  # 포트폴리오에 대한 현재가격, 변화를 튜플 리스트로 만든다
total_cost = make_total_cost(portfolio_l)  # 매수가격 계산
total_value = make_total_value(portfolio_l, prices_d)  # 현재가치 계산
holdings = make_holdings(portfolio_l)  # 종목별 보유수량 계산

print_report(report_l)
print(f'매수가격 {total_cost:0.2f}')
print(f'현재가격 {total_value:0.2f}')
print(f'손익 {total_value - total_cost:0.2f}')
print(f'종목별 총주식수량 {holdings}')
