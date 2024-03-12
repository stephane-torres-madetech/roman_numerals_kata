# convert numbers into Roman numerals
# simplest cases of that 1 = I, 5 = V, 10 = X
from .. import roman_numerals
    


def testFiveReturnsV():
    assert roman_numerals.convert_to_roman_numeral(5) == 'V'

def testOneReturnsI():
    assert roman_numerals.convert_to_roman_numeral(1) == 'I'

def testTenReturnsX():
    assert roman_numerals.convert_to_roman_numeral(10) == 'X' 

def testFiftyReturnsL():
    assert roman_numerals.convert_to_roman_numeral(50) == 'L'

def testTwoReturnsII():
    assert roman_numerals.convert_to_roman_numeral(2) == 'II'
 
def testFourReturnsIV():
    assert roman_numerals.convert_to_roman_numeral(4) == 'IV' 

