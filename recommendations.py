critics = {'Lisa Rose':{'Lady in the Water':2.5,'Snake on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':3.5,'You,Me and Dupree':2.5,'The Night Listener':3.0},
'Gene Seymour':{'Lady in the Water':3.0,'Snake on a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'You,Me and Dupree':3.5,'The Night Listener':3.0},
'Michael Phillips':{'Lady in the Water':2.5,'Snake on a Plane':3.0,'Superman Returns':3.5,'The Night Listener':4.0},
'Claudia Puig':{'Snake on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':4.0,'You,Me and Dupree':2.5,'The Night Listener':4.5},
'Mick LaSalle':{'Lady in the Water':3.0,'Snake on a Plane':4.0,'Just My Luck':2.0,'Superman Returns':3.0,'You,Me and Dupree':2.0,'The Night Listener':3.0},
'Jack Matthews':{'Lady in the Water':3.0,'Snake on a Plane':4.0,'Just My Luck':3.0,'Superman Returns':5.0,'You,Me and Dupree':3.5,'The Night Listener':3.0},
'Toby':{'Snake on a Plane':4.5,'Superman Returns':4.0,'You,Me and Dupree':1.0},
		}
from math import sqrt

def sim_distance(prefs,person1,person2):

	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	if len(si) == 0 : 
		return 0

	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])

	return 1/(1+sqrt(sum_of_squares))

def topMatches(prefs,person,n=5,similarity=sim_distance):
	scores = [(similarity(prefs,person,other),other) for other in prefs if other !=person]
	scores.sort()
	scores.reverse()
	return scores[0:n]

def getRecommendations(prefs,person,similarity = sim_distance):
	totals = {}
	simSums = {}
	for other in prefs:
		if other == person:
			continue
		sim = similarity(prefs,person,other)
		if sim <= 0 :
			continue
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item,0)
				totals[item] += prefs[other][item] * sim
				simSums.setdefault(item,0)	
				simSums[item] += sim

		rankings = [(total/simSums[item],item) for item,total in totals.items()]
		rankings.sort()
		rankings.reverse()
		return rankings

fgsdfsdfsdfsdfsdf
