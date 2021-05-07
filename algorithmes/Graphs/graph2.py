g = {}
g['cab'] = ['car', 'cat']
g['car'] = ['cat', 'bar']
g['cat'] = ['mat', 'bat']
g['bar'] = ['bat']
g['mat'] = ['bat']

def sp(dic, s, f):
    from collections import deque
    sq = deque()
    sq += dic[s]
    p=1

    while sq:
        i = sq.popleft()
        if i == f:
            return s, 'to', f, 'is', p, 'step'
            
        else:
            if not sq:
                p+=1
                try: sq +=dic[i]
                except KeyboardInterrupt:
                    print('no') 
                    break


#test
print(sp(g, 'mat', 'bat'))