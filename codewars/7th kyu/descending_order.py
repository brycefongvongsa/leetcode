'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Best answer:
return int("".join(sorted(str(num), reverse=True)))
'''


def descending_order(num):
    # return num if it's 1 number
    if len(str(num)) == 1:
        return num
    
    # sort into new list to sort and reverse
    numList = [int(digit) for digit in str(num)]
    numList.sort()
    numList.reverse()
    # convert it back into a num
    result = int("".join(map(str, numList)))
    return result
