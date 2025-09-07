'''
def fib1(n):
    fibValue = 0
    result = []
    if n == 0:
        pass
    elif n == 1:
        result.append(0)
    for i in range(n):
        result.append(fibValue)
        fibValue += 

        
    # We will print our results here
    pass

def fib2(n):
    result = [] 
    return result
'''

def fib1(n):
    if n == 0:
        return
    fibValue = 0
    secondLastValue = 0
    LastValue = 1
    newValue = 0


    for i in range(n):
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        elif i >= 2:
            newValue = LastValue + secondLastValue
            print(newValue)
            secondLastValue = LastValue
            LastValue = newValue

    pass


def fib2(n):
    result = [] #We will store our result in this list

    fibValue = 0
    if n == 0:
        pass
    elif n == 1:
        result.append(0)
    elif n >= 2:
        for i in range(n):
            if i == 0:
                result.append(0)
            elif i == 1:
                 result.append(1)
            else:
                newValue = result[-1] + result[-2]
                result.append(newValue)
    
    return result





    



