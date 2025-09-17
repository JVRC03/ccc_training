
t = int(input())

while t:
    t -= 1
    n = int(input())
    k = 1
    for i in range(1, n+1):
        k *= i 
    print(k)
