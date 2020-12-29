def mergeSort(arr, count):
    print('arr: ', arr)
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        Llen = len(L)
        Rlen = len(R)
        print('arr.mid: ', arr, L, R)
        while i < Llen and j < Llen:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                count += 1
            k += 1
 
        # Checking if any element was left
        while i < Llen:
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < Llen:
            arr[k] = R[j]
            j += 1
            k += 1
        
        print('arr end: ', arr)

        

startArr = [12, 11, 13, 5, 6, 7]
arr = startArr.copy()
mergeSort(arr, 0)
print('start: ', startArr)
print('sorted:', arr)