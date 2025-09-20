t = int(input())

while t:
    t -= 1
    dic = {}
    n = int(input())
    v = ['c', 'o', 'd', 'e', 'h', 'f']
    c = [2, 1, 1, 2, 1, 1]
    for i in range(n):
        s = input()
        for j in range(len(s)):
            if s[j] in v:
                if s[j] not in dic:
                    dic[s[j]] = 1
                else:
                    dic[s[j]] += 1
    
    jvrc = 0
    if len(dic) != 6:
        print(0)
        continue
    
    while True:
        stop = 0
        for i in range(len(c)):
            if dic[v[i]] >= c[i]:
                dic[v[i]] -= c[i]
                continue
            stop = 1
            break
        
        if stop:
            break
        jvrc += 1
    
    print(jvrc)
        
    
    
