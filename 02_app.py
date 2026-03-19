# ==========================================================================================
# Question 1: Sum of List
# Problem: Write a function to find the sum of all numbers in a list.
# Example:
    # Input: [1,2,3,4]
    # Output: 10
# ==========================================================================================
def sum_list(arr):
    sum = 0
    
    for num in arr:
        sum += num
        
    return sum
    
print(f"Sum of list : {sum_list([1,2,3,4])}")

# ==========================================================================================
# Question 2: Find Even Numbers
# Problem: Return only even numbers from a list.
# Example:
    # Input: [1,2,3,4,5,6]
    # Output: [2,4,6]
# ==========================================================================================
def get_even(arr):
    evens = []
    
    for num in arr:
        if(num % 2 == 0):
            evens.append(num)
    
    return evens

print(f"Even numbers in given array : {get_even([1,2,3,4,5,6])}")

# ==========================================================================================
# Question 3: Count Words in Sentence
# Problem: Count how many words are in a sentence.
# Example:
    # Input: "I love Python programming"
    # Output: 4
# ==========================================================================================
def count_words(sentence):
    words = sentence.split(" ")
    return len(words)

print(f"Words count : {count_words("I love Python programming")}")

# ==========================================================================================
# Question 4: Find Largest Number
# Problem: Find the largest number in a list.
# ==========================================================================================
def largest_num(arr):
    # return max(arr) # one-line answer to find max out of array
    
    # Alternative:
    largest = arr[0]
    
    for num in arr:
        if(num > largest):
            largest = num
    
    return largest

print(f"Largest number : {largest_num([22,33,12,4,52,34,6])}")

# ==========================================================================================
# Question 5: Count Occurrences (Important)
# Problem: Count how many times each element appears in a list.
# Example:
    # Input: [1,2,2,3,3,3]
    # Output: {1:1, 2:2, 3:3}
# ==========================================================================================
def count_elements(numbers):
    count_dict = {}
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    return count_dict

print(f"Count occurrences : {count_elements([1,2,2,3,3,3])}")

# ==========================================================================================
# Question 6: Remove Duplicates
# Problem: Multiple same elements in a list
# Example:
    # Input: [1,2,2,3,4,4,5]
    # Output: [1,2,3,4,5]
# ==========================================================================================
def remove_duplicates(numbers):
    # return list(set(numbers))
    
    # Alternative:
    unique = []
    
    for num in numbers:
        if num not in unique:
            unique.append(num)
            
    return unique

print(f"List are removing duplicates : {remove_duplicates([1,2,2,3,4,4,5])}")