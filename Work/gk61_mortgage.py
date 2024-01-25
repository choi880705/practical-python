# gk61_mortgage.py
#
# Exercise 1.8
"""
데이브가 처음 12 개월 동안 매달 1000 달러를 추가로 납입한다면 어떻게 될까?
이 추가 납입금 계산을 포함하도록 프로그램을 수정해 총 납입금액과 소요 월수를 프린트해보자.
프로그램을 실행했을 때 총 납입금이 929,965.62, 소요 월수는 342 로 나와야 한다.
"""


# 변수선언 및 초기화
principal = 500000.0  # 원금
rate = 0.05  # 년이자
payment = 2684.11  # 월납입금
total_paid = 0.0  # 총납입금
payment_add = 1000  # 추가납입금
mon_add = 12  # 추가납입개월
mon_paid = 0  # 상환개월

# 월 상환금액 = (대출 원금 × 월 이자율) / (1 - (1 + 월 이자율)^(-상환 기간))

while principal > 0:
    principal = principal * (1 + rate / 12) - (payment + payment_add)  # 추가납입
    total_paid = total_paid + (payment + payment_add)
    mon_add -= 1  # 지정한 개월만큼만 추가납입
    mon_paid += 1  # 납입개월증가
    if mon_add <= 0:  # 지정한 개월 지나면 추가납입은 없다
        payment_add = 0

print("Total paid", round(total_paid, 1))
print("Paid month", mon_paid)
