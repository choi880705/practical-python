# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv','rt')
shares = 0
price = 0
Total = 0
headers = next(f)
for line in f:
    l = line.split(',')
    shares = int(l[1])
    price = float(l[2])
    Total = shares * price + Total

result = f'Total cost ${Total}'

print(result)

f.close()

