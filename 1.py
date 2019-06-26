
f = open('1.txt', 'r')
s = list(f.read().split(','))
s = [int(item) for item in s]
print(s)
f.close()

def proc(arr,N):
    s = sorted(arr)
    n = N/100
    ii = n*len(s)
    if ii%1 == 0:
        pr = s[int(ii-1)]
        
    else:
        pr = s[int(ceil(ii)-1)]
        
    return pr
    

a = proc(s,50)
print(a)
    
print('90 percentile ',proc(s,90))
print('median ',proc(s,50))
print('average ',(sum(s)) / float(len(s)))
print('max ',max(s))
print('min ',min(s))

input('close?')
