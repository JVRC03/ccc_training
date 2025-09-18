t = int(input())

def row(arr):
    for i in range(len(arr)):
        if 'spoon' in arr[i]:
            return True
    
    return False


def col(arr):
    for i in range(len(arr[-1])):
        s = ''
        for j in range(len(arr)):
            s += arr[j][i].lower()
        
        if 'spoon' in s:
            return True
    
    return False

while t:
    t -= 1
    
    s = input()
    ss = s.split(' ')
    a = int(ss[0])

    arr = []
    for i in range(a):
        k = input()
        k = k.lower()
        arr.append(k)
    
    if row(arr) or col(arr):
        print('There is a spoon!')
    else:
        print('There is indeed no spoon!')
    
        
    
