# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_payment = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 0
message = ''

while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    principal = principal * (1+rate/12) - total_payment
    if principal < 0:
        principal = 0
    total_paid = total_paid + total_payment

    #print(month, round(total_paid, 2), round(principal, 2))
    message = f'월수: {month}, 현재까지 납부액: {round(total_paid, 2)}, 남은 원금: {round(principal, 2)}'
    print(message)

print('Total paid', round(total_paid, 2))
print('Months', month)
print('principal', principal)

#월수, 현재까지 납부액, 남은 원금
