# pcost_601.py

"""
404 : 클래스 적용(220811)
      딕셔너리 대신 클래스 인스턴스를 사용하도록 프로그램 변경
508 : 데코레이션(프로퍼티, setter) 적용(220817)
601 : 이터레이션 적용(220817)
"""

import report_601


def portfolio_cost(filename):
    """
    포트폴리오 파일을 읽어서 매수합계를 구하는 함수
    :param filename: 포트폴리오 csv 파일
    :return 보유종목 현재값 합계
    """
    portfolio = report_601.read_portfolio(filename)  # 포트폴리오 파일을 읽어서 인스턴스 리스트로 만든다
    return portfolio.total_cost  # 포트폴리오 각 인스턴스에 대해서 "수량*가격"을 모두 더한다


def main(args):  # 메인 함수인 경우만 실행
    if len(args) != 2:  # 인수 2가 아니면 에러 발생
        raise SystemExit('Usage: %s portfoliofile' % args[0])  # 실행하려면 파일 이름이 필요하다
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)
