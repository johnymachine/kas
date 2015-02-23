# -*- coding: utf-8 -*-
import hammcoder
import binpacker
import errormaker


def doHammingByteTest():
    byte = "00110011"
    result = "0010101100011"
    calculated = hammcoder.doHammingByte(byte)
    assert result == calculated


def fixHammingErrorTest():
    byte = "0010101100011"
    pos = 1
    result = "0110101100011"
    calculated = hammcoder.fixHammingError(byte, pos)
    #print byte
    #print calculated
    assert result == calculated


def calculateHammingSyndromTest():
    byte = "0010101100010"
    result = hammcoder.calculateHammingSyndrom(byte)
    #print result


def undoHammingByteTest():
    byte = "00110011"
    result = "00110011"
    calculated = \
    hammcoder.undoHammingByte(hammcoder.doHammingByte(byte))["output"]
    assert result == calculated


def hammingEncodeTest():
    buff = ["00110011", "00110011"]
    result = ["0010101100011", "0010101100011"]
    calculated = hammcoder.hammingEncode(buff)
    #print calculated
    assert result == calculated


def hammingDecodeTest():
    buff = ["0010101100011", "0010101100011"]
    result = ["00110011", "00110011"]
    calculated = hammcoder.hammingDecode(buff)
    #print calculated
    assert result == calculated["output"]


def writeReadTest():
    output = ["0010101100011", "1000110000001", "0000110000001"]
    with open("temp.bin", "wb") as ofile:
            binpacker.writeBinaryToEncode(ofile, output)
    with open("temp.bin", "rb") as ifile:
            buff = binpacker.readBinaryToDecode(ifile)
    #print output
    #print buff
    assert output == buff


def encodeDecodeTest():
    toencode = list()
    toencode.append(bin(ord("f"))[2:].zfill(8))
    encoded = hammcoder.hammingEncode(toencode)
    decoded = hammcoder.hammingDecode(encoded)
    print toencode
    print decoded
    assert toencode == decoded["output"]


def makeErrorTest():
    output = ["0010101100011", "1000110000001", "0000110000001"]
    print output
    result = errormaker.makeRandomError(output)
    print result
    assert output != result


if __name__ == "__main__":
    #doHammingByteTest()
    fixHammingErrorTest()
    #calculateHammingSyndromTest()
    #hammingDecodeTest()
    #readBinaryToEncodeTest()
    #hammingEncodeTest()
    #readBinaryToDecodeTest()
    #writeReadTest()
    #encodeDecodeTest()
    #makeErrorTest()