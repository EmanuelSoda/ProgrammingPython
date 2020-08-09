import numpy as np
milleCaratteri =  'acctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgtgaccctgaacctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgac'

duemilaCaratteri = "acctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgtgaccctgaacctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacacctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgtgaccctgaacctgacctgacacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgacctgactgaccctgaccctgaccctgacccctgactgacccctgacctgacctgacctgacctgacctgacctgacctgac"

milleInverse = 'cggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggga$gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggccggggggggggggggggggggggggggggggggggggggggggggaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccaaaccccccccccccccccccccccccccccccccccccaaaaaaaacccccccccccaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccaaaaaaaaaaaaaccccaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccctttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttccccccccccccccccccccccccccccgcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'

duemilaInverse = 'cggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggaac$ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggccccggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaaaaaaaaaccccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttccccccccccccccccccccccccccccccccccccccccccccccccccccccccggcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'


def BWT(t):
    if type(t) != str:
        exit(0)
        # mettere eccezione

    if t[-1] != '$':
        t += '$'

    string_size = len(t)

    matrix = np.sort(np.array([t[-i :] + t[: -i] for i in np.arange(string_size)], dtype= '<U' + str(string_size)))
    #print(matrix)
    # prendo riga per riga le parole della matrice e gli prendo l'ultimo elemento e concateno per formare una stringa
    return "".join([matrix[i][-1] for i in np.arange(string_size)])




def inverseBWT(bwt):
    n = len(bwt)
    bwt_array = np.array(list(bwt))
    firstCol = np.sort(bwt_array)
    print('bwt_array: ', bwt_array)
    print('firstCol:  ', firstCol)
    #for in i in np.arange(n):
    i = 0
    finalString = ''
    while len(finalString) != n:
        item = bwt_array[i]
        itemindex = np.where(firstCol == item)[0][0] # qui ci deve essere un più qualcosa che mi dice è la tot lettera uguale
        print('carattere first col:', firstCol[itemindex], 'index: ', itemindex)
        print('carattere bwt: ', item, 'index: ', itemindex)
        finalString = firstCol[itemindex] + finalString
        print(finalString)
        firstCol[itemindex]  = ''
        i = itemindex + np.size(np.where(firstCol == item)[0])



    return finalString[1: ]
    #QUESTO FUNZIONA
    # n = len(bwt)
    # matrix = np.empty(n, dtype = '<U' + str(n))
    #
    # for i in np.arange(n):
    #     matrix = np.array([bwt[i] + matrix[i] for i in np.arange(n)])
    #     matrix.sort()
    # return matrix[0][1:]

    # n = len(bwt)
    # bwt = np.array(list(bwt))
    # matrix = np.empty(n, dtype = '<U' + str(n))
    # for i in np.arange(n):
    #     for j in  np.arange(n):
    #         matrix[j] = bwt[j] + matrix[j]
    #     matrix.sort()
    #     #print(matrix)
    #
    # #print(matrix)
    # #print('matrix[3]:', matrix[3])
    # return matrix[0][1:]


#potrei mettere l'opzione verbose
#finalString = BWT(duemilaCaratteri)
#print(finalString)
#out_file = open("test.txt", "w")
#out_file.write(finalString)
#print(finalString)


#inversTrasf = inverseBWT('annb$aa')
#g$actc
inversTrasf = inverseBWT('cctt$aggg')
# tctat$
#inversTrasf = inverseBWT('cctt$aggg')
#inversTrasf = inverseBWT(milleInverse)
#inversTrasf = inverseBWT(duemilaInverse)
print('La stringa orginale è:', inversTrasf)

print('FINE')
