def makeAnagram(a, b):
    returnCount = len(a) + len(b)
    
    def createDict(string):
        returnDictionary = {}
        for each in string:
            # print(each, returnDictionary)
            if each in returnDictionary:
                returnDictionary[each] += 1
            else:
                returnDictionary[each] = 1
        return returnDictionary
    
    if len(a) <= len(b):
        shorter = a
        longer = createDict(b)
    else:
        shorter = b
        longer = createDict(a)
    
    print(shorter, longer)
    for each in shorter:
        # print(each)
        if (each in longer) and (longer[each]>0):
            longer[each] -= 1
            returnCount -= 2
            
    return(returnCount)


a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
nums = makeAnagram(a, b)
print(nums)