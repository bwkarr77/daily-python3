def countTriplets(arr, r):
    # create a cache for storing answers
    # assign each value in arr to the cache
    # iterate through the array
    # determine if the value is key*r or key*r*r

    count = 0
    dict = {}
    dictPairs = {}

    for value in reversed(arr):
        if value*r in dictPairs:
            count += dictPairs[value*r]
        if value*r in dict:
            dictPairs[value] = dictPairs.get(value, 0) + dict[value*r]
        
        ## dict.get(value, 0) => returns the keyname, based on the value you entered.
        dict[value] = dict.get(value, 0) + 1 

    return count

arr = [1, 5, 5, 25, 125]
r = 5

print(countTriplets(arr, r))