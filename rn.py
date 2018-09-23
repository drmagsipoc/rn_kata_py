
def _handle_ones(num):
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
    except KeyError:
        print('invalid handle ones numer')
    return ones[num]


def convert(input):
    ones = _handle_ones(input % 10)
    return ones

convert(1)