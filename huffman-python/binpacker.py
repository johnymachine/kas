# -*- coding: utf-8 -*-
import struct
SIZE = "I"
SIZEB = "B"


def stringToByteList(txt):
    byteList = list()
    for to in range(0, len(txt), 8):
        byteList.append(int(txt[to:to + 8], 2))
    return byteList


def byteListToString(byteList):
    txt = ""
    for element in byteList:
        txt = txt + bin(element)[2:].zfill(8)
    return txt


def occurrenceToByteList(occurrence):
    byteList = list()
    for key in occurrence:
        byteList.append(ord(key))
        byteList.append(occurrence[key])
    return byteList


def byteListToOccurrence(byteList):
    occurrence = dict()
    for index in range(0, len(byteList), 2):
        occurrence[chr(byteList[index])] = byteList[index + 1]
    return occurrence


def packData(output, occurrence):
    pack = fillZeros(output)
    sByte = stringToByteList(pack["output"])
    oByte = occurrenceToByteList(occurrence)
    sBytel = len(sByte)
    oBytel = len(oByte)
    buf = struct.pack(SIZEB, pack["filled"])
    buf = buf + struct.pack(SIZE, sBytel)
    buf = buf + struct.pack(SIZE, oBytel)
    buf = buf + struct.pack(SIZEB * sBytel, *sByte)
    buf = buf + struct.pack((SIZEB + SIZE) * (oBytel / 2), *oByte)
    return buf


def unpackData(buf):
    sizeb = struct.calcsize(SIZEB)
    size = struct.calcsize(SIZE)
    filled = struct.unpack(SIZEB, buf[:sizeb])[0]
    buf = buf[sizeb:]
    sBytel = struct.unpack(SIZE, buf[0:size])[0]
    buf = buf[size:]
    oBytel = struct.unpack(SIZE, buf[0:size])[0]
    buf = buf[size:]
    sByte = struct.unpack(SIZEB * sBytel, buf[:sizeb * sBytel])
    buf = buf[sizeb * sBytel:]
    oByte = struct.unpack((SIZEB + SIZE)
    * (oBytel / 2), buf[:oBytel * size * sizeb])
    return {
            'output': stripZeros(byteListToString(sByte), filled)["output"],
            'occurrence': byteListToOccurrence(oByte)
        }


def fillZeros(txt):
    tofill = 8 - (len(txt) % 8)
    return {
        'filled': tofill,
        'output': txt + "0" * tofill
        }


def stripZeros(txt, tostrip):
    return {
        'striped': tostrip,
        'output': txt[: - tostrip]
        }


def readBinaryToEncode(ifile):
    txt = list()
    byte = ifile.read(1)
    while byte:
        txt.append(byte)
        byte = ifile.read(1)
    return txt


def readBinaryToDecode(ifile):
    return ifile.read()