# Lab08
# Brett Roach
# 6907380

def recursiveDigitSum(n):
    '''
    Computes the sum of digits of a positive integer n
    - Your solution must use recursion in order to receive credit.
    '''
    if (n >= 0) and (n <= 9):
        return n
    elif (n >= 10):
        return (n%10) + recursiveDigitSum(n//10)
    return "stub"

def recursiveSubstring(s, sub):
    '''
    The parameters sub and s are strings. This function computes if a
    the string sub exists in s.
    - Your solution must use recursion in order to receive credit.
    '''
    if (len(s) >= len(sub)):
        if (s[0:len(sub)] == sub):
            return True
        else:
            return recursiveSubstring(s[1:], sub)
    else:
        return False
    return "stub"

def recursiveReverseList(L):
    '''
    Tbe parameter L is a list containing any items. This function returns
    the list L in reverse order.
    - Your solution must use recursion in order to receive credit.
    '''
    if (len(L) == 0):
        return L
    elif (len(L) > 0):
        return [L[-1]]+recursiveReverseList(L[0:len(L)-1])
    return "stub"
