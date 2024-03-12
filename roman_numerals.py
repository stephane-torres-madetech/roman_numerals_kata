
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
    number_length = get_number_length(num)
    units = roman_numerals[get_number_of_units(num)]

    if number_length == 1:
        result = units

    if number_length == 2:
        result = get_roman_tens(num) + units
    else: result = roman_numerals[num]
    
    
    return result

def get_number_length(num):
    return len(str(num))

def get_number_of_units(num):
    string_num = str(num)
    return int(string_num[len(string_num) - 1])

def get_number_of_tens(num):
    string_num = str(num)
    return int(string_num[len(string_num) - 2])

def get_roman_tens(num):
    result = ''
    number_of_tens = get_number_of_tens(num)
    if number_of_tens < 4:
        for i in range(number_of_tens):
            result += 'X'
    elif number_of_tens == 4:
        result = 'XL'
    elif number_of_tens == 5:
        result = 'L'
    elif number_of_tens > 5 and number_of_tens < 9:
        result = 'L'
        remainder = number_of_tens - 5
        for i in range(remainder):
            result += 'X'
    else: result = 'XC'

    return result


