# =====================================================================
# Question 1: Sum of List
# Problem: Write a function to find the sum of all numbers in a list.
# Example:
    # Input: [1,2,3,4]
    # Output: 10
# =====================================================================
def sumOfList(arr):
    sum = 0
    
    for num in arr:
        sum += num
        
    return sum
    
print(f"Sum of all numbers in a list is {sumOfList([1,2,3,4])}")

# =====================================================================
