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

def test_three_returns_III():
    assert roman_numerals.convert_to_roman_numeral(3) == 'III'

def test_returns_roman_for_one_to_ten():
    for i in range(1, 11):
        assert roman_numerals.convert_to_roman_numeral(i) == roman_numerals.roman_numerals[i]