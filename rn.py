
def _ones(num):
    try:
        ones = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }
        return ones[num % 10]
    except KeyError:
        return ''



def _tens(num):
    try:
        tens = {
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC',
        }
        return tens[(num // 10) % 10]
    except KeyError:
        return ''


def _dreds(num):
    try:
        hundreds = {
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM',
        }
        return hundreds[(num // 100) % 10]
    except KeyError:
        return ''


def _sands(num):
    try:
        thousands = {
            1: 'M',
            2: 'MM',
            3: 'MMM',
        }
        return thousands[(num // 1000) % 10]
    except KeyError:
        return ''


def convert(input):
    roman_numeral = _sands(input) + _dreds(input) + _tens(input)  + _ones(input)
    return roman_numeral
