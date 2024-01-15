# pcost_2.py

import report_3


def portfolio_cost(filename):
    """
    포트폴리오 파일(csv파일)을 읽어서 매수합계를 구하는 함수
    """
    portfolio = report_3.read_portfolio(filename)  # 포트폴리오 파일을 읽는다
    return sum(s['shares'] * s['price'] for s in portfolio)  # 포트폴리오 각 줄에 대해서 "수량*가격"을 모두 더한다


def main(args):  # 메인 함수인 경우만 실행
    if len(args) != 2:  # 인수 2가 아니면 에러 발생
        raise SystemExit('Usage: %s portfoliofile' % args[0])  # 실행하려면 파일 이름이 필요하다
    filename =  args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)
