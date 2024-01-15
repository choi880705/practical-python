# mortgage.py

principal = 500000.0    # 원금 = 500,000
principal_new = 500000.0
rate = 0.05             # 연이율 = 0.05%
payment = 2684.11       # 매달 납부할 금액 = 2684.11
total_paid = 0.0        # 납부금액 초기화
mon = 0                 # 납부횟수
principal_this_month = 0.0 # 이번달 상환원금 초기화
interest_this_month = 0.0  # 이번달 이자 초기화

while principal > 0:    # 원금이 남아 있는 동안
    principal_new = principal * (1 +rate/12) - payment  # 남은 원금 = 원금 *(1 + 월이자) - 매달 납부금
    if principal_new < 0:
        payment = principal * (1 +rate/12)
        principal_new = 0

    total_paid = total_paid + payment               # 납부 총액 = 이전 납부 총액 + 매달 납부금
    mon = mon + 1
    principal_this_month = principal - principal_new
    interest_this_month = payment - principal_this_month
    print(f'{mon} 번째달 상환원금: {round(principal_this_month, 2)} 이자: {round(interest_this_month, 2)} '
          f'현재까지 납부 금액: {round(total_paid, 2)} 남은 원금: {round(principal_new, 2)}')
    principal = principal_new

print('Total paid', round(total_paid, 2))
print(f'납부 횟수 : {mon}개월, {mon / 12}년')
