#!/usr/bin/env python3

from secrets import choice
from sys import argv

path = 'eff_large_wordlist.txt'

def read_wordlist():
    wordlist = {}
    with open(path, 'r') as f:
        for word in f:
            pair = [x.rstrip() for x in word.split('\t')]
            wordlist[int(pair[0])] = pair[1]
    return wordlist

def roll_dice():
    return choice(range(1, 7))

def roll_5_dice():
    n = 0
    for i in range(4, -1, -1):
        n += (10**i) * roll_dice()
    return n

def get_word(n, wordlist):
    if n not in wordlist:
        print('Error, index ' + str(n) + ' not in wordlist')
        exit()
    return wordlist[n]

def main():
    if (len(argv) != 2):
        print('Error: missing argument. Usage: ./diceware [number of words]')
        exit()
    if not argv[1].isdigit():
        print('Error: invalid argument. Usage: ./diceware [number of words]')
        exit()
    n = int(argv[1])
    wordlist = read_wordlist()
    words = ''
    print('')
    for i in range(n):
        diceroll = roll_5_dice()
        word = get_word(diceroll, wordlist)
        print(str(diceroll) + ' --> ' + word)
        words += word + ' '
    print('\nYour words are: ' + words + '\n')

if __name__ == "__main__":
    main()
