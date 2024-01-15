# tableformat_405.py

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
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
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


def create_formatter(name):
    """
    주어진 포맷으로 출력을 결정
    :param name: 출력 포맷 이름
    :return: 포맷함수이름
    """
    if name == 'txt' or name == 'TXT':
        return TextTableFormatter()
    elif name == 'csv' or name == 'CSV':
        return CSVTableFormatter()
    elif name == 'html' or name == 'HTML':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')
