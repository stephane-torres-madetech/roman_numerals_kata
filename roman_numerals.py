
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
    units = roman_numerals[get_number_of_units(num)]

    if get_number_length(num) == 2:
        result = get_roman_tens(num) + units
    
    
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
    if get_number_of_tens(num) < 4:
        for i in range(get_number_of_tens(num)):
            print(i, 'iiiiiiiiiii')
            print(num, 'num')
            result += 'X'
    elif get_number_of_tens(num) == 4:
        result = 'XL'
    elif get_number_of_tens(num) == 5:
        result = 'L'
    elif get_number_of_tens(num) > 5 and get_number_of_tens(num) < 9:
        result = 'L'
        remainder = get_number_of_tens(num) - 5
        print(remainder, 'tttttttttttttttttttttttt')
        for i in range(remainder):
            result += 'X'
    else: result = 'XC'

    return result


