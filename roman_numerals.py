
def ConvertToRomanNumeral(num):

    roman_numerals = {
        1 : 'I',
        2 : 'II',
        4 : 'IV',
        5 : 'V',
        10 : 'X',
        50 : 'L'
    }
    return roman_numerals[num]