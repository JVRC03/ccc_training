t = int(input())

while t:
    t -= 1
    a = input()
    s = a.split(' ')
    n = int(s[0])
    k = int(s[-1])
    arr = input()
    p = arr.split(' ')
    c = 0
    
    for i in range(len(p)):
        if int(p[i]) > k:
            c += 1 
    
    print(c)
