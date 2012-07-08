# embed.ly
# http://apply.embed.ly/

# ---------------------
# PROBLEM 1
# ---------------------

def f(n):
	if n == 1:
		return 1
	else:
		return n * f(n-1);

def convert(n):	
	return sum([int(no) for no in str(n)])

def c1():
	num = 1
	while True:
		if convert(f(num)) == 8001:
			break
		num += 1
	print 'Solution to problem 1:', num


# ---------------------
# PROBLEM 2
# ---------------------

import re

def meanstdv(x):
	from math import sqrt
	n, mean, std = len(x), 0, 0
	for a in x:
		a = float(a)
		mean = mean + a
   	mean = mean / float(n)
	for a in x:
		a = float(a)
		std = std + (a - mean)**2
   	std = sqrt(std / float(n-1))
	return mean, std


def gett(i, stri):
	starts = [match.start() for match in re.finditer(re.escape('<div'), stri[:i])]
	stops = [match.start() for match in re.finditer(re.escape('</div'), stri[:i])]
	return len(starts)-len(stops)+1


def c2():
	import urllib

	f    = urllib.urlopen("http://apply.embed.ly/static/data/2.html")
	data = f.read()
	f.close()
		
	starts = [match.start() for match in re.finditer(re.escape('<p>'), data)]
	temp   = meanstdv([str(gett(i, data)) for i in starts])
	num    = [round(n*10)/10 for n in temp]

	print 'Solution to problem 2:', num[1]


# ---------------------
# PROBLEM 3
# ---------------------

def c3():
	i = 0
	sumo = 0
	v = [1/float(i) for i in range(1, 901, 1)]
	s = sum(v)

	for num in v:
		i    += 1
		sumo += num

		if sumo > s/2:
			break

	print 'Solution to problem 3:', i







if __name__ == '__main__':
	c1()
	c2()
	c3()