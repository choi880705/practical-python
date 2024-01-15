# tableformat_410.py
"""
405 : 클래스 적용(220815)
410 : 사용자 정의 어트리뷰트를 보여주는 테이블을 만든다. getattr 적용(220816)
"""


class TableFormatter:
    def headings(self, headers):
        """
        테이블 헤딩을 반환
        :param headers:
        :return:
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        테이블 데이터의 단일 행을 반환
        :param rowdata:
        :return:
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    테이블을 일반 텍스트 포맷으로 출력
    """
    def headings(self, headers):
        """
        받은 헤더를 텍스트 포맷으로 인쇄
        :param headers: 헤더(컬럼) 이름들
        :return: 없다. 프린트한다
        """
        for h in headers:  # 각 컬럼 모두에 대해서 프린트
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        """
        출력하려는 데이터 한줄을 텍스트 포맷으로 인쇄
        :param rowdata: 데이터 한줄(인스턴스)
        :return: 없다. 프린트한다
        """
        for d in rowdata:  # 각 줄의 항목에 대해서 프린트
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    포트폴리오 데이터를 CSV 포맷으로 출력
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    포트폴리오 데이터를 HTML 포맷으로 출력
    """
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<tr>{h}</tr>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<tr>{d}</tr>', end='')
        print('</tr>')


class FormatError(Exception):
    """
    없는 포맷의 경우 pass한다
    """
    pass


def select_formatter(name):
    """
    출력 포맷을 선택
    :param name: 출력 포맷 이름
    :return: 포맷 메서드 이름
    """
    if name == 'txt' or name == 'TXT':
        return TextTableFormatter()
    elif name == 'csv' or name == 'CSV':
        return CSVTableFormatter()
    elif name == 'html' or name == 'HTML':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')


def print_table(objects, colnames, formatter):
    """
    데이터중 선택한 컬럼만 프린트
    :param objects: 프린트할 데이터
    :param colnames: 프린트할 컬럼 이름
    :param formatter: 출력 포맷 메서드 이름
    :return: 없다
    """
    formatter.headings(colnames)  # 지정한 colnames를 지정된 포맷으로 프린트
    for obj in objects:  # 프린트할 모든 줄(종목, 인스턴스, 객체)에 대해서
        rowdata = [str(getattr(obj, name)) for name in colnames]  # 인쇄할 줄 데이터 추출
        formatter.row(rowdata)  # 추출한 데이터를 프린트
