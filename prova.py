from Burrows_Wheeler_Transform import transform
from Burrows_Wheeler_Transform import inverse


milleCaratteri =  'acctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgtgaccctgaacctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgac'

stringa = "Tomorrow_and_tomorrow_and_tomorrowTomorrow"

trasformata = transform(milleCaratteri)
print(trasformata)
inversa = inverse(trasformata)
print(inversa)
