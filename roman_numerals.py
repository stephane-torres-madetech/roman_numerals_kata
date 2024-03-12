
roman_numerals = {
        0 : '',
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

    result = ''
    # number_length = len(str(num))
    if num <= 10 or num >= 50:
       result = roman_numerals[num]
    elif num > 10 and num <= 20:
        result = 'X'
        units = num - 10
        result += roman_numerals[units]
    elif num > 20 and num <= 30:
        result = 'XX'
        units = num - 20
        result += roman_numerals[units]
    elif num > 30 and num < 40:
        result = 'XXX'
        units = num - 30
        result += roman_numerals[units]
    else:
        num >= 40 and num < 50
        result = 'XL'
        units = num - 40
        result += roman_numerals[units]
    
    return result

def get_number_length(num):
    return len(str(num))

def get_number_of_tens(num):
    return 2