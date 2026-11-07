class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Traverse the array backwards (from the last digit to the first)
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just add 1 and return immediately
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0, and the loop continues to carry the 1
            digits[i] = 0
            
        # If the loop finishes, it means ALL digits were 9 (e.g., [9, 9, 9])
        # We need to add a 1 at the very front of the array
        return [1] + digits