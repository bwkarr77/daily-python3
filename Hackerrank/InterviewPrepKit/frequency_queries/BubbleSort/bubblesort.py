def countSwaps(a):
    n = len(a)
    count = 0
    response = []
    for i in range(n):
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                count += 1
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    # print(a)
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(a[0])+" ")
    print("Last Element: "+str(a[-1])+" ")

testCase = [4,2,3,1,44]
countSwaps(testCase)