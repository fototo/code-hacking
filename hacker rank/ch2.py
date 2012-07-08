

# nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

nd = {'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 9,
      'ten': 10,
      'eleven': 11,
      'twelve': 12,
      'thirteen': 13,
      'fourteen': 14,
      'fifteen': 15,
      'sixteen': 16,
      'seventeen': 17,
      'eighteen': 18,
      'nineteen': 19,
      'zero': 0}

dd = {'twenty': 2,
      'thirty': 3,
      'forty': 4,
      'fourty': 4,
      'fifty': 5,
      'sixty': 6,
      'seventy': 7,
      'eighty': 8,
      'ninety': 9}


def caesar(phrase, key):
    phrase = phrase.lower()
    result = ''
    for c in phrase:
        o = ord(c)

        if o >= 97 and o <= 122:

            if o + key > 122: o -= 26
            if o + key < 97: o += 26

            result += chr(o + key)
        else:
            result += c

    return result


def guess(tosolve, r=None):

    if len(tosolve.split(' ')) == 1 and r==None:
      return guess(tosolve, r=0)

    if r == None:
        thousand = tosolve.split(' ')[1][:-1]
        r = ord('t') - ord(thousand[0]) if len(thousand) == len('thousand') else 0
        if caesar(thousand, r) == 'thousand':
            return caesar(tosolve, r)
        else:
            return guess(tosolve, r=0)

    elif r > 27:
        return False

    else:
        c = caesar(tosolve, r)
        # print '==>', c, r
        if len(filter(lambda t: t == c, dd.keys())) != 0 or len(filter(lambda t: t == c, nd.keys())) != 0:
            return c
        else:
            return guess(tosolve, r + 1)




def conv2numeric(phrase):

    phrase = phrase.lower()
    phrase = phrase.replace(' and', ',')
    # print phrase

    shard = phrase.split(',')
    shard = map(lambda p: p.strip(), shard)

    soma = []
    for s in shard:
      if 'thousand' in s:
        thousand = s.split(' ')[0]
        v = nd[thousand] * 1000
        soma.append(v)

      elif 'hundred' in s:
        hundred = s.split(' ')[0]
        v = nd[hundred] * 100
        soma.append(v)

      elif '-' in s:
        dec, unit = s.split('-')
        v = dd[dec]*10
        soma.append(v)
        v = nd[unit]
        soma.append(v)

      elif s in dd.keys() and s not in nd.keys():
        v = dd[s]*10
        soma.append(v)
        # raise Exception('10 but not unit')

      elif s not in dd.keys() and s in nd.keys():
        v = nd[s]
        soma.append(v)

      else:
        # seven thousand, seven hundred, eighty
        print phrase
        raise Exception('New case in conv2numeric')

    return sum(soma)

f = open('list.txt', 'r')
data = f.read()
f.close()
name_list = data.split('\n')

name_list = [n.strip().lower() for n in name_list if n != '']

def newGuess(s):
  v = [(caesar(s, i), i) for i in range(0, 26) if len(filter(lambda word: word in name_list, caesar(s, i).split(' '))) > 0]
  if len(v) == 1:
    return v[0]
  elif len(v) == 0:
    return False, False
  else:
    rep = [len(filter(lambda w: w in name_list,  t[0].split(' ')))for t in v]
    return sorted(zip(rep, v))[-1][1]

def solveCypher(answer, question):
    v = newGuess(answer)
    if v[0] != False:
        result = caesar(question, v[1])
        tou = map(lambda l: l.isupper(), question)
        result2 = map(lambda w: w[1] if w[0]==False else w[1].upper(), zip(tou, result))
        return ''.join(result2)
    else:
        return False


if __name__ == '__main__':
    # tosolve = 'ymwjj ymtzxfsi, knaj mzsiwji fsi ymnwyd-tsj'
    # t = guess(tosolve)
    # t = t if t != False else tosolve

    # print guess('pfuqv-cfsb')
    # print conv2numeric('sixty-five')
    # print guescs('grebenqvbtencul')
    # print guess('aHR0cDovL2VuLndpa2lwZWRpYS5vcmcvd2lraS9MaXN0X29mX25vdmVsaXN0')
    # for i in range(-27, 27):
    # print caesar('Imxfqd Fqhue', 14)
    # print caesar('Jqdadmpuasdmbtk', 14)


    # print newGuess('Imxfqd Fqhue')
    # print caesar('Jqdadmpuasdmbtk', 14)

    # print caesar('aHR0cDovL2VuLndpa2lwZWRpYS5vcmcvd2lraS9MaXN0X29mX25vdmVsaXN0', 0)

    # print 'xxx'.split(' ')

    print newGuess('Ijgwf Ktc')
    print newGuess('Bdwru Kqjacr Vrccj')
    print newGuess('Drxqbjxix Zfqv')
    print newGuess('Imxfqd Fqhue')

    # print conv2numeric(t)
    # print conv2numeric('eight thousand and seventy-five')
    # print conv2numeric('seven thousand, seven hundred, eighty')
    # print conv2numeric('one thousand, seventeen')
