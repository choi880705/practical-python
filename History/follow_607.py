# follow_607.py

"""
https://wikidocs.net/84423
607: log 파일을 열고 파일의 끝에 새로운 출력이 있는지 감시(watch)하는 프로그램


"""

import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    f = open('data/stocklog.csv')
    f.seek(0, os.SEEK_END)  # 파일 포인터를 파일의 끝으로부터 0 바이트 이동

    while True:
        line = f.readline()  # 파일의 마지막 줄을 읽어 line에 저장
        if line == '':  # 마지막 줄이 공란이면
            time.sleep(0.1)  # 0.1초 쉬었다가 다시 시도
            continue
        yield line  # 제너레이터


# Example use
if __name__ == '__main__':
    import report_601

    portfolio = report_601.read_portfolio('../../Data/portfolio.csv')

    for line in follow('../../Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')