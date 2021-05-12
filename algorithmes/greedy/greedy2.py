# GREEDY ALGORITHM
# O(n**2)

sks  = set(['rain', 'defence', 'attack', 'stress', 'lead'])

pls = {}
pls['1'] = set(['defence', 'stress'])
pls['2'] = set(['rain', 'attack'])
pls['3'] = set(['stress', 'rain', ])
pls['4'] = set(['attack', 'lead'])
pls['5'] = set(['defence', 'stress'])

 

def dr_team(skills, players):
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
    return dream_team

print(dr_team(sks, pls))
            
