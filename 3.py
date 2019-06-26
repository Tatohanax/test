
points=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for n in range(31,36,1):
    f = open('{id}.txt'.format(id=n), 'r')
    data = list(f.read().split(','))
    data = [float(item) for item in data]
    for i in range(len(data)):
        points[i] += data[i]
print('nomer promezhutka',points.index(max(points))) #interval vremeni

input('close?')
