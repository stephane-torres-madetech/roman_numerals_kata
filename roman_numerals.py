
def convert_to_roman_numeral(num):

    roman_numerals = {
        1 : 'I',
        2 : 'II',
        4 : 'IV',
        5 : 'V',
        6 : 'VI',
        10 : 'X',
        50 : 'L'
    }
    return roman_numerals[num]