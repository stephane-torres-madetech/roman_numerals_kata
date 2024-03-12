# convert numbers into Roman numerals
# simplest cases of that 1 = I, 5 = V, 10 = X
from .. import roman_numerals
 
def test_five_returns_V():
    assert roman_numerals.convert_to_roman_numeral(5) == 'V'

def test_one_returns_I():
    assert roman_numerals.convert_to_roman_numeral(1) == 'I'

def test_ten_returns_X():
    assert roman_numerals.convert_to_roman_numeral(10) == 'X' 

def test_fifty_returns_L():
    assert roman_numerals.convert_to_roman_numeral(50) == 'L'

def test_two_returns_II():
    assert roman_numerals.convert_to_roman_numeral(2) == 'II'
 
def test_four_returns_IV():
    assert roman_numerals.convert_to_roman_numeral(4) == 'IV' 

def test_six_returns_VI():
    assert roman_numerals.convert_to_roman_numeral(6) == 'VI'