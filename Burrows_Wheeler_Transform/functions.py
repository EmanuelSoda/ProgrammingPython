import numpy as np

class not_a_string_error(TypeError):
    pass
class invalid_string_error(Exception):
    pass

def check_input(string) -> str:
    """
    check_input
    input: a string with or without a termination character not in the alphabet
    output: the string containing the termination character
    """
    if type(string) != str:
        raise not_a_string_error('The input ' + string + ' is not a string ')
    # The string must contain only one termination char
    elif string.count('$') > 1:
        raise invalid_string_error('The input ' + string + ' cointains more than one $' )

    # check if the last char contains the '$' otherwise add it
    elif string[-1] != '$':
        string += '$'

    return string

def transform(string) -> str:
    """
    Burrow - Wheeler Transform (BWT)
    input: a string with or without a termination character not in the alphabet
    output: the BWT of the input string 
    """

    # Check if the input is a string
    string = check_input(string)

    string_size = len(string)

    matrix = np.sort(np.array([string[-i :] + string[: -i] for i in np.arange(string_size)], dtype= '<U' + str(string_size)))
    # The final string is the concatenation of the last char of all the rows of the rotation matrix
    return str("".join([matrix[i][-1] for i in np.arange(string_size)]))

def inverse(bwt) -> str:
    '''
    The inverse of the Burrow - Wheeler Transform (BWT)
    input: the BWT of a string
    output: the original string '''

    # Check if the input is a string
    bwt = check_input(bwt)

    n = len(bwt)
    bwt_array = np.array(list(bwt))
    firstCol = np.sort(bwt_array)

    finalString = ''
    i = 0
    while len(finalString) != n:
        item = bwt_array[i]
        
        # The position is given by the index of the first occurrence in the first column of the rotation 
        # matrix plus the number of times that the item is present in the bwt till that moment
        itemindex = np.where(firstCol == item)[0][0] + np.count_nonzero(bwt_array[: i] == item)
        
        # Append the character to the top of the string
        finalString = firstCol[itemindex] + finalString
        i = itemindex

    # Returing the string without the '$'
    return finalString[1:]
