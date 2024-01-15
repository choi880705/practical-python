# fileparse_404.py

"""
fileparse_318과 동일하다
"""

import csv


def parse_csv(lines,
              select=None,
              types=None,
              has_headers=True,
              delimiter=',',
              silence_errors=False):
    """
    여러 형태의 파일을 파싱해 형변환된 목록 리스트 생성
    csv파일뿐만 아니라, zip파일 또는 텍스트 스트링도 입력이 가능하다
    :param lines: 여러 형태의 파일을 읽은 것
    :param select: 컬럼 선택 ( 컬럼 이름)
    :param types: 형변환 (str, int, float)
    :param has_headers: 헤더 유무 (True, False)
    :param delimiter: 컬럼 구분자 (쉼표, 공백등)
    :param silence_errors: 에러 체크
    :return records: 딕셔너리 또는 튜플 리스트
    """
    # "헤더가 없다 & 헤더를 선택한다"의 경우 에러발생
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    # 구분자를 확인해서 읽는다
    rows = csv.reader(lines, delimiter=delimiter)

    # 헤더를 읽음, 헤더가 없으면 공란
    headers = next(rows) if has_headers else []

    # 컬럼 선택기가 주어지면, 지정한 컬럼의 인덱스를 찾는다.
    if select:
        indices = [headers.index(colname) for colname in select]  # 선택한 컬럼명을 컬럼 인덱스에 매핑
        headers = select

    records = []  # 딕셔너리 또는 튜플 리스트
    for rowno, row in enumerate(rows, 1):  # 각 줄에 대해서
        if not row:  # 데이터가 없는 행을 건너뜀
            continue

        # 특정 컬럼이 선택되었으면 필터링하고, 선택이 없으면 모든 컬럼을 사용한다
        if select:
            row = [row[index] for index in indices]  # 매핑된 인덱스에 해당하는 컬럼만 선택

        # type이 지정되어 있으면 형변환하고, 없으면 원본대로
        if types:
            try:  # 해당줄에 이상이 없으면 실행
                row = [func(val) for func, val in zip(types, row)]  # type과 컬럼을 묶고, 각 묶음에 대해 형변환
            except ValueError as e:  # 이상이 있으면, 예외처리
                if not silence_errors:  # 에러 표시 원하면 아래 내용 프린트
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue  # 에러 유무에 관계없이 계속 진행

        # 헤더가 있으면 딕셔너리로, 없으면 튜플로 저장
        if headers:
            record = dict(zip(headers, row))  # 헤더와 각줄의 내용을 딕셔너리로 묶는다
        else:
            record = tuple(row)  # 각 줄을 튜플로 만든다

        records.append(record)  # 모든 줄을 딕셔너리 또는 튜플 리스트로 만든다

    return records
