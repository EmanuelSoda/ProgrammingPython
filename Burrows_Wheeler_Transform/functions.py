import numpy as np

class not_a_string_error(TypeError):
    pass
class invalid_string_error(Exception):
    pass


def transform(string):
    """
    Burrow - Wheeler Transform (BWT)
    input: a string with or without a termination character not in the alphabet
    output: the BWT of the input string """

    # check if the input is a string
    if type(string) != str:
        raise not_a_string_error('The input ' + string + ' is not a string ')
    # the string must contains only one termination char
    elif string.count('$') > 1:
        raise invalid_string_error('The input ' + string + ' cointains more than one $' )

    # check if the last char contains the '$' otherwhise add it
    elif string[-1] != '$':
        string += '$'

    string_size = len(string)

    matrix = np.sort(np.array([string[-i :] + string[: -i] for i in np.arange(string_size)], dtype= '<U' + str(string_size)))
    # the final string is the concatenation of the last char of all the rows of the rotation matrix
    return str("".join([matrix[i][-1] for i in np.arange(string_size)]))






def inverse(bwt):
    '''
    Inverse of the Burrow - Wheeler Transform (BWT)
    input: the BWT of a string
    output: the original string '''

    if type(bwt) != str:
        raise not_a_string_error('The input ' + bwt + ' is not a string')
    elif bwt.count('$') != 1:
        raise invalid_string_error('The input ' + bwt + ' does not contain exactly one $ character')

    n = len(bwt)
    bwt_array = np.array(list(bwt))
    firstCol = np.sort(bwt_array)

    finalString = ''
    i = 0
    while len(finalString) != n:
        item = bwt_array[i]
        # the position is given by the index of the first occurrence in the first column of the rotation matrix plus the number of times that the item is present int the bwt till that moment
        itemindex = np.where(firstCol == item)[0][0] +  np.count_nonzero(bwt_array[: i] == item)
        # append the character to the top of the string
        finalString = firstCol[itemindex] + finalString
        i = itemindex

    # return the string without the '$'
    return finalString[1:]
