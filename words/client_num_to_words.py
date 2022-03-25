
#CONSTANTS ONLY USED HERE
from token import GREATER


GREATERS = ('', 'thousand', 'million', 'billion', 'trillon')

PLACED_VALUES = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred',
}


def chunk_converter(chunk:int) -> str:
    if chunk in PLACED_VALUES:
        return PLACED_VALUES[chunk]
    response = ''
    if chunk > 99:
        c = int(chunk / 100)
        chunk = int(chunk % 100)
        response += PLACED_VALUES[c] + ' hundred '
    if chunk in PLACED_VALUES:
        response += PLACED_VALUES[chunk]
    else:
        unit = int(chunk % 10)
        response +=  PLACED_VALUES[chunk-unit] + ' ' + PLACED_VALUES[unit] 

    return response
 

def convert_to_word(number: int) -> str:
    if number == 0:
        return 'zero'
    words = list()
    count= 0
    while number > 0:
        chunk = int(number%1000)
        word = '{} {}'.format(chunk_converter(chunk), GREATERS[count])
        words.append(word)
        number = int(number / 1000)
        count += 1
    
    return ' '.join(words[::-1])
