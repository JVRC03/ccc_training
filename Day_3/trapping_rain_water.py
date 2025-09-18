class Solution:
    def trap(self, arr: List[int]) -> int:
        mx = arr.index(max(arr))

        jvrc = 0
        lx, rx = arr[0], arr[-1]

        for i in range(mx):
            lx = max(lx, arr[i])
            jvrc += (lx-arr[i])
        
        for i in range(len(arr)-1, mx, -1):
            rx = max(rx, arr[i])
            jvrc += (rx-arr[i])     

        return jvrc   

''' 
    
    Find the tallest wall → water can’t flow over it.

    From the left to tallest wall → keep track of the highest wall seen so far.
    
    Water trapped at each point = (highest wall so far – current wall).
    
    From the right to tallest wall → same logic with right-side max.
    
    Add them up → total trapped water.
    
    Your code does exactly this in O(n) time and O(1) space.

'''
