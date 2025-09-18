t = int(input())

while t:
    t-=1
    n = int(input())
    k = (n * n)
    e, o = [], []
    
    for i in range(1, k+1):
        if i%2 == 0:
            e.append(i)
        else:
            o.append(i)
    
    temp = []
    c = 0
    
    while len(o):
        d = []
        if c%2 == 0:
            for i in range(n):
                if i%2 == 0:
                    d.append(o.pop())
                else:
                    d.append(e.pop())
            temp.append(d)
        else:
            for i in range(n):
                if i%2 == 1:
                    d.append(o.pop())
                else:
                    d.append(e.pop())
            temp.append(d) 
        c += 1
    
    for i in range(len(temp)):
        for j in range(len(temp)):
            print(temp[i][j], end = ' ')
        print()

  
            
        
    
