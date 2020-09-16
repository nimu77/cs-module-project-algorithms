'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # Your code here
    # Your code here
    a = 0
    b = k
    output = []
    if k > len(nums):
        output.append(max(nums))
    else:
        for i in range(len(nums)-(k-1)):
            output.append(max(nums[a:b]))
            a += 1
            b += 1
            
 
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
