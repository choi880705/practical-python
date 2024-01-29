text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'

import re
result1 = re.findall(r'\d+/\d+/\d+', text)

print(result1)

