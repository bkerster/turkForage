#updated for use in mass production

import random

class Square:	
	def __init__(self, x1 = 0, y1 = 0, x2 = 1280, y2 = 1024, stars = 100, direction = 1):
		self.direction = direction
		self.x1 = float(x1)
		self.y1 = float(y1)
		self.x2 = float(x2)
		self.y2 = float(y2)
		self.stars = stars

def scatter(sqr, prob):
	if sqr.stars < 1:
		return
		
	if (sqr.x2 - sqr.x1 < 1) and (sqr.y2 - sqr.y1 < 1):
		x = int(sqr.x1)
		y = int(sqr.y1)
		for i in range(0, sqr.stars):
			points.append( (x,y) )
		return
		
	if sqr.stars == 1:
		try:
			x = random.randrange(int(sqr.x1), int(sqr.x2))
		except ValueError:
			x = int(sqr.x1)
		try: 
			y = random.randrange(int(sqr.y1), int(sqr.y2))
		except ValueError:
			y = int(sqr.y1)
		points.append( (x, y) )
		return

	if sqr.direction:
		mid = (sqr.x1 + sqr.x2) / 2
		stars1 = 0
		for i in range(0, sqr.stars):
			if random.random() < prob:
				stars1 += 1
		stars2 = sqr.stars - stars1
		#50% chance that the "larger" set of stars ends up on one side or another
		if random.random() < 0.5:
			temp = stars2
			stars2 = stars1
			stars1 = temp
			
		s1 = Square(sqr.x1, sqr.y1, mid, sqr.y2, stars1, 0 ) #square goes to the first half of the width
		s2 = Square(mid, sqr.y1, sqr.x2, sqr.y2, stars2, 0 ) #square goes to the second half of the width to the end of the first square
		
	else:
		mid = (sqr.y1 + sqr.y2) / 2
		stars1 = 0
		for i in range(0, sqr.stars):
			if random.random() < prob:
				stars1 += 1
		stars2 = sqr.stars - stars1
		#50% chance that the "larger" set of stars ends up on one side or another
		if random.random() < 0.5:
			temp = stars2
			stars2 = stars1
			stars1 = temp
		s1 = Square(sqr.x1, sqr.y1, sqr.x2, mid, stars1, 1)
		s2 = Square(sqr.x1, mid, sqr.x2, sqr.y2, stars2, 1)
		
	scatter(s1, prob)
	scatter(s2, prob)		
	
def randPoints(sqr, file):
	for i in range(0, num_stars):
		x = random.randrange(int(sqr.x1), int(sqr.x2))
		y = random.randrange(int(sqr.y1), int(sqr.y2))
		file.write('{0} {1}\n'.format(x, y) )
		
def countDupes(dupedList):
   uniqueSet = set(item for item in dupedList)
   return [(item, dupedList.count(item)) for item in uniqueSet]



#filename = '2000stars3.txt'
conditions = [ .05, .15, .25, .35, .5 ]
stars = [ 25, 50, 100, 150 ]
for prob in conditions:
	for num_stars in stars:
		for i in range(1000):
			print i
			points = []
			#prob = 0.5
			#num_stars = 150
			if len(str(prob)) == 3:
				#filename = str(num_stars) + 'stars' + str(int(prob * 10)) + '-7.txt'
				filename = '{0}stars{1}-{2}.txt'.format(num_stars, (int(prob*10)), i)
			elif len(str(prob)) == 4:
				if prob == .05:
					filename = '{0}stars{1}-{2}.txt'.format(num_stars, '05', i)
				#filename = str(num_stars) + 'stars' + str(int(prob * 10)) + '-7.txt'
				else:
					filename = '{0}stars{1}-{2}.txt'.format(num_stars, (int(prob*100)), i)
			else:
				print 'Error! Filename could not parse your prob!'
				break
			f = open(filename, 'w')
			   
			sq = Square(stars=num_stars)
			scatter(sq, prob)
			pnts = countDupes(points)
			for point in pnts:
				f.write('{0} {1} {2}\n'.format(point[0][0], point[0][1], point[1] ))
			f.close()		