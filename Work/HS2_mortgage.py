'''
[p.28/연습 문제 1.7 데이브의 주택 담보 대출 해석]
데이브는 500,000 달러의 30 년 고정 이율 주택 담보 대출 (mortgage) 을 받기로 결정했다.
이율은 5% 이고 매달 납부할 금액은 2684.11 달러다.
'''
# mortgage.py
principal = 500000.0 #원금 500,000달러
rate = 0.05 #연이율
payment = 2684.11 #납입금
total_paid = 0.0 #지불할 총액

while principal > 0: #원금이 0보다 클 동안 반복 실행
    principal = principal * (1+rate/12) - payment #원금은 (원금*월이율)에서 고정 납입금을 차감
    total_paid = total_paid + payment #지불할 총액은 총액+고정 납입금
print('Total paid', total_paid) #Tatal paid와 총 납입액 출력


'''
[p.29/연습 문제 1.8 데이브의 주택 담보 대출(추가 납입) 풀이]
데이브가 처음 12 개월 동안 매달 1000 달러를 추가로 납입한다면 어떻게 될까?
이 추가 납입금 계산을 포함하도록 프로그램을 수정해 총 납입금액과 소요 월수를 프린트해보자.
프로그램을 실행했을 때 총 납입금이 929,965.62, 소요 월수는 342 로 나와야 한다.
'''
# mortgage.py
principal = 500000.0 #원금 500,000달러
rate = 0.05 #연이율
payment = 2684.11 #납입금
total_paid = 0.0 #지불할 총액
month = 0 #소요 월수

while principal > 0: #원금이 0보다 클 동안 반복 실행
    month=month+1 #소요 월수는 1개월씩 증가
    if month <= 12: #소요 월수가 12개월보다 작거나 같을 때
        principal = principal * (1+rate/12) - (payment+1000) #원금은 (원금*월이율)에서 (고정 납입금+1000달러)를 차감
        total_paid=total_paid+(payment+1000) #지불할 총액은 총액+(고정 납입금+1000)
    else: #소요 월수가 12개월보다 작거나 같지 않을 때
        principal = principal * (1+rate/12) - payment #원금은 (원금*월이율)에서 고정 납입금을 차감
        total_paid = total_paid + payment #지불할 총액은 총액+고정 납입금
print('Total paid', round(total_paid,2)) #Tatal paid와 총 납입액 출력
print('Month', month)