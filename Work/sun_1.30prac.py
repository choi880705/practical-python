def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')

    total_cost = 0

    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])

    f.close()



cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
