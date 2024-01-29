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
#while principal > 0:
#    if month <12:
#        payment = 3684.11
#   else:
#        payment = 2684.11
#    principal = principal * (1+rate/12) - payment
#    total_paid = total_paid + payment
#    month = month + 1
#print('Total paid', total_paid)
#print('Total Month', month)

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

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
print('principal', principal)