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




#d = sim_distance (critics,'Lisa Rose','Gene Seymour')

#print d




# 2016.1.21