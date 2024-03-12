# convert numbers into Roman numerals
# simplest cases of that 1 = I, 5 = V, 10 = X
from .. import roman_numerals


def test_fifty_returns_L():
    assert roman_numerals.convert_to_roman_numeral(50) == 'L'
 

def test_returns_roman_for_one_to_ten():
    for i in range(1, 11):
        assert roman_numerals.convert_to_roman_numeral(i) == roman_numerals.roman_numerals[i]