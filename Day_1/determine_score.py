t = int(input())

while t:
    t -= 1
    s = input()
    arr = s.split(' ')
    n = int(arr[0])
    x = int(arr[-1])
    
    print((n//10) * x)
