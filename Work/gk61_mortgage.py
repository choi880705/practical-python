# gk61_mortgage.py
#
# Exercise 1.9 & 1.10 & 1.11
"""
Exercise 1.9
추가 납입금을 일반적으로 다룰 수 있게 프로그램을 수정하자. 
사용자가 다음 변수를 설정할 수 있게 한다.
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
프로그램이 이 변숫값을 읽고 총 납입액을 계산하게 해 보자.
데이브가 대출 시작 5 년 후부터 4 년간 매달 1000 달러를 추가로 지불할 경우 총 납입액은 얼마인가?

Exercise 1.10
월수, 현재까지의 납부액, 남은 원금을 나타내는 테이블을 프린트하게 프로그램을 수정해 보라. 다음과
같이 출력한다.

Exercise 1.11
마지막 달에 초과 납부하는 금액이 생기지 않게 프로그램을 수정해 보라.
"""


# 변수선언 및 초기화
principal = 500000.0  # 원금
rate = 0.05  # 년이자
payment = 2684.11  # 월납입금
total_paid = 0.0  # 총납입금
extra_payment_start_month = 61  # 추가납입 시작하는 달
extra_payment_end_month = 108  # 추가납입 끝나는 달
extra_payment = 1000  # 추가납입금
paid_month = 0  # 상환개월

# 월 상환금액 = (대출 원금 × 월 이자율) / (1 - (1 + 월 이자율)^(-상환 기간))

while principal > 0:
    if principal < payment:  # 1개월 상환금보다 적게 남았으면 그것만 납부
        total_paid += principal
        principal -= principal
    else:  # 1개월 상환금 이상 남았으면 정해진 금액을 상환
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment
    paid_month += 1  # 상환개월증가

    # 추가 상환금을 처리
    if extra_payment_start_month <= paid_month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print("납입회차: ", paid_month, end=", ")
    print("총납입금: ", round(total_paid, 2), end=", ")
    print("남은원금: ", round(principal, 2))

print()
print()
print()
