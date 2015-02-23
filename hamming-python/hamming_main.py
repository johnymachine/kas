# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Module for personal hamming coder."""

import argparse
import time
import os
import hammcoder
import binpacker
import errormaker


def setup_parser():
    '''
    Basic parser setup for simple hamming command line input.
    '''
    parser = argparse.ArgumentParser(description='Command line hamming coder')
    parser.add_argument("-i", "--input", required=True,
    help="Insert path to input file.")
    parser.add_argument("-o", "--output", required=True,
    help="Insert path to output file.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-K", "--encode", action="store_true",
    help="Swiches to encoding")
    group.add_argument("-D", "--decode", action="store_true",
    help="Swiches to decoding")
    group.add_argument("-1", "--singleerror", action="store_true",
    help="Injects input file with single bit errors")
    group.add_argument("-2", "--doubleerror", action="store_true",
    help="Injects input file with double bit errors")
    group.add_argument("-3", "--tripleerror", action="store_true",
    help="Injects input file with triple bit errors")
    group.add_argument("-R", "--randomerror", action="store_true",
    help="Injects input file with random bit errors")
    return parser


def main():
    '''
    Main program handler
    '''
    parser = setup_parser()
    args = parser.parse_args()

    inputfile = args.input
    outputfile = args.output

    #inputfile = "input.txt"
    #outputfile = "output.hamm"

    #inputfile = "output.hamm"
    #outputfile = "input.rebulild.txt"

    ##inputfile = "output.hamm"
    ##outputfile = "output.singleerrors.hamm"

    #inputfile = "output.singleerrors.hamm"
    #outputfile = "input.rebulild.txt"

    print "Welcome to Hamming code command line tool."
    print "Jan Gabriel FMTUL (jan.gabriel(at)tul.cz"
    print "========================================================"
    print "from: " + inputfile + " =====>>>>> to: " + outputfile
    if(args.encode):
        print "You have selected to ENCODE"
        print "========================================================"
        start_time = time.time()
        with open(inputfile, "rb") as ifile:
            buff = binpacker.readBinaryToEncode(ifile)
        output = hammcoder.hammingEncode(buff)
        with open(outputfile, "wb") as ofile:
            binpacker.writeBinaryToEncode(ofile, output)
        end_time = time.time()
        oldsize = os.path.getsize(inputfile)
        newsize = os.path.getsize(outputfile)
        compratio = (newsize / float(oldsize)) * 100
        insec = end_time - start_time
        print "You have succesfully ENCODED the file!"
        print "%.3fkB => %.3fkB = %.2f" % (oldsize / 1000.0,
        newsize / 1000.0, compratio) + "% increase in file size."
        print "===================In: %.5s seconds!===================" % insec
    elif(args.decode):
        print "You have selected to DECODE"
        print "========================================================"
        start_time = time.time()
        with open(inputfile, "rb") as ifile:
            buff = binpacker.readBinaryToDecode(ifile)
        output = hammcoder.hammingDecode(buff)
        with open(outputfile, "wb") as ofile:
            binpacker.writeBinaryToDecode(ofile, output["output"])
        end_time = time.time()
        oldsize = os.path.getsize(inputfile)
        newsize = os.path.getsize(outputfile)
        compratio = (newsize / float(oldsize)) * 100
        insec = end_time - start_time
        if len(output["log"]) == 0:
            print "You have succesfully DECODED the file!"
        else:
            for log in output["log"]:
                print log
        print "%.3fkB => %.3fkB = %.2f" % (oldsize / 1000.0,
        newsize / 1000.0, compratio) + "% decrease in file size."
        print "===================In: %.5s seconds!===================" % insec
    elif(args.singleerror or args.doubleerror
     or args.tripleerror or args.randomerror):
        start_time = time.time()
        with open(inputfile, "rb") as ifile:
            buff = binpacker.readBinaryToDecode(ifile)
        if(args.singleerror):
            print "You have selected to INJECT SINGLE ERRORS"
            print "========================================================"
            buff = errormaker.makeSingleError(buff)
        elif(args.doubleerror):
            print "You have selected to INJECT DOUBLE ERRORS"
            print "========================================================"
            buff = errormaker.makeDoubleError(buff)
        elif(args.tripleerror):
            print "You have selected to INJECT TRIPLE ERRORS"
            print "========================================================"
            buff = errormaker.makeTripleError(buff)
        elif(args.randomerror):
            print "You have selected to INJECT RANDOM ERRORS"
            print "========================================================"
            buff = errormaker.makeRandomError(buff)
        with open(outputfile, "wb") as ofile:
            binpacker.writeBinaryToEncode(ofile, buff)
        end_time = time.time()
        insec = end_time - start_time
        print "You have succesfully INJECTED ERRORS!"
        print "===================In: %.5s seconds!===================" % insec
    else:
        print "Sorry, something went terribly wrong!"
    os.system("pause")
    return 0

if __name__ == "__main__":
    main()