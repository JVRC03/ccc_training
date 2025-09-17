t = int(input())

while t:
    t -= 1
    n = int(input())
    s = input()
    k = s.split(' ')
    mini = float('inf')
    
    c = 0
    for i in range(n):
        c += int(k[i])
        mini = min(mini, int(k[i]))
    
    print(c-mini)
