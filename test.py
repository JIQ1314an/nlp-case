from collections import Counter

import numpy as np
from IPython.core.display import display

count = [Counter(['this', 'is', 'the', 'first', 'document']),
        Counter(['this', 'is' 'the' 'second' 'second' 'document']),
        Counter(['and', 'the', 'third', 'one']),
        Counter(['is', 'this', 'the', 'first', 'document']),
         ]
print(count)
# print(count['th'])
# print( 'th' in count)
# print( 'this' in count)
# print(sum(count.values()))
# a = ['', 't', '']
# print(a.count(''))
# a.remove('')
# a.remove('')
# print(a)

# print(sum([1 for c in count if 'first' in c]))
#
# import  pandas as pd
# a = {'this': [1 , 2, 3],'is': [11 , 21, 32]}
# if a.get('this'):
#     print(a.get('this'))
# print(pd.DataFrame(a))
# print(pd.DataFrame(a).values)
#
# a = pd.Series(['1', 2, '1', 2, 3])
# print(a.unique())
# a= [1, 2, 3]
# b= []
# print(b)
# b.extend(a)
# b.extend(a)
# print(b)
# print(np.array([1, 2, 3]) * np.array([1, 2, 3]))
# print(np.sqrt(sum(np.array([1, 2, 3])**2)))
# print(np.sqrt(sum(np.array([1, 2, 2])**2)))

file = './corpus/doc_one.txt'
corpus = []
with open(file) as f:
    for line in f.readlines():
        corpus.append(line.rstrip('\n'))
    print(corpus)

# with open(file) as f:
#     line = f.readline()
#     while line:
#         print(line)
#     line = f.readline()