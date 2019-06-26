import datetime
class man(object):

    def __init__(self,timein=0,timeout=0):
        self.timein = timein
        self.timeout = timeout

    def get_timein(self):
       return self.timein
    
    def get_timeout(self):
       return self.timeout

def timeparts(inter,kolvo):  
    l =inter/kolvo
    ls = [8.00]
    for i in range(kolvo):
        ls.append(ls[i]+l)
        ls[i] = int(ls[i])+ls[i]%1*0.6
        
    return ls

qwe = int(input('Vvedite chislo intervalov - '))
tps = timeparts(12,qwe)

f = open('4.txt', 'r')

t = f.read().split()

tm = []
for i in range(len(t)):
    tm.append(t[i].split(','))

men = [man() for i in range(len(tm))]
info = {}
for i in range(len(tm)):
    men[i].timein = float(tm[i][0])
    men[i].timeout = float(tm[i][1])

for i in range(1,len(tps)):
    info["{0:.2f}".format(tps[i-1]),"{0:.2f}".format(tps[i])]=0
    for j in range(len(tm)):
        if men[j].get_timein() < tps[i] and men[j].get_timeout() > tps[i-1] and men[j].get_timeout() != tps[i-1]:
        
            info[("{0:.2f}".format(tps[i-1]),"{0:.2f}".format(tps[i]))]+=1

#print(info)

maximum = max(info, key=info.get)  
print(maximum, info[maximum])
        
    
input('close?')




