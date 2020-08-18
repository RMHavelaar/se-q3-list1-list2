#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List1
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Robert Havelaar, Demo, Group C study group, I looked at Sara Beverton's repo AFTER I was finshed."

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


def match_ends(words):
    x = 0
    for word in words:
        if len(word) >= 2 and word[0].lower() == word[-1].lower():
            x += 1
    return x


def front_x(words):
    xlist = []
    alist = []

    for word in words:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)

    return sorted(xlist) + sorted(alist)


def sort_last(tuples):
    return sorted(tuples, key=sort_last_value)


def sort_last_value(t):
    return t[-1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.
def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.

    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\nfront_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\nsort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 9, 4), (2, 2)]),
         [(2, 2), (1, 3), (3, 9, 4), (1, 7)])


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
