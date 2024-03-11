# convert numbers into Roman numerals
# simplest cases of that 1 = I, 5 = V, 10 = X
from .. import roman_numerals
    
    

def testFiveReturnsV():
    assert roman_numerals.ConvertToRomanNumeral(5) == 'V'

def testOneReturnsI():
    assert roman_numerals.ConvertToRomanNumeral(1) == 'I'

def testTenReturnsX():
    assert roman_numerals.ConvertToRomanNumeral(10) == 'X' 

def testFiftyReturnsL():
    assert roman_numerals.ConvertToRomanNumeral(50) == 'L'

def testTwoReturnsII():
    assert roman_numerals.ConvertToRomanNumeral(2) == 'II'
 
