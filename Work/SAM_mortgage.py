# mortgage.py
#
# Exercise 1.7
principal=500000.0
rate=0.05
payment=2684.11
month=0
total_paid=0.0

extra_payment_start_month=61
extra_payment_end_month=108
extra_payment=1000

while principal>0:
    if extra_payment_start_month<=month<=extra_payment_end_month:
        principal=principal*(1+rate/12)-(payment+extra_payment)
        total_paid=total_paid+(payment+extra_payment)
    elif principal<payment:
        total_paid=total_paid+principal
        principal=0
    else:
        principal=principal*(1+rate/12)-payment
        total_paid=total_paid+payment
    month=month+1
    print(month,round(total_paid,2),round(principal,2))


print(f'Total paid amount is {round(total_paid,1)}')
print(f'Total months to finish the payment are {month}')