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

def test_thiry_one_returns_XXXI():
    assert roman_numerals.convert_to_roman_numeral(31) == 'XXXI'

def test_forty_returns_XL():
    assert roman_numerals.convert_to_roman_numeral(40) == 'XL'

def test_fourty_one_returns_XLI():
    assert roman_numerals.convert_to_roman_numeral(41) == 'XLI'

def test_one_digit_number_returns_1():
    assert roman_numerals.get_number_length(1) == 1

def test_two_digit_number_returns_2():
    assert roman_numerals.get_number_length(25) == 2

def get_number_tens_from_25():
    assert roman_numerals.get_number_of_tens(25) == 2