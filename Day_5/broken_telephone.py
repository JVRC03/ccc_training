'''
        https://www.codechef.com/problems/BROKPHON
'''

t = int(input())

while t:
    t -= 1
    n = int(input())
    s = input()
    arr = s.split(' ')
    jvrc=0
    s = set()
    
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            if i not in s:
                jvrc += 2
            else:
                jvrc += 1
            s.add(i)
            s.add(i+1)
    
    print(jvrc)
        
