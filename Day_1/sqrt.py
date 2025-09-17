def f(a):
  if a < 2:
      return 0
  
  if a == 2 or a == 3:
      return 1
  
  if a%2 == 0 or a%3 == 0:
      return 0
  
  for i in range(5, int(math.sqrt(a))+1, 6):
      if a%i == 0 or a%(i+2) == 0:
          return 0
  
  return 1

n = int(input())
print(f(n))
