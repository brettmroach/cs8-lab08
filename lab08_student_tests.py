# lab08_student_tests
# Brett Roach
# 6907380

from lab08 import recursiveDigitSum

def test_recursiveDigitSum_1():
    for num in range(0, 10):
        assert recursiveDigitSum(num) == num

def test_recursiveDigitSum_2():
    assert recursiveDigitSum(647) == 17

def test_recursiveDigitSum_3():
    assert recursiveDigitSum(100000) == 1

from lab08 import recursiveSubstring

def test_recursiveSubstring_1():
    for alph in 'abcdefg':
        assert recursiveSubstring('abcdefg', alph) == True

def test_recursiveSubstring_2():
    assert recursiveSubstring('substring', 'string') == True

def test_recursiveSubstring_3():
    assert recursiveSubstring('homeownership', 'meow') == True

def test_recursiveSubstring_4():
    for num in '0123456789':
        assert recursiveSubstring('abcdefghijklmnopqrstuvwxyz', num) == False

from lab08 import recursiveReverseList

def test_recursiveReverseList_1():
    assert recursiveReverseList([]) == []

def test_recursiveReverseList_2():
    assert recursiveReverseList([1, 2, 3]) == [3, 2, 1]

def test_recursiveReverseList_3():
    assert recursiveReverseList(['a']) == ['a']

from lab08 import isAnagram

def test_isAnagram_1():
    assert isAnagram("Eleven plus two", "Twelve plus one") == True

def test_isAnagram_2():
    assert isAnagram('Hello', 'Helo') == False

def test_isAnagram_3():
    assert isAnagram('This is not', 'The same as this') == False

def test_isAnagram_4():
    assert isAnagram("School master","The Classroom") == True

from lab08 import isPalindrome

def test_isPalindrome_1():
    for i in range(1, 4):
        assert isPalindrome('a'*i) == True

def test_isPalindrome_2():
    assert isPalindrome('') == False

def test_isPalindrome_3():
    assert isPalindrome("Redivider") == True


