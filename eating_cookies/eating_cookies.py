'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    # if n < 2:
    #     return 1
    # elif n ==2:
    #     return 2
    # else:
    #     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    if n < 0:
        return 0

    elif n == 0:
        return 1

    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
