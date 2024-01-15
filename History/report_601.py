# report_601.py

"""
405 : 클래스 적용(220811)
      딕셔너리 대신 클래스 인스턴스를 사용하도록 프로그램 변경
      print메서드를 클래스를 사용하여 일반화한다(220815)
410 : 특수 메서드 적용(220816)
601 : 이터레이션 적용(220817)
"""

import fileparse_404
import tableformat_410
from stock_508 import Stock
from portfolio_601 import Portfolio


def read_portfolio(filename):
    """
    포트폴리오 파일을 읽어서 name, shares, price 키를 가진 딕셔너리의 리스트를 만든다
    클래스 인스턴트로 만든다
    :param filename: 이름, 수량, 매수가격이 기재된 csv파일
    :return portfolio: 이름, 수량, 매수가격으로 구성된 클래스 인스턴트 리스트
    """
    with open(filename) as lines:  # 주어진 파일을 읽어서 lines라 칭한다
        # lines의 각 줄을 읽어서 딕셔너리 리스트로 만든다
        port_dict = fileparse_404.parse_csv(lines,
                                            select=['name', 'shares', 'price'],
                                            types=[str, int, float])
    # 각 딕셔너리 값으로 클래스 인스턴트 리스트를 만든다
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in port_dict]
    return Portfolio(portfolio)  # portfolio는 클래스 인스턴트


def read_prices(filename):
    """
    주어진 파일의 보유 종목 & 현재 가격 읽어서 딕셔너리로 만든다
    :param filename: 보유종목, 현재가격이 기재된 csv 파일
    :return 종목&가격 딕셔너리
    """
    with open(filename) as lines:
        return dict(fileparse_404.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """
    매수정보 리스트(portfolio)와 현재가격정보 딕셔너리(prices)로 부터 튜플 리포트(rows)를 만든다
    :param portfolio: 보유종목의 인스턴트 리스트
    :param prices: 현재가격 딕셔너리
    :return rows: 리포트에 사용할 data 튜플 리스트
    """
    rows = []
    for s in portfolio:  # 각 보유종목에 대해서
        current_price = prices[s.name]  # 현재가격을 구하고
        change = current_price - s.price  # 현재가격 - 매수가격
        summary = (s.name, s.shares, current_price, change)  # 종목, 수량, 현재가격, 변화
        rows.append(summary)  # 전 종목에 대해서
    return rows  # 리포트 data 튜플 리스트


def print_report(reportdata, formatter):
    """
    리포트 data(튜플 리스트)로부터 필요한 내용을 정형화된 형태로 프린트한다
    :param reportdata: 리포트 data 파일
    :param formatter: 프린트 포맷
    :return 없음
    """
    # TableFormatter클래스의 headings메서드 실행, 인스턴스=formatter
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)  # TableFormatter클래스의 row 메소드 실행, 인스턴스=formatter


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    """
    주어진 포트폴리오 파일과 가격 파일을 가지고, 리포트를 만들고 프린트한다
    :param portfoliofile: 포트폴리오 파일
    :param pricefile: 현재가격 파일
    :param fmt: 출력 포맷 이름
    :return 없음
    """
    # 주어진 파일을 읽는다
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # 보고서 데이터 생성
    report = make_report_data(portfolio, prices)

    # 프린트한다
    formatter = tableformat_410.select_formatter(fmt)  # tableformat_410 클래스에서 출력할 포맷 메서드 이름을 얻어온다
    print_report(report, formatter)


def main(args):
    if len(args) != 4:  # 인수 4개(실행파일, 포트폴리오파일, 잔고금액파일, 출력포맷) 아니면 에러 발생
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])  # 인수 4개이면 실행


if __name__ == '__main__':
    import sys  # main이면 sys 임포트
    main(sys.argv)  # main 콜
