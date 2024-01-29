symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

#print(symbols[0])
#print(symbols[1])
#print(symbols[2])
#print(symbols[-1])
#print(symbols[-2])

#1.14
symbols = symbols + ',GOOG'
symbols = 'HPQ,' + symbols
print(symbols)

#1.15
print('IBM' in symbols)
print('AA' in symbols)
print('CAT' in symbols)

#1.16
print(symbols.lower())
print(symbols)

lowersyms = symbols.lower()
print(lowersyms)

print(symbols.find('MSFT'))
print(symbols[13:17])

symbols = symbols.replace('SCO','DOA')
print(symbols)

name = ' IBM \n'
name = name.strip()
print(name)