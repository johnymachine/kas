# -*- coding: utf-8 -*-
import struct


def readBinaryToEncode(ifile):
    txt = list()
    byte = ifile.read(1)
    while byte:
        txt.append(bin(struct.unpack("B", byte)[0])[2:].zfill(8))
        byte = ifile.read(1)
    return txt


def readBinaryToDecode(ifile):
    txt = list()
    byte = ifile.read(2)
    while byte:
        txt.append(bin(struct.unpack("H", byte)[0])[2:].zfill(13)[-13:])
        byte = ifile.read(2)
    return txt


def writeBinaryToEncode(ofile, output):
    for item in output:
        ofile.write(struct.pack("H", int(item, 2)))


def writeBinaryToDecode(ofile, output):
    for item in output:
        ofile.write(struct.pack("B", int(item, 2)))