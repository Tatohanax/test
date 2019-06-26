

f = open('2.txt', 'r')

s = f.read().split()

s1 = s[0].split(',')
s1 = [float(item) for item in s1]
s2 = s[1].split(',')
s2 = [float(item) for item in s2]
s3 = s[2].split(',')
s3 = [float(item) for item in s3]
s4 = s[3].split(',')
s4 = [float(item) for item in s4]

f.close()
def yrpr(t1,t2):
    try:
        K = 1
        k = (t1[1] - t2[1]) / (t1[0] - t2[0])
        b = t2[1] - k*t2[0]
        
    except ZeroDivisionError:
        b = t1[1]
        k = -1
        K = 0
    return (k,b,K)

def doit(x,y,s1,s2,s3,s4):
    p1 = yrpr(s1,s2)
    p2 = yrpr(s2,s3)
    p3 = yrpr(s3,s4)
    p4 = yrpr(s4,s1)
   
 
    if  p1[2]*y == p1[0]*x+p1[1] or p3[2]*y == p3[0]*x+p3[1] or p2[0]*x == y*p2[2]-p2[1] or p4[0]*x == y*p4[2]-p4[1] and p1[2]*y <= p1[0]*x+p1[1] and p3[2]*y >= p3[0]*x+p3[1] and p2[0]*x >= y*p2[2]-p2[1] and p4[0]*x <= y*p4[2]-p4[1]  :
        
                text = (x,y,'Na grani')
  
            
                  
    elif p1[2]*y < p1[0]*x+p1[1] and p3[2]*y > p3[0]*x+p3[1] and p2[0]*x > y*p2[2]-p2[1] and p4[0]*x < y*p4[2]-p4[1]:
        text = (x,y,' Vnutri')
    else:
        text = (x,y,'Snarugi')
    
    return text






while True:
    try:
        xx = float(input('VVedite X - '))
        yy = float(input('VVedite Y - '))
        if [xx,yy] == s1 or [xx,yy] == s2 or [xx,yy] == s3 or [xx,yy] == s4:
            print(xx,yy,'Vershina')
           
        else:
                       
            print(doit(xx,yy,s1,s2,s3,s4))
    except:
        print('''''')
