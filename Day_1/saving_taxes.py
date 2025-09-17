n = int(input())

for i in range(n):
    s = input()
    arr = s.split(' ')
    x = int(arr[0])
    y = int(arr[-1])
    print(x-y)
