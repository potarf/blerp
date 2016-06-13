#!/usr/bin/python

#blerp.py

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-a",action="store_true",dest="attackMode",default=False,\
                  help="ATTACK MODE")
parser.add_option("-b",action="store_true",dest="suppressBees",default=False,\
                  help="SUPPRESS BEES")
parser.add_option("-_",action="store_true",dest="dashes",default=False,\
                  help="FLAG USE EM DASHES")
parser.add_option("-c",action="store_true",dest="countArgs",default=False,\
                  help="COUNT NUMBER OF ARGUMENTS")
parser.add_option("-d",action="store_true",dest="debug",default=False,\
                  help="PIPES OUTPUT TO DEBUG.EXE")
parser.add_option("-D",action="store_true",dest="depracated",default=False,\
                  help="DEPRECATED")
parser.add_option("-e",action="store_true",dest="execute",default=False,\
                  help="EXECUTE SOMETHING")
parser.add_option("-f",action="store_true",dest="fun",default=False,\
                  help="FUN MODE")
parser.add_option("-g",action="store_true",dest="google",default=False,\
                  help="USE GOOGLE")
parser.add_option("-H",action="store_true",dest="halts",default=False,\
                  help="CHECK WHETHER INPUT HALTS")
parser.add_option("-i",action="store_true",dest="ignoreLower",default=False,\
                  help="IGNORE CASE (LOWER)")
parser.add_option("-I",action="store_true",dest="ignoreUpper",default=False,\
                  help="IGNORE CASE (UPPER)")
parser.add_option("--jk",action="store_true",dest="kidding",default=False,\
                  help="KIDDING")


options, args = parser.parse_args()
