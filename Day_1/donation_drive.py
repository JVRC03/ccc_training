t = int(input())

while t:
    t -= 1
    s = input()
    arr = s.split(' ')
    a = int(arr[0])
    b = int(arr[-1])
    print(a-b)
