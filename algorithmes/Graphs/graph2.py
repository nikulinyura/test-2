# how many steps to s

# add comments

import pandas as pd
import matplotlib.pyplot as plt

g = {}
g['cab'] = ['car', 'cat']
g['car'] = ['cat', 'bar']
g['cat'] = ['mat']
g['bar'] = ['bat']
g['mat'] = ['bat']
from collections import deque
def steps(dic, s):
    sq = deque()
    st=deque()
    sq+=dic[s]
    sed = []
    tab={}
    n=1
    while sq:
        i = sq.popleft()
        if i not in sed:
            sed.append(i)
            tab[i]=n
            try: 
                st+=dic[i]
            except KeyError:
                pass
            if not sq:
                n+=1
                sq += st
                st = deque()
            
    return tab   

a =  steps(g, 'cab')
A =  pd.Series(steps(g, 'cab'))
print(pd.Series(steps(g, 'cab')))
A.plot()
plt.show()
