f = open('res.txt', 'r')
data = f.read()
f.close()
vals = map(lambda x: int(x), data.split('\n'))




d = {}

for v in vals:
    if v not in d.keys():
        d[v] = 1
    else:
        d[v] += 1

print d