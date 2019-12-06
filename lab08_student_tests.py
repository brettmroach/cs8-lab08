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
