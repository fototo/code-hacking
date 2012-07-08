# http://www.krista.cc/posts/48


def binaryString(strB):
    strB = ''.join([bstr(ord(l)) for l in strB])
    return strB


def s(qqCoisa):
    return sum(map(lambda x: len(x), qqCoisa))

bstr     = lambda n, l=16: n<0 and binarystr((2L<<l)+n) or n and bstr(n>>1).lstrip('0')+str(n&1) or '0'
bstrSize = lambda s, m: '0' * (m - len(s)) + s


def LZ77(arrayB, encLen=5):
    # http://en.wikipedia.org/wiki/LZ77_(algorithm)
    convDic = {}

    arrayF = []
    jump = 0
    for i in range(len(arrayB) - encLen + 1):

        if sum(map(lambda x: len(x), arrayB[i:i + encLen])) != encLen:
            arrayF.append(arrayB[i])
            continue

        letters = ''.join(arrayB[i:i + encLen])

        if jump > 0:
            jump -= 1
            continue

        if letters not in convDic.keys():
            convDic[letters] = i
            arrayF.append(arrayB[i])
        else:
            arrayF.append((convDic[letters], encLen))
            jump = 2

    map(arrayF.append, arrayB[-(encLen - 1):])

    if encLen == 3:
        return arrayF
    else:
        return LZ77(arrayF, encLen - 1)


def runL(_s, last=None, count=1, result=[]):
    # http://en.wikipedia.org/wiki/Run-length_encoding
    t = []
    for i in range(len(_s) - 1):
        t.append([_s[i], _s[i + 1]])

    b = map(lambda a: a[0] != a[1], t)
    b.append(True)

    ms = zip(range(len(_s)), _s, b)

    intervalo = map(lambda x: x[0], filter(lambda i: i[2] == True, ms))

    if intervalo[0] != 0:
        intervalo = [0] + intervalo

    _t = zip(intervalo[:-1], intervalo[1:])

    for i in range(len(_t)):
        old = _t[i]
        if i == 0:
            _t[i] = (old[0], old[1] + 1)

        elif i == len(_t) - 1:
            _t[i] = (old[0] + 1, old[1] + 1)
        else:
            _t[i] = (old[0] + 1, old[1] + 1)

    # print _t

    cod = map(lambda i: _s[i[0]:i[1]], _t)

    return map(lambda e: (len(e), e[0]), cod)


strB = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec felis ante, tristique condimentum consequat eu, imperdiet id mi. Fusce quam nisi, tristique facilisis feugiat a, ullamcorper ac nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Curabitur eu tellus ac justo aliquam porta id nec leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam et orci metus, vulputate auctor ligula. Vivamus vitae enim varius ipsum feugiat pellentesque. Nam aliquet sodales porta. Sed rhoncus fermentum dolor, porta hendrerit sem hendrerit nec. Donec fringilla, erat ut aliquet dictum, enim dui auctor eros, a viverra mauris quam vel ligula. Suspendisse pretium eros nec orci pulvinar dapibus. Mauris fringilla velit id enim dignissim lobortis. Nulla tristique turpis eu mauris egestas molestie. Nullam lacinia elit nibh. Sed vulputate arcu non dui dapibus sit amet commodo quam cursus.

In hac habitasse platea dictumst. Suspendisse tincidunt semper nisl, sit amet elementum ligula ultrices vel. Morbi cursus, velit eu venenatis accumsan, tellus erat dapibus diam, eget laoreet nulla arcu at urna. Sed ornare mi pellentesque eros dignissim volutpat. Phasellus varius blandit ligula, vitae commodo tellus egestas in. Praesent placerat eros non elit commodo at dapibus metus pulvinar. In sodales hendrerit nulla, quis laoreet tortor iaculis ac. Curabitur in pellentesque nunc. Vivamus gravida eros ac augue iaculis vel feugiat ligula malesuada.

Aliquam risus mauris, rhoncus non mollis ac, commodo ut metus. Nullam at purus justo, sed gravida nunc. Proin et velit sem. Proin vulputate, dolor et volutpat aliquet, nunc nibh sodales massa, ut tempor justo ligula et sapien. Aliquam id elit erat. Suspendisse sem nisl, accumsan ac ultricies at, ullamcorper sed est. Proin sed mi sit amet lacus consequat interdum. Cras ac orci eget neque posuere aliquam at et nisl. Quisque pellentesque imperdiet tortor, sit amet ultrices mi tincidunt ut. Ut ullamcorper pulvinar est.

Fusce in tortor felis. Nulla ac sodales lorem. Integer cursus sodales auctor. In eu leo metus, a pharetra mauris. Donec ut nulla odio, in varius neque. Praesent ac augue purus. Sed eget turpis quis felis mattis ultrices. Integer ante metus, accumsan at fermentum in, laoreet in augue. Donec consequat sagittis mauris et tristique. Curabitur aliquam sem non lorem porta elementum. Sed lacinia dapibus pulvinar. Suspendisse porta eros sit amet mauris eleifend sit amet dapibus diam rutrum.

Duis sodales, mi ut bibendum viverra, tellus ipsum vulputate velit, et laoreet elit dolor nec massa. Donec tincidunt, est non venenatis condimentum, elit enim fringilla nulla, vel venenatis nisl ipsum et metus. Ut ornare tempus vehicula. Pellentesque ac leo sapien. Cras at sollicitudin urna. Fusce malesuada, ante blandit iaculis molestie, tellus lectus commodo velit, sit amet congue dui dui at elit. Vivamus dolor metus, fringilla a tempor sit amet, posuere sit amet mi. Morbi pharetra nulla vel lorem porta accumsan. Phasellus dapibus posuere laoreet. Etiam et elit ac dolor bibendum condimentum. Vivamus sit amet est convallis lorem consectetur mollis. Suspendisse eu porttitor ipsum. Praesent adipiscing adipiscing consequat. Vivamus ultrices, purus a cursus egestas, urna lacus dapibus erat, ac.
"""

f = open('lorem.txt', 'r')
strB = f.read()
f.close()


arrayF = LZ77(strB)
print s(strB), '==>', s(arrayF), '%s%%' % (100 * s(arrayF) / float(s(strB)))


dd = []
for l in strB:
    if l not in dd:
        dd.append(l)

dd = [len(bstr(ord(d))) for d in dd]
m = max(dd)


strB = [bstrSize(bstr(ord(d)), m) for d in strB]


arrayF = runL(strB)
print s(strB), '==>', s(arrayF), '%s%%' % (100 * s(arrayF) / float(s(strB)))




# arrayF = LZ77(strB, encLen=4)
# print s(strB), '==>' , s(arrayF), '%s%%' % (100*s(arrayF)/float(s(strB)))





# http://en.wikipedia.org/wiki/Huffman_coding