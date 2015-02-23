# -*- coding: utf-8 -*-


def hammingEncode(buff):
    """Generates complete hamming encoding"""
    output = list()
    newbyte = None
    for byte in buff:
        newbyte = doHammingByte(byte)
        output.append(newbyte)
    return output


def hammingDecode(buff):
    """Generates complete hamming decoding"""
    output = list()
    syn = None
    log = list()
    for num, byte in enumerate(buff):
        syn = calculateHammingSyndrom(byte)
        #print syn
        #print byte
        if syn["S"] == 0 and syn["SX"] == 0:
            output.append(undoHammingByte(byte))
        elif syn["S"] > 0 and syn["SX"] == 1:
            byte = fixHammingError(byte, syn["S"])
            output.append(undoHammingByte(byte))
            log.append("Single Error detected and FIXED at byte: " + str(num))
        elif syn["S"] > 0 and syn["SX"] == 0:
            output.append(undoHammingByte(byte))
            log.append("Double Error detected at byte: " + str(num))
        #also aplies to Single Error at [0] == Parity bit
        elif syn["S"] == 0 and syn["SX"] == 1:
            output.append(undoHammingByte(byte))
            log.append("Triple Error detected at byte: " + str(num))
        else:
            log.append("Decoding Error detected at byte: " + str(num))
            output.append(undoHammingByte(byte))
    return {"output": output, "log": log}


def doHammingByte(byte):
    """Secures one byte by hamming code"""
    #P1 = A1 xor A2 xor A4 xor A5 xor A7
    P1 = str(
        int(byte[0]) ^
        int(byte[1]) ^
        int(byte[3]) ^
        int(byte[4]) ^
        int(byte[6])
        )
    #P2 = A1 xor A3 xor A4 xor A6 xor A7
    P2 = str(
        int(byte[0]) ^
        int(byte[2]) ^
        int(byte[3]) ^
        int(byte[5]) ^
        int(byte[6])
        )
    #P3 = A2 xor A3 xor A4 xor A8
    P3 = str(
        int(byte[1]) ^
        int(byte[2]) ^
        int(byte[3]) ^
        int(byte[7])
        )
    #P4 = A5 xor A6 xor A7 xor A8
    P4 = str(
        int(byte[4]) ^
        int(byte[5]) ^
        int(byte[6]) ^
        int(byte[7])
        )
    #PX = C1 to C12
    PX = str(
        int(P1) ^
        int(P2) ^
        int(byte[0]) ^
        int(P3) ^
        int(byte[1]) ^
        int(byte[2]) ^
        int(byte[3]) ^
        int(P4) ^
        int(byte[4]) ^
        int(byte[5]) ^
        int(byte[6]) ^
        int(byte[7])
        )
    return PX + P1 + P2 + byte[0] + P3 + byte[1] + byte[2] +\
    byte[3] + P4 + byte[4] + byte[5] + byte[6] + byte[7]


def fixHammingError(byte, pos):
    return byte[:pos] + str(int(byte[pos]) ^ 1) + byte[pos + 1:]


def undoHammingByte(byte):
    """Decomposes hamming code back to byte"""
    output = byte[3] + byte[5] + byte[6] + byte[7] +\
    byte[9] + byte[10] + byte[11] + byte[12]
    return output


def calculateHammingSyndrom(byte):
    """Calculates hamming syndrom"""
    #S0 = C1 xor C3 xor C5 xor C7 xor C9 xor C11
    S0 = str(
        int(byte[1]) ^
        int(byte[3]) ^
        int(byte[5]) ^
        int(byte[7]) ^
        int(byte[9]) ^
        int(byte[11])
        )
    #S1 = C2 xor C3 xor C6 xor C7 xor C10 xor C11
    S1 = str(
        int(byte[2]) ^
        int(byte[3]) ^
        int(byte[6]) ^
        int(byte[7]) ^
        int(byte[10]) ^
        int(byte[11])
        )
    #S2 = C4 xor C5 xor C6 xor C7 xor C12
    S2 = str(
        int(byte[4]) ^
        int(byte[5]) ^
        int(byte[6]) ^
        int(byte[7]) ^
        int(byte[12])
        )
    #S3 = C8 xor C9 xor C10 xor C11 xor C12
    S3 = str(
        int(byte[8]) ^
        int(byte[9]) ^
        int(byte[10]) ^
        int(byte[11]) ^
        int(byte[12])
        )
    #SX = C1 to C12
    SX = str(
        int(byte[0]) ^
        int(byte[1]) ^
        int(byte[2]) ^
        int(byte[3]) ^
        int(byte[4]) ^
        int(byte[5]) ^
        int(byte[6]) ^
        int(byte[7]) ^
        int(byte[8]) ^
        int(byte[9]) ^
        int(byte[10]) ^
        int(byte[11]) ^
        int(byte[12])
        )
    S = int(S3 + S2 + S1 + S0, 2)
    return {"SX": int(SX), "S": S}

