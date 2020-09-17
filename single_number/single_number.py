'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # loop through the loop
    # if the value matches move to another index to check
    bucket = [0 for i in range(len(arr))]

    for value in arr:
        bucket[value] += 1
        
    for i, v in enumerate(bucket):
        if v == 1:
            return i
    
'''
    s = set()
    for num in arr:    # O(n)
        if num in s:     #O(1)
            s.remove(num)   #O(1)
        else:
            s.add(num)      #O(1)

    return list(s)[0]         #O(1)

'''

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")