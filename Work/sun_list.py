symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']

#1.20
for s in symlist:
    print('s =', s)

#1.21
print('AIG' in symlist)
print('AA' in symlist)
print('CAT' not in symlist)

#1.22
symlist.append('RHT')
symlist.insert(1, 'AA')
symlist.remove('MSFT')
symlist.insert(len(symlist), 'YHOO')
print(symlist.index('YHOO'))
print(symlist.count('YHOO'))
symlist.remove('YHOO')

#1.23
symlist.sort()
symlist.sort(reverse=True)

#1.24
a = ','.join(symlist)
b = ':'.join(symlist)
c = ''.join(symlist)
print(c)

#1.25
nums = [101, 102, 103]
items = ['spam', symlist, nums]
print(items)