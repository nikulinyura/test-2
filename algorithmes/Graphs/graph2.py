
#test
g = {}
g['cab'] = ['car', 'cat']
g['car'] = ['cat', 'bar']
g['cat'] = ['mat', 'bat']
g['bar'] = ['bat']
g['mat'] = ['bat']

'''    
from collections import deque
sq = deque()
sq += g['cab']
itm = sq.popleft()

while sq:
    if fin(itm):
        print(itm + 'IT IS')
    else:
        sq +=g[itm]


def ser(s, f):
    pass


def fin(i):
    if i == 'bat':
        return True
'''
print('-' * 20)