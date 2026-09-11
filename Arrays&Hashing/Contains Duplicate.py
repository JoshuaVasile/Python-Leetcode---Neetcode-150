"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
import random

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

def main():
    print("Select Input Mode:")
    print("1: Generate a random array")
    print("2: Enter own array")
    
    mode = input("Mode (1/2): ").strip()
    
    if mode == '1':
        size = random.randint(4, 10)
        nums = [random.randint(1, 10) for _ in range(size)]
        print(f"\nInput: nums = {nums}")
        
    elif mode == '2':
        raw_input = input("\nEnter integers separated by commas (e.g., 1, 2, 3, 4): ")
        try:
            nums = [int(x.strip()) for x in raw_input.split(',')]
            print(f"\nInput: nums = {nums}")
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")
            return
            
    else:
        print("Invalid selection.")
        return

    result = Solution().containsDuplicate(nums)
    print(f"Output: {str(result).lower()}")

if __name__ == "__main__":
    main()