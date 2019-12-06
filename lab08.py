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

def isAnagramHelp(l1, l2):
    if (len(l1) == len(l2)):
        if l1[0] in l2:
            i = l2.index(l1[0])
            l1.pop(0)
            l2.pop(i)
            if (l1 == l2):
                return True
            else:
                return isAnagramHelp(l1, l2)
        else:
            return False
    return "stub"

def isAnagram(s1, s2):
    '''
    Takes two strings and compares the characters in them to see if
    they are anagrams of each other
    '''
    
    if (len(s1) == len(s2)):
        if (s1 == s2):
            return True
        else:
            l1 = list(s1.lower())
            l2 = list(s2.lower())
            for i in range(len(l1)-1, -1, -1):
                if l1[i].isalnum():
                    continue
                else:
                    l1.pop(i)
            for i in range(len(l2)-1, -1, -1):
                if l2[i].isalnum():
                    continue
                else:
                    l2.pop(i)
            return isAnagramHelp(l1, l2)
    else:
        return False
    return "stub"

def isPalindrome(s):
    '''
    Determines whether or not a string is a Palindrome
    '''
    s = s.lower()
    if (len(s) > 0) and (len(s) <= 2):
        if s[0] == s[-1]:
            return True
    elif (len(s) > 2):
        if (s[0] == s[-1]):
            return isPalindrome(s[1:-1])
    return False

