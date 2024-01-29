f = open('C:/Users/user/OneDrive/문서/practical-pyhon/Work/Data/portfolio.csv', 'rt')
headers = next(f).split(',')

total_cost = 0

for line in f:
     row = line.split(',')
     total_cost = total_cost + int(row[1]) * float(row[2])

f.close()
print('Total cost', total_cost)

#1.28
import gzip
with gzip.open('C:/Users/user/OneDrive/문서/practical-pyhon/Work/Data/portfolio.csv.gz', 'rt') as f:
     for line in f:
          print(line, end='')