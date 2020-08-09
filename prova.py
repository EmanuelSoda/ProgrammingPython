
def suffixArray(s):
    setups = sorted([(s[i : ], i) for i in range(0, len(s))])
    print(setups, '\n\n')
    return map(lambda x: x[1], setups)

def bwtViaSa(t):
    bw = []
    for si in suffixArray(t):
        if si == 0:
            bw.append('$')
        else:
            bw.append(t[si-1])

    return ''.join(bw)


print(bwtViaSa("Tomorrow_and_tomorrow_and_tomorrowTomorrow"))
