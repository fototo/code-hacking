from clipboard import *
from color import color_text
from random import randint, random

f1 = (
        'Ola %s, muito obrigado!',
        'Ola %s, obrigado!',
        'Ola %s. Muito obrigado!',
        'Ola %s. Obrigado!',

        'Hey %s, muito obrigado!',
        'Hey %s, obrigado!',
        'Hey %s. Muito obrigado!',
        'Hey %s. Obrigado!',

        'Oi %s, muito obrigado!',
        'Oi %s, obrigado!',
        'Oi %s. Muito obrigado!',
        'Oi %s. Obrigado!',

        'Alo %s, muito obrigado!',
        'Alo %s, obrigado!',
        'Alo %s. Muito obrigado!',
        'Alo %s. Obrigado!',

        'Muito obrigado %s!',
        'Obrigado %s!',
        '%s, muito obrigado!',
        '%s, obrigado!',
     )

f2 = (
        'Tudo bem?',
        'Td bem?',
        'Tudo bem contigo?',
        'Td bem contigo?',
        'Tudo bem ctg?',
        'Td bem ctg?',

        'Como estas?',
        'Cm estas?',

        'Que contas de novo?',

        'Como vai isso?',
        'Como vai essa vida?',
        'Cm vai essa vida?',

        'Entao e novidades?',
        'Entao e novidades desse lado?',
        'Entao, novidades?',
        'Tao e novidades?',
        'Novidades?',
     )

f3 = (':)', ':D', '^^', ':]', '(:', ':p')


def frase(name):

    fi1 = f1[randint(1, len(f1)) - 1]
    if '%' in fi1:
        fi1 = fi1 % name

    fi2 = f2[randint(1, len(f2)) - 1]
    fi3 = f3[randint(1, len(f3)) - 1]

    return fi1 + ' ' + fi2 + ' ' + fi3


def sandy():
    print len(f1) * len(f2), 'possibilidades'


def main():

    text = ''
    old_text = ''

    while 1:

        old_text = text
        text = getClipboardData()

        if old_text != text:
            name = getClipboardData().strip()
            text = frase(name)

            setClipboardData(text)

            print color_text('=> %s: ' % name, 'WHITE', True), color_text('%s' % text, 'WHITE')


if __name__ == '__main__':
    main()
    # sandy()

