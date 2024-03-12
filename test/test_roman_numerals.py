# convert numbers into Roman numerals
# simplest cases of that 1 = I, 5 = V, 10 = X
from .. import roman_numerals


def test_fifty_returns_L():
    assert roman_numerals.convert_to_roman_numeral(50) == 'L'

def test_one_hundred_returns_C():
    assert roman_numerals.convert_to_roman_numeral(100) == 'C'
 
def test_five_hundred_returns_D():
    assert roman_numerals.convert_to_roman_numeral(500) == 'D'

def test_one_thousand_returns_M():
    assert roman_numerals.convert_to_roman_numeral(1000) == 'M'

def test_returns_roman_for_one_to_ten():
    for i in range(1, 11):
        assert roman_numerals.convert_to_roman_numeral(i) == roman_numerals.roman_numerals[i]

def test_eleven_returns_XI():
    assert roman_numerals.convert_to_roman_numeral(11) == 'XI'

def test_twenty_returns_XX():
    assert roman_numerals.convert_to_roman_numeral(20) == 'XX'

def test_twenty_one_returns_XXI():
    assert roman_numerals.convert_to_roman_numeral(21) == 'XXI'