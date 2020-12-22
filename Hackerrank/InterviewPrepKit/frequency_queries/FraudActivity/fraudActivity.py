# d = # of trailing days
# given a list of values
# compare list to 

def activityNotifications(expenditure, d):
    trailing = expenditure[0:d]
    num_alerts = 0
    n = len(expenditure)
    valToCheck = 0
    
    for index in range(d, n):
        sortedList = trailing.copy()
        sortedList.sort()
        # print(trailing, sortedList)
        if d%2 > 0:
            valToCheck = sortedList[d//2]
        else:
            valToCheck = (sortedList[d//2] + sortedList[d//2 + 1])/2
        
        if valToCheck*2 <= expenditure[index]:
            num_alerts += 1
        trailing.pop(0)
        trailing.append(expenditure[index])
    return(num_alerts)

print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))