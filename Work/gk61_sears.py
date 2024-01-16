"""
[page17 예제 프로그램]_V0_240116
어느 날 아침, 당신은 시카고의 시어스 타워 (Sears tower) 근처를 거닐다가 보도에 1 달러 지폐를 한
장 올려뒀다. 그 후 매일 외출할 때마다 그 위에 지폐를 얹어 탑을 쌓으며, 높이는 매일 두 배로 불어
난다. 돈으로 쌓은 탑의 높이가 시어스 타워의 높이와 같아지려면 시간이 얼마나 걸릴까?
"""
# 변수 선언 및 초기화
BILL_THICKNESS = 0.11 * 0.001  # 지폐의 두께(0.11mm)를 미터로 환산(상수=대문자)
SEARS_HEIGHT = 442  # sears 빌딩의 높이 (상수변수는 변수이름을 대문자로 쓴다)
num_bills = 1  # 지폐 갯수, 처음에는 1
day = 1  # 지폐 추가한 일자, 첫날은 1

while num_bills * BILL_THICKNESS < SEARS_HEIGHT:
    # "지폐갯수 * 지폐1장 높이"가 sears빌딩 높이보다 작으면 아래 문장을 실행
    print(day, num_bills, num_bills * BILL_THICKNESS)  # 누적일수, 누적지폐갯수, 누적지폐높이
    day = day + 1  # 일수를 1증가
    num_bills = num_bills * 2  # 추가해야 할 지폐갯수는 2배로 증가
# "지폐갯수 * 지폐1장 높이"가 sears빌딩 높이보다 크면 아래 문장을 실행
print("Number of days", day)  # 지폐 추가한 일자
print("Number of bills", num_bills)  # 총 지폐 갯수
print("Final height", num_bills * BILL_THICKNESS)  # 쌓은 지페의 높이
