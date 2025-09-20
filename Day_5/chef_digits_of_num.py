t = int(input())

while t:
    t -= 1
    
    s = input()
    a, b = 0, 0
    
    for i in range(len(s)):
        if s[i] == '1':
            a += 1
        else:
            b += 1
    
    if a == 1 or b == 1:
        print('Yes')
    else:
        print('No')
