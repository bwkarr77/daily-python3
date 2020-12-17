def freqQuery(queries):
    # queries = [(operation, value)]
    # operation = 1) add value into array 2) Delete value from array
    #   ... 3) find the number of  
    
    response = []
    storage = {}
    
    for query in queries:
        # print(query)
        command = query[0]
        value = query[1]
        
        if command == 1:
            # print('1')
            if value not in storage:
                storage[value] = 1
            else:
                storage[value] += 1
        elif command == 2:
            # print('2')
            if (value in storage) and (storage[value] > 0):
                storage[value] = 1
        elif command == 3:
            # print('3')
            keys = list(storage.keys())
            val_list = list(storage.values())
            try:
                position = val_list.index(value)
                response.append(1)
            except:
                response.append(0)
    return response

    testCase = [
        
    ]