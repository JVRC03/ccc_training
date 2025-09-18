n = int(input())

jvrc = [-1, -1]

a, b = 0, 0

for i in range(n):
    ss = input()
    s = ss.split(' ')
    a += int(s[0])
    b += int(s[-1])
    
    diff = abs(a-b)
    
    if a > b:
        if diff > jvrc[-1]:
            jvrc[-1] = diff
            jvrc[0] = 1
    
    else:
        if diff > jvrc[-1]:
            jvrc[-1] = diff
            jvrc[0] = 2
    

print(jvrc[0], jvrc[1])
        
'''
            In this game, after every round we keep adding each player’s scores to get their cumulative total.
            
            The player who is ahead after that round becomes the leader.
            
            The difference between their scores is called the lead.
            
            At the end of all rounds, we look back at the biggest lead that ever happened.
            👉 The player who had that biggest lead is declared the winner.

'''
