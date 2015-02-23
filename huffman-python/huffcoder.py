# -*- coding: utf-8 -*-
from collections import Counter
from heapq import heappush, heappop, heapify


def huffmanEncode(txt):
    """Generates complete huffman encoding"""
    occurrence = getOccurrence(txt)
    huffmancodes = getHuffmanCodes(occurrence)
    huffmandict = dict(huffmancodes)
    output = ""
    for ch in txt:
        output = output + huffmandict[ch]
    return {
            'occurrence': occurrence,
            'huffmancodes': huffmancodes,
            'output': output
        }


def huffmanDecode(txt, occurrence):
    """Generates complete huffman decoding"""
    output = ""
    huffmancodes = getHuffmanCodes(occurrence)
    fr = 0
    for to in range(1, len(txt) + 1):
        for symbol, code in huffmancodes:
            if code == txt[fr:to]:
                output = output + symbol
                fr = to
                break
    return {
            #'huffmancodes': huffmancodes,
            'output': output,
            #'occurrence': getOccurrence(output),
        }


def getOccurrence(txt):
    return dict(Counter(txt))


def getHuffmanCodes(charfreq):
    """Huffman encode dict with chars and occurence"""
    heap = [[oc, [ch, ""]] for ch, oc in charfreq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))