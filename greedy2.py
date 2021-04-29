# add comments
# make as function

skills  = set(['rain', 'defence', 'attack', 'stress', 'lead'])

players = {}
players['1'] = set(['defence', 'stress'])
players['2'] = set(['rain', 'attack'])
players['3'] = set(['stress', 'rain', ])
players['4'] = set(['attack', 'lead'])
players['5'] = set(['defence', 'stress'])

dream_team = set() 


while skills:
    best_player = None
    skills_cov = set()
    for P, SK in players.items():
        skil = skills & SK
        if len(skil) > len(skills_cov):
            best_player = P
            skills_cov = skil
    skills -= skills_cov
    dream_team.add(best_player)

print(dream_team)
            
