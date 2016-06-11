#!/usr/bin/env python2
#
# rail fence cipher implementation with optional offset feature
#
# for educational use only! (rail fence cipher is a very weak cipher.)
#
# https://en.wikipedia.org/wiki/Rail_fence_cipher
#


def printFence(fence):
    for rail in range(len(fence)):
        print ''.join(fence[rail])
    
def encryptFence(plain, rails, offset=0, debug=False):
    cipher = ''

    # offset
    plain = '#'*offset + plain

    length = len(plain)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    # print pretty fence
    if debug:
        printFence(fence)

    # read fence
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher


def decryptFence(cipher, rails, offset=0, debug=False):
    plain = ''

    # offset
    if offset:
        t = encryptFence('o'*offset + 'x'*len(cipher), rails)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1

    # print pretty fence
    if debug:
        printFence(fence)

    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain


if __name__ == "__main__":
    plain = "Proprietary software tends to have malicious features. The point is with a proprietary program, when the users don't have the source code, we can never tell. So you must consider every proprietary program as potential malware."
    print plain
    cipher = encryptFence(plain, 6, offset=4, debug=True)
    print cipher
    plain2 = decryptFence(cipher, 6, offset=4, debug=True)
    print plain2
