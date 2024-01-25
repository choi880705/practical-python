# mortgage.py
#
# Exercise 1.7

# 변수선언 및 초기화
principal = 500000.0  # 원금
rate = 0.05  # 년이자
payment = 2684.11  # 월납입금
total_paid = 0.0  # 총상환액


while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print("Total paid", round(total_paid, 1))
