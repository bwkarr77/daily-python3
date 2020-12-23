# d = # of trailing days
# given a list of values
# compare list to 

def activityNotifications(expenditure, d):
    freq = {}
    num_alerts = 0
    n = len(expenditure)
    median = 0
    
    medVal = d/2
    
    def find(idx):
        total_count = 0
        for i in range(201):
            # print('forLoop: ', i, total_count) 
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i    
    
    for index in range(n-1):
        value = expenditure[index]
        
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
        
        if index >= (d-1):
            # determine the median
            if d%2 == 0:
                median = (find(medVal) + find(medVal + 1))/2
            else:
                median = find(medVal)
                
            if expenditure[index+1] >= median*2:
                num_alerts += 1
            
            freq[expenditure[(index-d)+1]] -= 1 #removes the oldest value from freq
    return(num_alerts)

print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))