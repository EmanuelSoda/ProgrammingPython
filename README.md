# Implementation description
## transform method
For the transform the method first checks if the input is a string and contains zero or one '$''.
In the case in which there is no '$' the methods adds it at the end of the string.
A rotation matrix (it is actually implemented as an array of strings) is constructed concataning the string end of the string starting from the -i character with the start of the string till the -i character. In the end the inverse is returned.


## inverse metho
For the inverse transform the method first checks if the input is a string with exactly one $ character.
Then it turns the string in a numpy array it sorts the array and reconstruct the first column of the rotation matrix.
A while loop is performed untill the output has the same length of the input string. In this loop is searched through the use of the indexes the order of the characters of the original string. In the end the original string is returned without the termination character
