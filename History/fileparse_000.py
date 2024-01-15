# fileparse_000.py

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
     CSV 파일을 파싱해 형변환된 목록 리스트 생성
    :param filename: csv파일
    :param select: 컬럼 선택 ( 컬럼 이름)
    :param types: 선택한 컬럼을 목적에 맞게 형변환 (str, int, float)
    :param has_headers: 헤더 유무 (True, False) - 헤더는 컬럼의 제목에 해당한다. 제목이 없으면 False
    :param delimiter: 컬럼 구분자 (쉼표, 공백등) - csv 파일의 구분자를 지정한다
    :param silence_errors: 에러 체크 - 에러가 발생하였을 경우 어떻게 처리할 것인지를 결정
    :return records: 딕셔너리 또는 튜플 리스트 - 헤더가 있으면 헤더:값 형식의 딕셔너리로 반환, 헤더가 없으면 튜플로 반환
    """
    # 1: "헤더가 없는데 헤더를 선택"의 경우 에러를 발생시키고 종료한다
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    # 2: csv파일을 열고
    with open(filename) as f:
        # 3: 구분자를 확인해서 읽는다
        rows = csv.reader(f, delimiter=delimiter)

        # 4: 헤더가 있다면 첫줄을 읽어서 headers에 저장, 헤더가 없으면 공란
        headers = next(rows) if has_headers else []  # 여기의 headers에는 (선택되지 않은 것을 포함한 모든) 헤더가 저장된다

        # 5: 컬럼이 선택되었다면, 지정한 컬럼의 인덱스(컬럼번호)들을 찾아서 indices에 저장한다
        if select:
            indices = [headers.index(colname) for colname in select]  # 선택한 컬럼명을 컬럼 인덱스에 매핑
            headers = select  # 여기의 headers에는 선택된 헤더만 저장한다

        # 6: 반환할 변수를 초기화
        records = []  # 딕셔너리 또는 튜플 리스트
        
        # 7: 데이터 작업
        for rowno, row in enumerate(rows, 1):  # 각 줄에 대해서 아래 작업을 진행
            
            # 7-1: 데이터가 없는 행은 건너 뛰도록 처리
            if not row:
                continue

            # 7-2: 특정 컬럼이 선택되었으면 필터링하고, 선택이 없으면 모든 컬럼을 사용한다
            if select:
                row = [row[index] for index in indices]  # 매핑된 인덱스에 해당하는 컬럼만 선택

            # 7-3: type이 지정되어 있으면 형변환하고, 없으면 str로 처리
            if types:
                try:  # 해당줄에 이상이 없으면 실행
                    row = [func(val) for func, val in zip(types, row)]  # type과 컬럼을 묶고, 각 묶음에 대해 형변환
                except ValueError as e:  # 이상이 있으면, 예외처리
                    if not silence_errors:  # 에러 표시 원하면 아래 내용 프린트
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue  # 에러 유무에 관계없이 계속 진행

            # 7-4: 헤더가 있으면 딕셔너리로, 없으면 튜플로 저장
            if headers:
                record = dict(zip(headers, row))  # 헤더와 각줄의 내용을 딕셔너리로 묶는다
            else:
                record = tuple(row)  # 각 줄을 튜플로 만든다

            # 7-5: 데이터를 records에 계속 추가
            records.append(record)  # 모든 줄을 딕셔너리 또는 튜플 리스트로 만든다

    return records
