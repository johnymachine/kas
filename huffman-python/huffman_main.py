# -*- coding: utf-8 -*-
"""Module for personal huffman coder."""

import argparse
import time
import os
import huffcoder
import binpacker


def setup_parser():
    '''
    Basic parser setup for simple huffman command line input.
    '''
    parser = argparse.ArgumentParser(description='Command line huffman coder')
    parser.add_argument("-i", "--input", required=True,
    help="Insert path to input file.")
    parser.add_argument("-o", "--output", required=True,
    help="Insert path to output file.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-K", "--encode", action="store_true",
    help="Swiches to encoding")
    group.add_argument("-D", "--decode", action="store_true",
    help="Swiches to decoding")
    return parser


def main():
    '''
    Main program handler
    '''
    parser = setup_parser()
    args = parser.parse_args()

    inputfile = args.input
    outputfile = args.output

    #inputfile = "output.huff"
    #outputfile = "input.rebuild.txt"
    #selection = "D"

    print "Welcome to Huffman code command line tool."
    print "Jan Gabriel FMTUL (jan.gabriel(at)tul.cz"
    print "========================================================"
    print "from: " + inputfile + " =====>>>>> to: " + outputfile
    if(args.encode):
        print "You have selected to ENCODE"
        print "========================================================"
        start_time = time.time()
        with open(inputfile, "rb") as ifile:
            txt = binpacker.readBinaryToEncode(ifile)
        encoded = huffcoder.huffmanEncode(txt)
        packed = binpacker.packData(encoded["output"], encoded["occurrence"])
        with open(outputfile, "wb") as ofile:
            ofile.write(packed)
        end_time = time.time()
        oldsize = os.path.getsize(inputfile)
        newsize = os.path.getsize(outputfile)
        compratio = (newsize / float(oldsize)) * 100
        insec = end_time - start_time
        print "You have succesfully ENCODED the file!"
        print "%.3fkB => %.3fkB = %.2f" % (oldsize / 1000.0,
        newsize / 1000.0, compratio) + "% compression."
        print "===================In: %.5s seconds!===================" % insec
    elif(args.decode):
        print "You have selected to DECODE"
        print "========================================================"
        start_time = time.time()
        with open(inputfile, "rb") as ifile:
            txt = binpacker.readBinaryToDecode(ifile)
        unpacked = binpacker.unpackData(txt)
        decoded = huffcoder.huffmanDecode(unpacked["output"],
        unpacked["occurrence"])
        with open(outputfile, "wb") as ofile:
            ofile.write(decoded["output"])
        end_time = time.time()
        oldsize = os.path.getsize(inputfile)
        newsize = os.path.getsize(outputfile)
        compratio = (newsize / float(oldsize)) * 100
        insec = end_time - start_time
        print "You have succesfully DECODED the file!"
        print "%.3fkB => %.3fkB = %.2f" % (oldsize / 1000.0,
        newsize / 1000.0, compratio) + "% compression."
        print "===================In: %.5s seconds!===================" % insec
    else:
        print "Sorry, something went terribly wrong!"
    os.system("pause")
    return 0

if __name__ == "__main__":
    main()