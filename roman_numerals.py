
roman_numerals = {
        1 : 'I',
        2 : 'II',
        3 : 'III',
        4 : 'IV',
        5 : 'V',
        6 : 'VI',
        7 : 'VII',
        8 : 'VIII',
        9 : 'IX',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M'
    }
def convert_to_roman_numeral(num):

    if num > 10 and num < 50:
        units = num - 10
        return 'X' + roman_numerals[units]
    else: return roman_numerals[num]