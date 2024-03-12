
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

    result = 'X'

    if num <= 10 or num >= 50:
       result = roman_numerals[num]
    elif num > 10 and num <= 20:
        units = num - 10
        result += roman_numerals[units]
    elif num > 20 and num <= 30:
        units = num - 20
        result += 'X' + roman_numerals[units]
    else: 
        num > 30 and num <= 40
        units = num - 30
        result += 'XX' + roman_numerals[units]
    
    return result