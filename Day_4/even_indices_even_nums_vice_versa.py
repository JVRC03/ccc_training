n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

def call(arr, temp, idx, k):
    temp = arr[idx]
    for i in range(idx, k+1, -1):
        arr[i] = arr[i-1]
    
    return arr
        
for i in range(n):
    if (i%2 == 0 and arr[i]%2 == 0) or (i%2 == 1 and arr[i]%2 == 1):
        continue
    
    for j in range(i+1, n):
        if i%2 == 0:
            if arr[j]%2 == 0:
                temp = arr[i]
                arr[i] = arr[j]
                arr = call(arr, temp, j, i)
                arr[i+1] = temp
                break
        else:
            if arr[j]%2 == 1:
                temp = arr[i]
                arr[i] = arr[j]
                arr = call(arr, temp, j, i)
                arr[i+1] = temp
                break

print(arr)


