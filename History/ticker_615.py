# ticker_612.py

"""
https://wikidocs.net/84424

[612]   이터레이터 적용
[615]   제너레이터 표현식 적용

"""


import csv
import report_601
import tableformat_410
from follow_607 import follow
import time


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


# 딕셔너리로 변환
def make_dicts(rows, headers):
    # for row in rows:  # 이터레이터
    #     yield dict(zip(headers, row))
    return (dict(zip(headers, row)) for row in rows)  # (220904) 리스트 컴프리헨션 스타일의 제너레이터 표현식


# 종목, 현재가, 변동을 딕셔너리로 만든다
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


# 주어진 name의 줄을 반환
# (220904) 제너레이터 표현식으로 직접 사용하여 이것은 사용하지 않게 되었다.
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def ticker(portfile, logfile, fmt):
    portfolio = report_601.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    # rows = filter_symbols(rows, portfolio)
    rows = (row for row in rows if row['name'] in portfolio)  # filter_symbol 메소드를 제너레이터 표현식으로 변경
    formatter = tableformat_410.select_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
