class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        left = 0
        right = n - 1
        
        # Climb up from the left
        while left + 1 < n and arr[left] < arr[left + 1]:
            left += 1
            
        # Climb up from the right
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1
            
        # Valid only if both climbed at least once and met at the same peak
        return 0 < left == right < n - 1
