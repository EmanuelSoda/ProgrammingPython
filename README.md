[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# Python Scientific Programming project
This is a simple implementation of the Burrows–Wheeler transform in python using numpy. 

## Built With
* Jupyter notebook
* Python

## Prerequisites 
* numpy 
```sh
pip install numpy
```
or
```sh
conda install numpy
```

## Usage

```python
from Burrows_Wheeler_Transform import transform
from Burrows_Wheeler_Transform import inverse

finalString = transform('Banana') # return  a$nnBaa
originalString = inverse('a$nnBaa') # return Banana
```




## Implementation description
###  transform method
For the transform the method first checks if the input is a string and contains zero or one '$''.
In the case in which there is no '$' the methods adds it at the end of the string.
A rotation matrix (it is actually implemented as an array of strings) is constructed concataning the string end of the string starting from the -i character with the start of the string till the -i character. In the end the inverse is returned.


### inverse method 
For the inverse transform the method first checks if the input is a string with exactly one $ character.
Then it turns the string in a numpy array it sorts the array and reconstruct the first column of the rotation matrix.
A while loop is performed untill the output has the same length of the input string. In this loop is searched through the use of the indexes the order of the characters of the original string. In the end the original string is returned without the termination character




## Authors
* Emanuel Michele Soda
