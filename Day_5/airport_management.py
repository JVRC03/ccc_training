t = int(input())

while t:
    t -= 1
    dic = {}
    jvrc = 0
    
    n = int(input())
    
    s = input()
    a = s.split(' ')
    p = input()
    b = p.split(' ')

    for i in range(len(a)):
        if int(a[i]) not in dic:
            dic[int(a[i])] = 1
        else:
            dic[int(a[i])] += 1
        jvrc = max(jvrc, dic[int(a[i])])

    for i in range(len(b)):
        if int(b[i]) not in dic:
            dic[int(b[i])] = 1
        else:
            dic[int(b[i])] += 1  
        
        jvrc = max(jvrc, dic[int(b[i])]  )
            
        
    print(jvrc)

# Since we have to find out the buisiest time second where the airport is so busy, 
# we can simply count the number of times in which at a particular second the airport is busy. 
# I typically used a dictionary to get the occurances of each sec, and finally printed the 
# highest count. 

