# -*- coding: utf-8 -*-
from random import randint
from hammcoder import fixHammingError


def makeSingleError(output):
    result = list()
    for item in output:
        pos = randint(1, 12)
        result.append(fixHammingError(item, pos))
    return result


def makeDoubleError(output):
    return makeSingleError(makeSingleError(output))


def makeTripleError(output):
    return makeSingleError(makeSingleError(makeSingleError(output)))


def makeRandomError(output):
    result = list()
    for item in output:
        pos = randint(0, 12)
        pos1 = randint(0, 12)
        if pos > pos1:
            result.append(fixHammingError(item, pos))
        elif pos < pos1:
            result.append(fixHammingError(fixHammingError(item, pos), pos1))
        else:
            result.append(
                fixHammingError(
                    fixHammingError(
                        fixHammingError(item, pos), pos1), pos * pos1 % 13))
    return result